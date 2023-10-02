"""
Strings - Seminar Activity
"""


# Given a string called text, like: text = "This is a sentence"
# Write a list comprehension that produces a list of the words that have > 3 characters.
# Example: print(long_words)
# Should output: ['This', 'sentence']

def main():
    """This program will write a list comprehension that produces a list of the words that have > 3 characters."""
    text = "This is a sentence"

    long_words = text.split()
    print(long_words)


main()
