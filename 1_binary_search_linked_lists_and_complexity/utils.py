def test_location(array: list, item: int, mid: int) -> str:
    """
    Helper function to make sure we return the first occurrence of a duplicated
    item in a list.

    Args:
        array: list containing all the elements in which to perform the search;
        item: desired item to be found in the list;
        mid: the middle element in the array.
    """

    middle_element = array[mid]

    if middle_element == item:
        # Handles the cases where the gotten item has duplicates before the element.
        if (mid - 1) >= 0 and array[(mid - 1)] == item:
            return "left"
        # Handles the cases where there are no duplicates before it (and the cases
        # where there duplicates, but after the element).
        else:
            return "found"
    # The following simply tell the binary search whether to look on the right or
    # on the left of the element.
    elif middle_element < item:
        return "left"
    else:
        return "right"
