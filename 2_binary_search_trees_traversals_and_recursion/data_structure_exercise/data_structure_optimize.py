"""
PROBLEM 1:

As a senior backend engineer at Jovian, you are tasked with developing a fast 
in-memory data structure to manage profile information (username, name and email) 
for 100 million users. It should allow the following operations to be performed 
efficiently:
    
    - Insert the profile information for a new user;
    - Find the profile information of a user, given their username;
    - Update the profile information of a user, given their username;
    - List all the users of the platform, sorted by username.

You can assume that usernames are unique.
"""


class UserDatabase:
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
            node = UserDatabase(key, value)

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