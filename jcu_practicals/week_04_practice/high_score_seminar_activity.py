"""
High Score - Seminar Activity
"""
from operator import itemgetter


def main():
    """This program will ask the user for a new name and score in one input,
    then add those to the list, then sort it."""
    score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]

    new_name_and_score = get_valid_name_and_score()
    add_new_name_and_score(new_name_and_score, score_pairs)
    score_pairs.sort(key=itemgetter(1))

    print(score_pairs)


def add_new_name_and_score(name_and_score, name_and_scores):
    """Add a name and corresponding score to a list."""
    name = name_and_score[0]
    score = int(name_and_score[1])
    name_and_scores.append([name, score])


def get_valid_name_and_score():
    """Get a valid name and score from the user."""
    new_name_and_score = input("Enter new name and score, formatted like so (Damon 2): ").split()
    while len(new_name_and_score) != 2:
        print("Invalid format.")
        new_name_and_score = input("Enter new name and score, formatted like so (Damon 2): ").split()
    return new_name_and_score


main()
