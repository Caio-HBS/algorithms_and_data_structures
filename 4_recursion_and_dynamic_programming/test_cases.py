from colorama import Fore, Style

def test_print(test_cases, function):
    for test in test_cases:
        if (function(**test["input"]) == test["output"]) == True:
            status = "PASSED"
        else:
            status = "FAILED"
        
        if status == "PASSED":
            print(test["test_description"], ":", Fore.GREEN + status, Style.RESET_ALL)
        else:
            print(test["test_description"], ":", Fore.RED + status, Style.RESET_ALL)

test_list = [
    {
        'test_description': 'The subsequence exists (strings)',
        'input': {
            'seq1': 'serendipitous',
            'seq2': 'precipitation',
        },
        'output': 7
    },
    {
        'test_description': 'The subsequence exists (lists)',
        'input': {
            'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
            'seq2': [6, 2, 4 ,7, 1, 5, 6, 2, 3],
        },
        'output': 5
    },
    {
        'test_description': 'The subsequence doesn\'t exist',
        'input': {
            'seq1': 'serendipitous',
            'seq2': 'abba',
        },
        'output': 0
    },
    {
        'test_description': 'The subsequence is equal to one of the provided sequence',
        'input': {
            'seq1': 'participation',
            'seq2': 'art',
        },
        'output': 3
    },
    {
        'test_description': 'One of the subsequence is empty',
        'input': {
            'seq1': 'bomb',
            'seq2': '',
        },
        'output': 0
    },
    {
        'test_description': 'Both sequences are empty',
        'input': {
            'seq1': '',
            'seq2': '',
        },
        'output': 0
    },
    {
        'test_description': 'Multiple subsequences with the same length',
        'input': {
            'seq1': 'abcdef',
            'seq2': 'badcfe',
        },
        'output': 3
    },
]