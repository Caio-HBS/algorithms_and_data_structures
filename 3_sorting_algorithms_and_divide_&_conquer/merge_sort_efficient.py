"""
QUESTION 1: You're working on a new feature on Jovian called "Top Notebooks of 
the Week". Write a function to sort a list of notebooks in decreasing order of 
likes. Keep in mind that up to millions of notebooks can be created every week, 
so your function needs to be as efficient as possible.
"""


class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes

    def __repr__(self):
        return f'Notebook <"{self.username}/{self.title}", {self.likes} likes>'
    

def default_compare(x, y) -> str:
    """
    Helper function to compare two notebooks.

    Args:
        x: the first notebook value for comparasion;
        y: the second notebook value for comparasion.
    """

    if x < y:
        return "less"
    elif x == y:
        return "equal"
    else:
        return "greater"
    

def compare_likes(nb1, nb2) -> str:
    """
    Helper function to compare the amount of likes in two notebooks.

    Args:
        nb1: the first notebook for comparasion;
        nb2: the second notebook for comparasion.
    """

    if nb1.likes > nb2.likes:
        return "lesser"
    elif nb1.likes == nb2.likes:
        return "equal"
    elif nb1.likes < nb2.likes:
        return "greater"
    

def compare_titles(nb1, nb2) -> str:
    """
    Helper function to compare the titles in two notebooks.

    Args:
        nb1: the first notebook title for comparasion;
        nb2: the second notebook title for comparasion.
    """

    if nb1.title < nb2.title:
        return "lesser"
    elif nb1.title == nb2.title:
        return "equal"
    elif nb1.title > nb2.title:
        return "greater"
    

def merge(left, right, compare):
    """
    Helper function to merge two lists. Compares the first elements of the 
    two lists and appends the smaller one to the merged array until one of 
    the lists is exhausted; proceeds to append the last elements in that case.

    Args:
        left: the first sorted array;
        right: the second sorted array;
        compare: the type of comparasion to be done.
    """

    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == "lesser" or result == "equal":
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]


def merge_sort(objs, compare=default_compare):
    """
    Implementation of Merge Sort in Python.

    Args:
        objs: array to be sorted;
        compare: the type of comparasion. Defaults to 'default_compare'.
    """

    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(
        merge_sort(objs[:mid], compare),
        merge_sort(objs[mid:], compare),
        compare
    )


# TODO: Implementation of quicksort and bubble sort.