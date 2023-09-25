"""
Write a function to find the length of the LONGEST COMMON SUBSEQUENCE betweenm 
two sequences. E.g. Given the strings "serendipitous" and "precipitation", the 
longest common subsequence is "reipito" and its length is 7.

A "sequence" is a group of items with a deterministic ordering. Lists, tuples 
and ranges are some common sequences in Python.

A "subsequence" is a sequence obtained by deleting zero or more elements from 
another sequence. For exemple, "edpt" is a subsequence of "serendipitous"
"""
from colorama import Fore, Style

from test_cases import test_list, test_print


# Recursion approach.
def long_common_subseq_recursion(seq1, seq2, idx1: int = 0, idx2: int = 0) -> int:
    """
    Two sequences (strings, ints etc.) are provided and the function returns the
    length to the longest common subsequence, which means the longest piece of
    characters to appear in the same order on both sequences. Recursion approach.

    Args:
        seq1: a sequence such as "serendipitous";
        seq2: a sequence such as "precipitation";
        idx1: initializes the first index for recursion. Defaults to 0;
        idx2: initializes the second index for recursion. Defaults to 0.
    """

    # The index has reached the end of the sequence.
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0

    # A match has been found, so increment the counter.
    elif seq1[idx1] == seq2[idx2]:
        return 1 + long_common_subseq_recursion(seq1, seq2, (idx1 + 1), (idx2 + 1))

    # Either ignore the first element of the first or the second sequence based
    # on the larger number.
    else:
        option1 = long_common_subseq_recursion(seq1, seq2, (idx1 + 1), idx2)
        option2 = long_common_subseq_recursion(seq1, seq2, idx1, (idx2 + 1))
        return max(option1, option2)


# Memoization approach.
def long_common_subseq_memo(seq1, seq2):
    """
    Two sequences (strings, ints etc.) are provided and the function returns the
    length to the longest common subsequence, which means the longest piece of
    characters to appear in the same order on both sequences. Memoization approach.

    Args:
        seq1: a sequence such as "serendipitous";
        seq2: a sequence such as "precipitation";

    """

    # Dictionary to store solved problems within the function.
    memo = {}

    def recurse(idx1: int = 0, idx2: int = 0) -> 0:
        """
        Args:
            idx1: initializes the first index for recursion. Defaults to 0;
            idx2: initializes the second index for recursion. Defaults to 0.
        """
        key = (idx1, idx2)

        # The problem was solved previously, so just return the result we already
        # have.
        if key in memo:
            return memo[key]

        # The index has reached the end of the sequence.
        elif idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0

        # A match has been found, so increment the counter.
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse((idx1 + 1), (idx2 + 1))

        # Either ignore the first element of the first or the second sequence based
        # on the larger number.
        else:
            memo[key] = max(recurse((idx1 + 1), idx2), recurse(idx1, (idx2 + 1)))

        return memo[key]

    return recurse()


# Dynamic programming approach.
def long_common_subseq_dynamic(seq1, seq2):
    """
    Two sequences (strings, ints etc.) are provided and the function returns the
    length to the longest common subsequence, which means the longest piece of
    characters to appear in the same order on both sequences. Dynamic programming
    approach.

    Args:
        seq1: a sequence such as "serendipitous";
        seq2: a sequence such as "precipitation";

    """

    # Creates a table the size of the two sequences.
    n1, n2 = len(seq1), len(seq2)
    table_of_results = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    # Iterates over the lines.
    for idx1 in range(n1):
        # Iterates over the columns.
        for idx2 in range(n2):
            
            if seq1[idx1] == seq2[idx2]:
                table_of_results[idx1 + 1][idx2 + 1] = 1 + table_of_results[idx1][idx2]

            else:
                table_of_results[idx1 + 1][idx2 + 1] = max(
                    table_of_results[idx1][idx2 + 1], table_of_results[idx1 + 1][idx2]
                )

    # Returns the bottom right element of the table.
    return table_of_results[-1][-1]


# Print the tests
print(
    "\nLONGEST COMMON SUBSEQUENCE TESTS" + Fore.CYAN + " (RECURSION):\n",
    Style.RESET_ALL,
)
test_print(test_list, long_common_subseq_recursion)

print(
    "\nLONGEST COMMON SUBSEQUENCE TESTS" + Fore.CYAN + " (MEMOIZATION):\n",
    Style.RESET_ALL,
)
test_print(test_list, long_common_subseq_memo)

print(
    "\nLONGEST COMMON SUBSEQUENCE TESTS" + Fore.CYAN + " (DYNAMIC PROGRAMMING):\n",
    Style.RESET_ALL,
)
test_print(test_list, long_common_subseq_dynamic)
