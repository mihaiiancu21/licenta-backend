# compile and run test cases
def get_primary_test_cases():
    return {
        "method_to_test": "sortedMatrix",
        "test_cases": {
            "Test Case 1": (
                4, [
                    [10, 20, 30, 40],
                    [15, 25, 35, 45],
                    [27, 29, 37, 48],
                    [32, 33, 39, 50]
                ]
            ),
            "Test Case 2": (
                2, [
                    [1, 5],
                    [2, 3]
                ]
            ),
        }
    }


# for submit and get score
def get_all_test_cases():
    return {
        "method_to_test": "sortedMatrix",
        "test_cases": {
            "Test Case 1": (
                4, [
                    [10, 20, 30, 40],
                    [15, 25, 35, 45],
                    [27, 29, 37, 48],
                    [32, 33, 39, 50]
                ]
            ),
            "Test Case 2": (
                2, [
                    [1, 5],
                    [2, 3]
                ]
            ),
            "Test Case 3": (
                5, [
                    [100, 20, 30, 40, 1000],
                    [50, 25, 35, 45, 50],
                    [27, 29, 1, 48, 21],
                    [32, 33, 99, 50, 456],
                    [12, 5653, 109, 220, 456],
                ]
            ),
        }
    }


def get_expected_outputs():
    return {
        "Test Case 1": [
            [10, 15, 20, 25],
            [27, 29, 30, 32],
            [33, 35, 37, 39],
            [40, 45, 48, 50]
        ],
        "Test Case 2": [
            [1, 2],
            [3, 5],
        ],
        "Test Case 3": [
            [1, 12, 20, 21, 25],
            [27, 29, 30, 32, 33],
            [35, 40, 45, 48, 50],
            [50, 50, 99, 100, 109],
            [220, 456, 456, 1000, 5653],
        ],
    }
