"""
QUESTION 1: You're working on a new feature on Jovian called "Top Notebooks of 
the Week". Write a function to sort a list of notebooks in decreasing order of 
likes. Keep in mind that up to millions of notebooks can be created every week, 
so your function needs to be as efficient as possible.
"""
from test_cases_for_sorting import test_list


def sort_list(array: list) -> list:
    """
    Simple implementation of bubble-sort in Python.

    Args:
        array: list of items to be sorted.
    """

    # Two variables, the first one retrieves the length of the list; the second
    # is a boolean to keep track of the position-swapping of items.
    n = len(array)
    swapped = True

    # If a whole passage of the list doesn't change the variable, we know the
    # list is sorted.
    while swapped:
        swapped = False

        for i in range(n - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                # Changes the 'swapped' boolean back to True so we know there's
                # still unordered items.
                swapped = True

    return array


# Print the tests
print("\nBINARY SEARCH TESTS:\n")
for test in test_list:
    if (sort_list(**test["input"]) == test["output"]) == True:
        status = "PASSED"
    else:
        status = "FAILED"
    print(test["test_description"], ":", status)
