"""
Activity: Hashed Password
"""

import hashlib
import random
import string


def main():
    """THe main function."""
    auth_system = AuthenticationSystem()

    # Registering a user
    auth_system.register_user("john_doe", "john@example.com", "P@ssw0rd")

    # Generating a random password
    random_password = generate_random_password()
    print(f"Generated Password: {random_password}")

    # Checking password strength
    password_strength = check_password_strength("StrongP@ssw0rd")
    print("Password Strength:", "Strong" if password_strength else "Weak")

    # Logging in
    auth_system.login("john_doe", "P@ssw0rd")


class User:
    """Represents a user with a username, email, and password."""

    def __init__(self, username, email, password):
        """Initializes a User object."""
        self.username = username
        self.email = email
        self.password = password


def _hash_password(password):
    """Hashes a password using SHA-256 with a random salt."""
    salt = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    return hashlib.sha256((password + salt).encode()).hexdigest() + ":" + salt


def generate_random_password():
    """Generates a random password with 12 characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(12))


def check_password_strength(password):
    """Checks the strength of a password based on certain criteria."""
    if len(password) < 8:
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True


class AuthenticationSystem:
    """Handles user registration, password management, and authentication."""

    def __init__(self):
        """Initializes an AuthenticationSystem object."""
        self.users = {}
        self.password_file = "passwords.txt"

    def register_user(self, username, email, password):
        """Registers a new user."""
        if username in self.users:
            print("Username already exists.  Please choose another one.")
            return
        hashed_password = _hash_password(password)
        self.users[username] = User(username, email, hashed_password)
        self._save_passwords()

    def _save_passwords(self):
        """Saves the hashed passwords to a file."""
        with open(self.password_file, "w") as output_file:
            for username, user in self.users.items():
                output_file.write(f"{username}:{user.password}")

    def login(self, username, password):
        """Logs in a user by verifying the provided username and password."""
        if username not in self.users:
            print("User does not exist.")
            return False
        stored_password = self.users[username].password
        hashed_input_password, salt = stored_password.split(":")
        input_hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
        if input_hashed_password == hashed_input_password:
            print("Login successful!")
            return True
        else:
            print("Incorrect password.  Please try again.")
            return False


if __name__ == '__main__':
    main()
