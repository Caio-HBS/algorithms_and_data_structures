from test_cases_for_sorting import test_list


def merge(nums1: list, nums2: list) -> list:
    """
    Helper function to merge two lists. Compares the first elements of the two 
    lists and appends the smaller one to the merged array until one of the lists 
    is exhausted; proceeds to append the last elements in that case.

    Args:
        nums1: the first sorted array.
        nums2: the second sorted array.
    """

    # List to store the results.
    merged = []

    # Indices for iteration.
    i, j = 0, 0

    # Loop over the two lists.
    while i < len(nums1) and j < len(nums2):
        # Include the smaller element in the result array and move to next element.
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Get the remaining parts.
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # Return the final merged array.
    return merged + nums1_tail + nums2_tail


def merge_sort(array: list) -> list:
    """
    Implementation of Merge Sort in Python.

    Args:
        array: list to be sorted.
    """

    # Terminating condition (list of 0 or 1 elements).
    if len(array) <= 1:
        return array

    # Get the midpoint.
    mid = len(array) // 2

    # Split the list into two halves.
    left = array[:mid]
    right = array[mid:]

    # Solve the problem for each half recursively.
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Combine the results of the two halves.
    sorted_nums = list(merge(left_sorted, right_sorted))

    return sorted_nums


# Print the tests
print("\nBINARY SEARCH TESTS:\n")
for test in test_list:
    if (merge_sort(**test["input"]) == test["output"]) == True:
        status = "PASSED"
    else:
        status = "FAILED"
    print(test["test_description"], ":", status)
