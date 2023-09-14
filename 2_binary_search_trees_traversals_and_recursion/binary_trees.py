class TreeNode:
    """
    Simple implementation of a binary tree in Python.
    """

    def __init__(self, key):
        """
        Sets the left and right nodes to be none so that they are independent when
        created.

        Args:
            key: the key to be added to the tree.
        """
        self.key = key
        self.left = None
        self.right = None


def parse_tuple(data):
    """
    Recursive function to create nodes for a binary tree using a tuple that
    represents the tree itself.

    Args:
        data: tuple that represent the node relations on a binary tree.
    """

    # Checks to see if data is a tuple. Also breakes the recursion on the node
    # creation by checking the length.
    if isinstance(data, tuple) and len(data) == 3:
        # Creates the root.
        node = TreeNode(data[1])
        # Creates the two nodes by using recursion.
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    # Deals with nodes that aren't present.
    elif data is None:
        node = None
    # Deals with the leaves i.e. nodes with no children.
    else:
        node = TreeNode(data)

    return node


"""
Exercise: Define a function tree_to_tuple that converts a binary tree into a tuple 
representing the same tree. E.g. tree_to_tuple converts the tree created above to 
the tuple ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))). Hint: Use recursion.
"""


def tree_to_tuple(node):
    """
    Converts a binary tree (or a node of it) into a tuple representation.

    Args:
        node: either the tree itself or a node of it.
    """

    # Catches the None nodes.
    if node is None:
        return None

    # Recursion to create the left and right nodes.
    left_node = tree_to_tuple(node.left)
    right_node = tree_to_tuple(node.right)

    # Catches the leaves (nodes without children).
    if left_node is None and right_node is None:
        return node.key
    else:
        return (left_node, node.key, right_node)
