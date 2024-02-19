"""
Caesar Cipher
"""


def caesar_cipher(text, key, mode):
    """Encrypts or decrypts the given text using Caesar cipher."""
    result = ""
    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            shift = key if mode == "encrypt" else -key
            ascii_offset = ord("A") if char.isalpha() else ord("a")
            shifted_char = chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
            result += shifted_char
        else:
            result += char
    return result


def main():
    """Main function to interact with the user and perform Caesar cipher encryption/decryption """
    text = input("Enter the text to encrypt or decrypt: ")
    key = int(input("Enter the key (an integer from 1 to 25): "))
    mode = input("Enter 'encrypt' for encryption or 'decrypt' for decryption: ")

    if mode.lower() == "encrypt":
        result = caesar_cipher(text, key, "encrypt")
        print(f"Encrypted text: {result}")
    elif mode.lower() == "decrypt":
        result = caesar_cipher(text, key, "decrypt")
        print(f"Decrypted text: {result}")
    else:
        print("Invalid mode.  Please enter 'encrypt' or 'decrypt'.")


if __name__ == '__main__':
    main()
