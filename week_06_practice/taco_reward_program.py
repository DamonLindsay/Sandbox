"""Taco Reward Program"""


class User:
    def __init__(self, name, tacos=5, score=0):
        self.name = name
        self.tacos = tacos
        self.score = score

    def give_tacos(self, other_user, number_of_tacos):
        if self.tacos >= number_of_tacos:
            other_user.receive_tacos(number_of_tacos)
            self.tacos -= number_of_tacos
            self.score += number_of_tacos
            print(f"{self.name} gave {number_of_tacos} taco(s) to {other_user.name}.")
        else:
            print(f"Sorry, {self.name} doesn't have enough tacos to give.")

    def receive_tacos(self, number_of_tacos):
        self.tacos += number_of_tacos

    def __str__(self):
        return f"{self.name}, {self.score} points, {self.tacos} tacos left."


# Example usage:
if __name__ == '__main__':
    # Creating users.
    user1 = User("Ben")
    user2 = User("Alice")

    print(user1)  # Output: Ben, 0 points, 5 tacos left.
    print(user2)  # Output: Alice, 0 points, 5 tacos left.

    # User giving tacos to another user
    user1.give_tacos(user2, 2)
    print(user1)  # Output: Ben gave 2 taco(s) to Alice.
    print(user2)  # Output: Alice, 2 points, 7 tacos left.
