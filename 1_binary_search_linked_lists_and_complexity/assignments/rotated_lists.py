"""
You are given list of numbers, obtained by rotating a sorted list an unknown number 
of times. Write a function to determine the minimum number of times the original 
sorted list was rotated to obtain the given list. Your function should have the 
worst-case complexity of O(log N), where N is the length of the list. You can assume 
that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list
[0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding 
it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing 
order e.g. [1, 3, 5, 7].
"""
from tests_for_assignment import test_list


def how_many_rotations(rotated: list) -> int:
    """
    Uses binary search to find the point of rotation in a list that HAS to be
    sorted in increasing order.

    Args:
        rotated: rotated list.
    """
    if rotated == []:
        return -1

    left, right = 0, (len(rotated) - 1)

    # Handles the cases where the list wasn't rotated.
    if rotated[left] <= rotated[right]:
        return 0

    # Handles the cases where the list was rotated.
    while left <= right:
        mid = (left + right) // 2

        # The rotation point has been found.
        if rotated[mid] > rotated[(mid + 1)]:
            return mid + 1

        # Traditional binary search:
        if rotated[mid] >= rotated[left]:
            left = mid + 1
        else:
            right = mid - 1


# Print the tests
print("\nTEST RESULTS:\n")
for test in test_list:
    if (how_many_rotations(**test["input"]) == test["output"]) == True:
        status = "PASSED"
    else:
        status = "FAILED"
    print(test["test_description"], "\b:", status)
