def display_keys(node, space="\t", level=0):
    """
    Displays the binary tree vertically by using recursion.

    Args:
        node: the node object itself;
        space: the space beetween each node;
        level: the vertical level on the tree (branches).
    """

    # Handles empty nodes.
    if node is None:
        print(space * level + "∅")
        return

    # Handles leaves.
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # Handles nodes with children.
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)


def traverse_in_order(node):
    """
    Traverses the tree in the left subtree, root, right subtree configuration.

    Args:
        node: the node object itself.
    """

    # Handles the nodes that don't exist.
    if node is None:
        return []

    return traverse_in_order(node.left) + [node.key] + traverse_in_order(node.right)


def tree_height(node, minimum=False) -> int:
    """
    Returns the tree height.

    Args:
        node: the node object itself.
        minimum: defines if the desired value is the minimum or maximum height of
        the tree. Defaults to False.
    """

    # Handles the nodes that don't exist (leaves).
    if node is None:
        return 0

    # Handles the minimum height cases should the user want it.
    if minimum:
        return 1 + min(tree_height(node.left), tree_height(node.right))

    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node) -> int:
    """
    Returns the tree size (number of nodes).

    Args:
        node: the node object itself.
    """

    # Handles the nodes that don't exist (leaves).
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


# ------------------------------EXERCISES----------------------------------------

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


"""
Exercise: Define two functions that traverse a binary tree both in preorder, as 
well as in post order. Hint: Use recursion.
"""


def traverse_pre_order(node):
    """
    Traverses the tree in the root, left subtree, right subtree configuration.

    Args:
        node: the node object itself.
    """

    # Handles the nodes that don't exist.
    if node is None:
        return []

    return [node.key] + traverse_in_order(node.left) + traverse_in_order(node.right)


def traverse_post_order(node):
    """
    Traverses the tree in the left subtree, right subtree, root configuration.

    Args:
        node: the node object itself.
    """

    # Handles the nodes that don't exist.
    if node is None:
        return []

    return traverse_in_order(node.left) + traverse_in_order(node.right) + [node.key]
