"""Taco BATTLE Program"""
from taco_reward_program import User


class Team:
    """A class representing a team in the Taco BATTLE program."""

    def __init__(self):
        self.users = []

    def add(self, user):
        """Add a user to the team."""
        self.users.append(user)

    def delete(self, user):
        """Delete a user from the team."""
        if user in self.users:
            self.users.remove(user)
        else:
            print(f"{user.name} is not in the team.")

    def get(self, index):
        """Get a user from the team by index."""
        if 0 <= index < len(self.users):
            return self.users[index]
        else:
            return None

    def get_leader(self):
        """Get the user with the highest score as the team leader."""
        if not self.users:
            return None
        return max(self.users, key=lambda x: x.score)

    def get_total_tacos_to_give(self):
        """Get the total number of tacos the team can give collectively."""
        return sum(user.tacos for user in self.users)

    def get_total_score(self):
        """Get the total score of the team."""
        return sum(user.score for user in self.users)


# Example usage:
if __name__ == '__main__':
    # Creating users.
    user1 = User("Ben")
    user2 = User("Alice")
    user3 = User("Charlie")
