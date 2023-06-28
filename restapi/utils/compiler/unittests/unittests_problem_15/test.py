# compile and run test cases
def get_primary_test_cases():
    return {
        "method_to_test": "longest",
        "test_cases": {
            "Test Case 1": (["abc", "cb", "a"], 3),
            "Test Case 2": (["abc", "cb", "aaaaaa"], 3),
        }
    }


# for submit and get score
def get_all_test_cases():
    return {
        "method_to_test": "longest",
        "test_cases": {
            "Test Case 1": (["abc", "cb", "a"], 3),
            "Test Case 2": (["abc", "cb", "aaaaaa"], 3),
            "Test Case 3": (["abc", "bcd", "cda"], 3),
            "Test Case 4": (["elicopter", "BrainQuest", "casa", "masa"], 4),
        }
    }


def get_expected_outputs():
    return {
        "Test Case 1": "abc",
        "Test Case 2": "aaaaaa",
        "Test Case 3": "abc",
        "Test Case 4": "BrainQuest",
    }
