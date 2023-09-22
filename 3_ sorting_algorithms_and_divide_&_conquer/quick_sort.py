from test_cases_for_sorting import test_list


def partition(array: list, start: int=0, end=None) -> int:
    """
    Helper function to allow partitioning for quicksort.

    Args:
        list_of_nums: list of numbers to be partitioned;
        start: start position of the list;
        end: end position of the list.
    """

    # Assigns the end position of the list to the variable 'end'.
    if end is None:
        end = (len(array) - 1)
    
    # Initialize right and left pointers in the beggining and the second to last 
    # positions of the list.
    left_pointer, right_pointer = start, (end - 1)
    
    # Iterate while they're apart from each other.
    while right_pointer > left_pointer:
        
        # Increment left pointer if number is less or equal to pivot (since its 
        # already in its right side).
        if array[left_pointer] <= array[end]:
            left_pointer += 1
        
        # Decrement right pointer if number is greater than pivot (since its 
        # already in its right side).
        elif array[right_pointer] > array[end]:
            right_pointer -= 1
        
        # Two out-of-place elements found, swap them.
        else:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]

    # Sends the pivot to its correct place (if it wasn't already there to begin 
    # with).
    if array[left_pointer] > array[end]:
        array[left_pointer], array[end] = array[end], array[left_pointer]
        return left_pointer
    else:
        return end


def quick_sort(array: list, start: int=0, end=None) -> list:
    """
    Implementation of quicksort in Python.

    Args:
        list_on_nums: the list to be ordered;
        start: the beggining of the list to be ordered. Defaults to 0;
        end: the end of the list to be ordered. Defaults to None.
    """

    # Gets the last position.
    if end is None:
        end = (len(array) - 1)
    

    # I.e. the list has more then one element. 
    if start < end:
        # Sets the pivot (last element) to be the middle of the list and then call
        # quicksort on the other two halves.
        pivot = partition(array, start, end)
        quick_sort(array, start, (pivot - 1))
        quick_sort(array,(pivot + 1), end)

    return array


# Print the tests
print("\nQUICKSORT TESTS:\n")
for test in test_list:
    if (quick_sort(**test["input"]) == test["output"]) == True:
        status = "PASSED"
    else:
        status = "FAILED"
    print(test["test_description"], ":", status)
