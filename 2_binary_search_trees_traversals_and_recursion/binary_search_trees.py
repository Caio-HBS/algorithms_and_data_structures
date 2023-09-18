class BSTNode():
    """
    Binary search tree implementation.
    """
    def __init__(self, key, value=None):
        # Key-value pair
        self.key = key
        self.value = value
        # Left node.
        self.left = None
        # Right node.
        self.right = None
        # Helpful for upwards traversing.
        self.parent = None

    def remove_none(self, nums):
        """
        Deals with the non-existant nodes as well as leaves by discarding them from
        the list.

        Args: 
            nums: the binary tree in list form.
        """
        return [x for x in nums if x is not None]

    def is_bst(self, node):
        """
        Checks to see if a binary tree is a binary search tree (BST) as well as the
        minimum and maximum node keys.

        Args:
            node: the node object itself.
        """

        # Deals with the non-existant nodes/leaves.
        if node is None:
            return True, None, None

        # Gets the values of the current subtrees.
        is_bst_l, min_l, max_l = self.is_bst(node.left)
        is_bst_r, min_r, max_r = self.is_bst(node.right)

        # Is BST check (recursively for each node).
        is_bst_node = (is_bst_l and is_bst_r and 
                  (max_l is None or node.key > max_l) and 
                  (min_r is None or node.key < min_r))

        # Min and max check for the tree.
        min_key = min(self.remove_none([min_l, node.key, min_r]))
        max_key = max(self.remove_none([max_l, node.key, max_r]))

        return is_bst_node, min_key, max_key
    
    def is_balanced(self, node):
        """
        Determines if a binary search tree is balanced or not.

        Args:
            node: the node object itself.
        """

        # Deals with the non-existant nodes/leaves.
        if node is None:
            return True, 0
        
        # Checks if each subtree is balanced
        balanced_l, height_l = self.is_balanced(node.left)
        balanced_r, height_r = self.is_balanced(node.right)
        balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1

        # Determines the height of the tree.
        height = 1 + max(height_l, height_r)

        return balanced, height

    def insert(self, node, key, value):
        """
        Inserts a new node into its proper place in a binary search tree.

        Args:
            node: the node object itself;
            key: the key for the node;
            value: the value for the node.
        """

        # If the node is none, that is, if the node doesn't exist, create a new
        # one.
        if node is None:
            node = BSTNode(key, value)

        # Defines if the new node is going into the left or right subtree by 
        # comparing the keys recursively.
        elif key < node.key:
            node.left = self.insert(node.left, key, value)
            node.left.parent = node
        elif key > node.key:
            node.right = self.insert(node.right, key, value)
            node.right.parent = node
        return node
    
    def find(self, node, key):
        """
        Finds the desired node in a binary search tree.

        Args:
            node: the node object itself;
            key: the key for the node;
        """

        # Handles the cases where the node is not on the tree.
        if node is None:
            return None
        
        # Handles the cases where the node was found.
        if key == node.key:
            return node
        
        # Recursively traverses the tree in search of the node.
        if key < node.key:
            return self.find(node.left, key)
        if key > node.key:
            return self.find(node.right, key)
        
    def update(self, node, key, value):
        """
        Updates the VALUE of an existing node.

        Args:
            node: the node object itself;
            key: the key for the node;
            value: the value for the node.
        """

        # Uses the "find" function to locate the existing node.
        target = self.find(node, key)

        # So long as the node exists on the tree, updates the value.
        if target is not None:
            target.value = value

    def list_all(self, node):
        """
        Lists all the nodes in a binary search tree.

        Args:
            node: the node object itself.
        """

        # Deals with non-existant nodes/leaves.
        if node is None:
            return []
        
        # Returns the sorted list of tuples for each node using recursion and in-
        # order traversal.
        return (self.list_all(node.left) + 
                [(node.key, node.value)] + 
                self.list_all(node.right))
    

def make_balanced_bst(data, lo=0, hi=None, parent=None):
    """
    Turns a sorted list into a balanced binary search tree

    Args:
        data: the sorted list;
        lo: the beggining of the list; set to 0 by default;
        hi: the end of the list; set to None by default;
        porent: the parent node.
    """

    # Gets the beggining and end of the list.
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    # Determines the middle element of the list to be the root and be able to 
    # create a more balanced tree.
    mid = (lo + hi) // 2
    key, value = data[mid]

    # Creates the root node and uses recursion to deal with the two other halves
    # of the tree
    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    
    return root
