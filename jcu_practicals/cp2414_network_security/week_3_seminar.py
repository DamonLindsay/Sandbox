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


def _encrypt_password(password):
    """Encrypts a password using Caesar cipher."""
    shift = random.randint(1, 25)  # Random shift between 1 and 25
    encrypted_password = ""
    for char in password:
        if char.isalpha():
            shifted_char = chr((ord(char) + shift - 97) % 26 + 97) if char.islower() else chr(
                (ord(char) + shift - 65) % 26 + 65)
            encrypted_password += shifted_char
        else:
            encrypted_password += char
            return encrypted_password


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
        encrypted_password = _encrypt_password(password)
        self.users[username] = User(username, email, encrypted_password)
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
        input_hashed_password = _encrypt_password(password)
        if input_hashed_password == stored_password:
            print("Login successful!")
            return True
        else:
            print("Incorrect password.  Please try again.")
            return False


if __name__ == '__main__':
    main()
