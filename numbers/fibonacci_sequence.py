"""
Fibonacci Sequence
"""


def generate_fibonacci(n):
    """Generate the Fibonacci sequence up to the specified number or to the Nth number."""
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence


def main():
    """Main function to interact with the user and generate the Fibonacci sequence."""
    while True:
        try:
            n = int(input("Enter a number to generate the Fibonacci sequence up to: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input.  Please enter a valid integer.")

    fibonacci_sequence = generate_fibonacci(n)
    print(f"The Fibonacci sequence is: {fibonacci_sequence}")


if __name__ == '__main__':
    main()
