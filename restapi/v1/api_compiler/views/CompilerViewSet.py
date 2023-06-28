from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from restapi.models import Problem
from restapi.utils import solution_utils
from restapi.utils.compiler.compile_and_run import PythonCompiler


class CompilerRunCodeView(generics.ListCreateAPIView):
    """
    Compile/Execute code for user for a small defined amount of testcases
    This is used more for users to test if their code it is working and has no errors
    """

    def create(self, request, *args, **kwargs):
        obj = PythonCompiler(data=request.data)
        results = obj.compile_solution()
        results = solution_utils.check_test_cases(results)
        results["compile_and_run"] = True

        return Response(data=results, status=status.HTTP_200_OK)


class CompilerSubmitSolutionView(generics.ListCreateAPIView):
    """
    Submit the solution for the current problem and run against multiple unittests
    """

    def create(self, request, *args, **kwargs):
        obj = PythonCompiler(data=request.data)
        results = obj.compile_solution(all_test_cases=True)

        user = User.objects.get(username=request.data["user"])
        problem = Problem.objects.get(pk=request.data["problem_id"])

        # compute the score obtained by the user
        test_case_passed = 0

        if results["command_status"] == "command_succeed":

            total_points = request.data["points"]
            test_cases_count = len(results["all_test_cases"])

            point_per_test_case = total_points / test_cases_count
            for k, v in results["all_test_cases"].items():
                if v == "passed":
                    test_case_passed += 1

            total_score_obtained = point_per_test_case * test_case_passed
            results["score_obtained"] = total_score_obtained

            results = solution_utils.check_test_cases(results)

            # insert in DB user submission
            solution_utils.add_solution_entry(
                user, problem, total_score_obtained, results, request
            )

            # compute rank for user (overall coding points and total problem solved)
            solution_utils.compute_user_rank(user)

            results["compile_and_run"] = False

        else:
            results["score_obtained"] = 0
            results["test_cases_passed"] = 0
            results["compile_and_run"] = False

        return Response(data=results, status=status.HTTP_200_OK)
