"""
Dictionaries in Python are implemented using a data structure called hash table. 
A hash table uses a list/array to store the key-value pairs, and uses a hashing 
function to determine the index for storing or retrieving the data associated with 
a given key.

Your objective in this assignment is to implement a HashTable class which supports 
the following operations:

    1. Insert: Insert a new key-value pair;
    2. Find: Find the value associated with a key;
    3. Update: Update the value associated with a key;
    4. List: List all the keys stored in the hash table.

"""


class HashTable:
    def __init__(self, max_size=4096):
        self.data_list = [None] * max_size

    def get_index(self, key) -> int:
        """
        Hashing function.

        Args:
            key: the key from the key-value pair.
        """

        # Initializes a variable to store the result from the ord() function.
        result = 0

        # Uses the ord() function to convert the string into numbers.
        for character in str(key):
            number_from_character = ord(character)
            result += number_from_character

        # Uses the remainder of the result divided by length of the data list size 
        # to generate an index. 
        list_index = result % len(self.data_list)
        return list_index

    def insert(self, key, value):
        """
        Insert a new key-value pair.

        Args:
            key: the object associated with the key.
            value: the object associated with the value.
        """

        # Uses the hashing function to append the key-value pair to its designated 
        # index.
        index_for_key = self.get_index(key)

        # Prevents the user from using the same key.
        if self.data_list[index_for_key] is None:
            self.data_list[index_for_key] = (key, value)

    def find(self, key):
        """
        Find the value associated with a key.

        Args:
            key: the object associated with the key.
        """
        
        # Gets the index for the key.
        found_index = self.get_index(key)
        
        # Returns the key-value pair for the given index.
        if self.data_list[found_index] is not None:
            return self.data_list[found_index]
        
        return None

    def update(self, key, value):
        """
        Change the value associated with a key.

        Args:
            key:
            value:
        """

        # Gets the index for the particular key.
        index = self.get_index(key)

        # Ensures the key is not empty.
        if self.data_list[index] is not None:
            self.data_list[index] = (key, value)

        else:
            print("Unable to update key because it was empty")

    def list_all(self) -> list:
        """
        List all the keys.
        """
        
        return [kv[0] for kv in self.data_list if kv is not None]
