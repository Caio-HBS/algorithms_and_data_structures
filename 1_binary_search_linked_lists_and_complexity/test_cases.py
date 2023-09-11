test_list = [
    {
        'test_description': 'Item is in the middle of the list',
        'input': {
            'array': [10, 8, 5, 2, 0],
            'item': 5
        },
        'output': 2
    },
    {
        'test_description': 'Item is the first element of the list',
        'input': {
            'array': [10, 8, 5, 2, 0],
            'item': 10
        },
        'output': 0
    },
    {
        'test_description': 'Item is the last element of the list',
        'input': {
            'array': [10, 8, 5, 2, 0],
            'item': 0
        },
        'output': 4
    },
    {
        'test_description': 'The list has only one element, which is Item',
        'input': {
            'array': [10],
            'item': 10
        },
        'output': 0
    },
    {
        'test_description': 'The list does not contain item',
        'input': {
            'array': [10, 8, 5, 2, 0],
            'item': 9
        },
        'output': -1
    },
    {
        'test_description': 'The list is empty',
        'input': {
            'array': [],
            'item': 10
        },
        'output': -1
    },
    {
        'test_description': 'The list contains repeating numbers',
        'input': {
            'array': [10, 10, 10, 8, 8, 8, 5, 2, 2, 2, 2, 0],
            'item': 5
        },
        'output': 6
    },
    {
        'test_description': 'The list contains Item more than once',
        'input': {
            'array': [10, 8, 5, 5, 5, 2, 0],
            'item': 5
        },
        'output': 2
    },
]