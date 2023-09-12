from test_cases import test_list

from utils import test_location


def binary_search(array: list, item: int) -> int:
    """
    Binary search algorithm inmplemantation in Python. Basically takes the element
    in the middle of the list/array and compares them to the desired item. If they
    match, returns it, then eliminates half the elements based on them being
    greater or lower them the middle item. Does this recursively until the
    item is found (or returns -1).

    Args:
        array: list containing all the elements in which to perform the search;
        item: desired item to be found in the list.

    Pros:
        - Eliminates half the elements every cycle, making it quite efficient.

    Cons:
        - List/array HAS to be sorted previously.

    Big O notation: O(log n)
    """

    # Initiates two variables to keep track of the beggining and the and of the
    # array.
    lowest, highest = 0, len(array) - 1

    # Creates a loop that should only break when the list only has one item; also
    # makes sure the list is not empty to begin with.
    while lowest <= highest:
        middle = (lowest + highest) // 2
        # Calls in the helper function to make a few checks on the item.
        result = test_location(array, item, middle)

        # Based on the result of the helper function, tells the program to look
        # on the left side or right side of the list as it narrows it down.
        if result == "found":
            return middle
        elif result == "left":
            highest = middle - 1
        elif result == "right":
            lowest = middle + 1

    # The item is not on the list/array or the list/array is empty.
    return -1


# Print the tests
print("\nBINARY SEARCH TESTS:\n")
for test in test_list:
    if (binary_search(**test["input"]) == test["output"]) == True:
        status = "PASSED"
    else:
        status = "FAILED"
    print(test["test_description"], ":", status)
