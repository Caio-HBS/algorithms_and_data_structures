import random


really_long_random_list = list(range(1, 10001))
random.shuffle(really_long_random_list)


test_list = [
    {
        'test_description': 'List in random order',
        'input': {
            'array': [8, 5, 3, 1, 2, 7, 4, 6],
        },
        'output': [1, 2, 3, 4, 5, 6, 7, 8]
    },
    {
        'test_description': 'List already sorted',
        'input': {
            'array': [1, 2, 3, 4, 5, 6, 7, 8],
        },
        'output': [1, 2, 3, 4, 5, 6, 7, 8]
    },
    {
        'test_description': 'List sorted in descending order',
        'input': {
            'array': [8, 7, 6, 5, 4, 3, 2, 1],
        },
        'output': [1, 2, 3, 4, 5, 6, 7, 8]
    },
    {
        'test_description': 'List with repeating elements',
        'input': {
            'array': [6, 4, 2, 3, 7, 8, 1, 3, 5, 4, 3],
        },
        'output': [1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 8]
    },
    {
        'test_description': 'Empty list',
        'input': {
            'array': [],
        },
        'output': []
    },
    {
        'test_description': 'List with only one element',
        'input': {
            'array': [1],
        },
        'output': [1]
    },
    {
        'test_description': 'List with only one repeating element',
        'input': {
            'array': [1, 1, 1, 1],
        },
        'output': [1, 1, 1, 1]
    },
    {
        'test_description': 'Really long list (10000 elements)',
        'input': {
            'array': really_long_random_list,
        },
        'output': list(range(1, 10001))
    },
]