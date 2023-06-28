# compile and run test cases
def get_primary_test_cases():
    return {
        "method_to_test": "search",
        "test_cases": {
            "Test Case 1": ([1, 2, 3], 3, 2),
            "Test Case 2": ([1, 2, 3, 4, 5, 6], 6, 4),
        }
    }


# for submit and get score
def get_all_test_cases():
    return {
        "method_to_test": "search",
        "test_cases": {
            "Test Case 1": ([1, 2, 3], 3, 2),
            "Test Case 2": ([1, 2, 3, 4, 5, 6], 6, 4),
            "Test Case 3": ([1, 2, 3, 4, 5, 6], 6, 7),
            "Test Case 4": ([1, 2, 3, 4, 4, 4, 5], 7, 4),
            "Test Case 5": ([x for x in range(1, 100)], 100, 97),
            "Test Case 6": ([x for x in range(1, 100)], 100, 101),
        }
    }


def get_expected_outputs():
    return {
        "Test Case 1": 1,
        "Test Case 2": 3,
        "Test Case 3": -1,
        "Test Case 4": 3,
        "Test Case 5": 96,
        "Test Case 6": -1,
    }
