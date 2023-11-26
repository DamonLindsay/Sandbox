"""
League of Legends XP Calculator
"""


def main():
    """Main function to run the League of Legends XP Calculator program."""
    print("League of Legends XP Calculator")
    target_level = int(input("Enter the target level: "))

    if target_level <= 0:
        print("Please enter a valid target level greater than 0.")
    else:
        total_xp = calculate_xp_for_level(target_level)
        print(f"The total XP required to reach level {target_level} is {total_xp}.")


def calculate_xp_for_level(level):
    """Calculate the total XP required to reach the given level in League of Legends."""
    # Base case: XP required for level 1 is 0
    if level == 1:
        return 0
    # Recursive case: XP for current level = XP for previous level + 100
    else:
        return calculate_xp_for_level(level - 1) + 100


main()
