from rest_framework import generics, status
from rest_framework.response import Response

from restapi.utils.compiler.compile_and_run import PythonCompiler


class CompilerRunCodeView(generics.ListCreateAPIView):
    """
    Compile/Execute code for user for a small amount of testcases
    """

    def create(self, request, *args, **kwargs):
        obj = PythonCompiler(data=request.data)
        results = obj.compile_solution()
        results = check_test_cases(results)

        return Response(data=results, status=status.HTTP_200_OK)


class CompilerSubmitSolutionView(generics.ListCreateAPIView):
    """
    Submit the solution for the current problem and runt against multiple unittests
    """

    def create(self, request, *args, **kwargs):
        obj = PythonCompiler(data=request.data)
        results = obj.compile_solution(all_test_cases=True)

        # compute the score obtained by the user
        test_case_passed = 0

        if results["command_status"] == "command_succeed":

            total_points = request.data["points"]
            test_cases_count = len(results["all_test_cases"])

            point_per_test_case = total_points / test_cases_count
            for k, v in results["all_test_cases"].items():
                if v == "passed":
                    test_case_passed += 1

            total_score = point_per_test_case * test_case_passed
            results["score_obtained"] = total_score

            results = check_test_cases(results)

        else:
            results["score_obtained"] = 0
            results["test_cases_passed"] = 0

        return Response(data=results, status=status.HTTP_200_OK)


def check_test_cases(compiling_results: dict) -> dict:
    test_case_passed = 0
    for k, v in compiling_results["all_test_cases"].items():
        if v == "passed":
            test_case_passed += 1

    # no passed test_cases
    if test_case_passed == 0:
        compiling_results["test_cases_passed"] = 0

    # partial passed
    if 0 < test_case_passed < len(compiling_results["all_test_cases"]):
        compiling_results["test_cases_passed"] = 1

    # all testcases passed
    if test_case_passed == len(compiling_results["all_test_cases"]):
        compiling_results["test_cases_passed"] = 10

    return compiling_results
