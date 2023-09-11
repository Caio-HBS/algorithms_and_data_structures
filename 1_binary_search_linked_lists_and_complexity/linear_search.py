from test_cases import test_list

def linear_search(array: list, item: int) -> int:
    """
    Linear search algorithm inmplemantation in Python. Most basic search algorithm,
    Basically takes in a list/array and compares each element until it finds the
    desired one.

    Args:
        array: list containing all the elements in which to perform the search;
        item: desired item to be found in the list.

    Pros:
        - Easy solution;
        - The list doesn't need to be sorted;
        
    Cons:
        - Inefficient;

    Big O notation:
    """

    # Initialize a variable to go through the array.
    position = 0

    # Initializing the while loop this way prevents errors from empty lists.
    while position < len(array):
        # Return the position where the item was found (if it is found).
        if array[position] == item:
            return position
        # Increases the position to keep going down the array.
        position += 1
    # If the item wasn't on the array or if the array was empty, returns -1 as a default.
    return -1

# Print the tests
print("\nLINEAR SEARCH TESTS:\n")
for test in test_list:
    if (linear_search(**test['input']) == test['output']) == True:
        status = "PASSED"
    else:
        status = "FAILED"
    print(test['test_description'], ":", status)
