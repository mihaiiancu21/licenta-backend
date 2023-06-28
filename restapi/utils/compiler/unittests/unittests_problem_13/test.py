# compile and run test cases
def get_primary_test_cases():
    return {
        "method_to_test": "series_sum",
        "test_cases": {
            "Test Case 1": (5,),
            "Test Case 2": (10,),
        }
    }


# for submit and get score
def get_all_test_cases():
    return {
        "method_to_test": "series_sum",
        "test_cases": {
            "Test Case 1": (5,),
            "Test Case 2": (10,),
            "Test Case 3": (20,),
            "Test Case 4": (0,),
            "Test Case 5": (-1,),
            "Test Case 6": (55,),
            "Test Case 7": (-5,),
            "Test Case 8": (-8,),
            "Test Case 9": (1000,),
            "Test Case 10": (1000000,)
        }
    }


def get_expected_outputs():
    return {
        "Test Case 1": 15,
        "Test Case 2": 55,
        "Test Case 3": 210,
        "Test Case 4": 0,
        "Test Case 5": 0,
        "Test Case 6": 1540,
        "Test Case 7": 0,
        "Test Case 8": 0,
        "Test Case 9": 500500,
        "Test Case 10": 0
    }
