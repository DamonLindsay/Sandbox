def main():
    password_minimum_length = 5

    password = input("Enter a password: ")
    while len(password) < password_minimum_length:
        print("Invalid password.")
        password = input("Enter a password: ")

    for character in range(len(password)):
        print("*", end="")


main()
