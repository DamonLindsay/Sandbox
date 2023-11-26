"""
League of Legends XP Calculator
"""


def main():
    """"""
    pass


def calculate_xp_for_level(level):
    """"""
    # Base case: XP required for level 1 is 0
    if level == 1:
        return 0
    # Recursive case: XP for current level = XP for previous level + 100
    else:
        return calculate_xp_for_level(level - 1) + 100


main()
