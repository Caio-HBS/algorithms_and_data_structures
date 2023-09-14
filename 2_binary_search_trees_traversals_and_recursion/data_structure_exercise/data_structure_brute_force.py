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


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(username={self.username}, name={self.name}, email={self.email})"

    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        """
        Loops through the list until it finds the correct place to store the new
        user by simply comparing the strings.

        Args:
            user: new user object.
        """
        index = 0

        while index < len(self.users):
            if self.users[index].username > user.username:
                break
            index += 1
        self.users.insert(index, user)

    def retrieve(self, username):
        """
        Loops through the list until it finds the desired user by its username.

        Args:
            username: the desired username.
        """
        for user in self.users:
            if user.username == username:
                return user
            return "ERROR: username not found"

    def update(self, user):
        """
        Uses the retrieve method to find the desired user and updates the new
        information.

        Args:
            user: the user to be updated.
        """
        found_target = self.retrieve(user)
        found_target.name, found_target.email = user.name, user.email

    def list_all(self):
        """
        Displays the full list of users in alphabetical order.
        """
        return print(self.users)


database = UserDatabase()
list_of_users = [
    User("aline", "Aline Ramos", "aline@example.com"),
    User("beatriz", "Beatriz da Silva", "beatriz@example.com"),
    User("henrique", "Henrique Jânio", "henrique@example.com"),
    User("joao", "João Verma", "joao@example.com"),
    User("silas", "Silas Soares", "silas@example.com"),
    User("sona", "Sona Kumar", "sona@example.com"),
    User("victor", "Victor Goethe", "victor@example.com"),
]

for user in list_of_users:
    database.insert(user)

database.list_all()
