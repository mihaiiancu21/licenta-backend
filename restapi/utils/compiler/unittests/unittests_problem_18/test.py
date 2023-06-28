# compile and run test cases
def get_primary_test_cases():
    return {
        "method_to_test": "nextLargerElement",
        "test_cases": {
            "Test Case 1": (
                [1, 3, 2, 4],
                4
            ),
            "Test Case 2": (
                [1, 3, 2, 4, 5, 2],
                6
            ),
        }
    }


# for submit and get score
def get_all_test_cases():
    return {
        "method_to_test": "nextLargerElement",
        "test_cases": {
            "Test Case 1": (
                [1, 3, 2, 4],
                4
            ),
            "Test Case 2": (
                [1, 3, 2, 4, 5, 2],
                6
            ),
            "Test Case 3": (
                [1, 3, 2, 4, 5, 2, 1, 10],
                8
            ),
            "Test Case 4": (
                [
                    1, 3, 2, 4, 5, 2, 1, 10, 5, 5, 2, 2, 3, 55, 11, 88, 7, 8, 8, 100
                ],
                20
            ),
        }
    }


def get_expected_outputs():
    return {
        "Test Case 1": [3, 4, 4, -1],
        "Test Case 2": [3, 4, 4, 5, -1, -1],
        "Test Case 3": [3, 4, 4, 5, 10, 10, 10, -1],
        "Test Case 4": [
            3, 4, 4, 5, 10, 10, 10, 55, 55, 55, 3, 3, 55, 88, 88, 100, 8, 100, 100, -1
        ],
    }
