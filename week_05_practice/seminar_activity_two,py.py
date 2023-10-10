"""
Seminar Activity Two
"""


def main():
    """ """
    strings = ["Hi", "Bye", "Lolly", "Rainbow"]
    string_to_strings_count = convert_list_to_dict(strings)
    print(string_to_strings_count)


def convert_list_to_dict(strings):
    """Convert list to a dictionary."""
    string_to_string_count = {}
    for string in strings:
        string_to_string_count[string] = len(string)
    return string_to_string_count


main()
