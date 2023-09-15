from utils import (
    tree_size,
    tree_height,
    display_keys,
    tree_to_tuple,
    traverse_in_order,
    traverse_pre_order,
    traverse_post_order,
)


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


# Tests
tree2 = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print("\nDisplay tree vertically:\n")
display_keys(tree2, "  ")

tree3 = tree_to_tuple(tree2)
print("\nTree to Tuple:", tree3)

print("\nTraverse tree inorder:", traverse_in_order(tree2))
print("Traverse tree preorder:", traverse_pre_order(tree2))
print("Traverse tree postorder:", traverse_post_order(tree2))

print("\nTree height (maximum):", tree_height(tree2))
print("Tree height (minimum):", tree_height(tree2, minimum=True))
print("Tree size:", tree_size(tree2))
