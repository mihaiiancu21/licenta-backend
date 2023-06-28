import importlib
import os

from BrainQuest.settings import SOLUTIONS_DIR


class PythonCompiler:
    """
    Class which handles compiling and running the solution
    provided by the user against unittest
    In this class we generate the corresponding folders for each user and problem, then we
    run the code against some input
    """

    def __init__(self, data: dict) -> None:

        self.user_code = data["user_code"]
        self.user_dir = os.path.join(SOLUTIONS_DIR, data["user"])
        self.problem_dir = os.path.join(
            self.user_dir, f"problem_{data['problem_id']}"
        )

        self.module_user = data["user"]
        self.module_problem = f"problem_{data['problem_id']}"
        self.module_solution = f"solution_problem_{data['problem_id']}"

        self.solution_file = f"solution_problem_{data['problem_id']}.py"

        self.__generate_user_dir()
        self.__generate_problem_dir()
        self.__generate_solution_file()

    def __generate_user_dir(self) -> None:
        """
        This method is responsible to ensure that each use has his proper test space.
        Its generates a folder for each user
        """
        if not os.path.exists(self.user_dir):
            os.mkdir(self.user_dir)

    def __generate_problem_dir(self) -> None:
        """
        This method is responsible to generate a problem id folder in user's test space
        """
        if not os.path.exists(self.problem_dir):
            os.mkdir(self.problem_dir)

    def __generate_solution_file(self) -> None:
        """
        This method generates and save the current solution that user submitted.
        If user submits a new version of the solution, this file gets overwritten
        """

        tmp_file = os.path.join(self.problem_dir, self.solution_file)

        with open(tmp_file, "w") as f:
            f.write(self.user_code)

        init_file = os.path.join(self.problem_dir, "__init__.py")

        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                f.write('# empty __init__ autogenerated\n')

    def compile_solution(self, all_test_cases: bool = False) -> dict:
        try:
            # import the module for user dynamically
            solution_module = importlib.import_module(
                f'solutions.{self.module_user}.{self.module_problem}.{self.module_solution}'
            )

            # import the unittest module responsible for testing the current problem
            unittest_module = importlib.import_module(
                f'restapi.utils.compiler.unittests.unittests_{self.module_problem}.test'
            )

            # get the unittests
            if all_test_cases:
                test_cases = unittest_module.get_all_test_cases()
            else:
                test_cases = unittest_module.get_primary_test_cases()

            expected = unittest_module.get_expected_outputs()

            passed_test_cases = 0
            all_test_cases = {}

            method_to_test_expected = test_cases["method_to_test"]
            test_cases = test_cases["test_cases"]
            test_cases_count = len(test_cases)

            for label in test_cases.keys():

                # import the class solution and try to execute the code
                obj_solution = solution_module.Solution()

                # call the solution method dynamically
                _method_obj = getattr(obj_solution, method_to_test_expected)
                code_result = _method_obj(*test_cases[label])

                if code_result == expected[label]:
                    passed_test_cases += 1
                    all_test_cases[label] = "passed"
                else:
                    all_test_cases[label] = "failed"

            stack_message = f"Passed {passed_test_cases} out of " \
                            f"{test_cases_count} test cases."

            results = {
                "command_status": "command_succeed",
                "stack_message": stack_message,
                "all_test_cases": all_test_cases
            }

            return results
        except Exception as exc:
            results = {
                "command_status": "command_error",
                "stack_message": str(exc),
                "all_test_cases": {}
            }

            return results
