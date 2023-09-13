test_list = [
    {
        'test_description': "The list isn't rotated",
        'input': {
            'rotated': [0, 1, 2, 3, 4, 5, 6],
        },
        'output': 0
    },
    {
        'test_description': 'The list was rotated 2 times',
        'input': {
            'rotated': [5, 6, 0, 1, 2, 3, 4],
        },
        'output': 2
    },
    {
        'test_description': 'The list was rotated 1 time',
        'input': {
            'rotated': [6, 0, 1, 2, 3, 4, 5],
        },
        'output': 1
    },
    {
        'test_description': 'The list was rotated 6 rotated',
        'input': {
            'rotated': [1, 2, 3, 4, 5, 6, 0],
        },
        'output': 6
    },
]