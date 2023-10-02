"""
Strings - Seminar Activity
"""

# Given a string called text, like: text = "This is a sentence"
# Write a list comprehension that produces a list of the words that have > 3 characters.
# Example: print(long_words)
# Should output: ['This', 'sentence']
MINIMUM_WORD_LENGTH = 3


def main():
    """This program will write a list comprehension that produces a list of the words
    that have > LONG_WORD_MINIMUM characters."""

    text = "This is a sentence"
    long_words = find_long_words(text)
    print(long_words)


def find_long_words(text):
    """Find and return a list of words from the given text that has more than {MINIMUM_WORD_LENGTH} characters."""
    words = text.split()
    long_words = [word for word in words if len(word) > MINIMUM_WORD_LENGTH]
    return long_words


main()
