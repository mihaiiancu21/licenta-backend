from django.db.models import OuterRef, Subquery

from restapi.models import UserSolutionSubmitted, UsersRank


def add_solution_entry(user, problem, total_score_obtained, results, request):
    # check if there is an entry with the current score
    tmp_obj = UserSolutionSubmitted.objects.filter(
        user=user, problem=problem, points=total_score_obtained
    )
    entry_exists = False

    if len(tmp_obj) > 0:
        entry_exists = True

    if not entry_exists:
        # if the user solved the problem and has obtained the maximum score
        # the problem is solved
        if total_score_obtained == problem.points:
            submission_obj = UserSolutionSubmitted.objects.create(
                user=user, problem=problem,
                status=UserSolutionSubmitted.STATUS_SOLVED, lang="Python",
                test_cases=results["stack_message"],
                code_submitted=request.data["user_code"],
                points=total_score_obtained
            )

        # if the user solved the problem and has obtained a lower score than maximum
        # the problem is partial solved
        elif 0 < total_score_obtained < problem.points:
            submission_obj = UserSolutionSubmitted.objects.create(
                user=user, problem=problem,
                status=UserSolutionSubmitted.STATUS_ATTEMPTED, lang="Python",
                test_cases=results["stack_message"],
                code_submitted=request.data["user_code"],
                points=total_score_obtained
            )

        # if the user didn't solve the problem and status remain unsolved
        else:
            submission_obj = UserSolutionSubmitted.objects.create(
                user=user, problem=problem,
                status=UserSolutionSubmitted.STATUS_UNSOLVED, lang="Python",
                test_cases=results["stack_message"],
                code_submitted=request.data["user_code"],
                points=total_score_obtained
            )

        submission_obj.save()


def check_test_cases(compiling_results: dict) -> dict:
    """
    Check how many testcases the current code has passed

    Args:
        compiling_results (`dict`): The results from Compiling/Running the code

    Returns:
        A `dict` with new key which represents the number of passed testcases
    """

    test_case_passed = 0
    total_testcases = len(compiling_results["all_test_cases"])

    for k, v in compiling_results["all_test_cases"].items():
        if v == "passed":
            test_case_passed += 1

    # no passed test_cases
    if test_case_passed == 0:
        compiling_results["test_cases_passed"] = 0

    # partial passed
    if 0 < test_case_passed < total_testcases:
        compiling_results["test_cases_passed"] = 1

    # all testcases passed
    if test_case_passed == total_testcases:
        compiling_results["test_cases_passed"] = 10

    return compiling_results


def compute_user_rank(user):
    # filter all problems by max points and group by problem id
    sq = UserSolutionSubmitted.objects.filter(
        problem=OuterRef('problem'),
        user=user
    ).order_by('-points')  # deferred execution

    all_max_problems = UserSolutionSubmitted.objects.filter(
        pk=Subquery(sq.values('pk')[:1])
    )

    overall_coding_points = 0
    total_problems_solved = len(all_max_problems)

    for item in all_max_problems:
        overall_coding_points += item.points

    try:
        obj = UsersRank.objects.get(user=user)
    except UsersRank.DoesNotExist:
        obj = None

    if obj is None:
        entry = UsersRank.objects.create(
            user=user,
            overall_coding_points=overall_coding_points,
            total_problems_solved=total_problems_solved
        )

        entry.save()
    else:

        obj.overall_coding_points = overall_coding_points
        obj.total_problems_solved = total_problems_solved

        obj.save()
