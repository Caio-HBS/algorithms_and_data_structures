from colorama import Fore, Style


def test_print(test_cases, function):
    for test in test_cases:
        if (function(**test["input"]) == test["output"]) == True:
            status = "PASSED"
            print(
                test["test_description"], ":", Fore.GREEN + status, Style.RESET_ALL
            )
        else:
            status = "FAILED"
            print(
                test["test_description"], ":", Fore.RED + status, Style.RESET_ALL
            )


test_list = [
    {
        "test_description": "General case 1",
        "input": {
            "weights": [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
            "profits": [92, 57, 49, 68, 60, 43, 67, 84, 87, 72],
            "capacity": 165,
        },
        "output": 309,
    },
    {
        "test_description": "General case 2",
        "input": {
            "weights": [41, 50, 49, 59, 55, 57, 60],
            "profits": [442, 525, 511, 593, 546, 564, 617],
            "capacity": 170,
        },
        "output": 1735
    },
    {
    "test_description": "General case 3",
    "input": {
        "weights": [4, 5, 6],
        "profits": [1, 2, 3],
        "capacity": 15,
    },
    "output": 6,
    },
    {
        "test_description": "General case 4",
        "input": {
            "weights": [4, 5, 1, 3, 2, 5],
            "profits": [2, 3, 1, 5, 4, 7],
            "capacity": 15,
        },
        "output": 19,
    },
    {
        "test_description": "Capacity is not enough for any weight",
        "input": {
            "weights": [4, 5, 6],
            "profits": [1, 2, 3],
            "capacity": 3,
        },
        "output": 0,
    },
    {
        "test_description": "Capacity is enough for a single weight",
        "input": {
            "weights": [4, 5, 1],
            "profits": [1, 2, 3],
            "capacity": 4,
        },
        "output": 3,
    },
]
