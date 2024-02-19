import decimal
import math


def calculate_e(n):
    """Calculate Euler's number (e) to the specified number of decimal places."""
    decimal.getcontext().prec = n + 2  # Set the precision to n+2 to ensure accuracy
    e = sum(decimal.Decimal(1) / math.factorial(i) for i in range(n))
    return e


def main():
    """Main function to interact with the user and calculate e."""
    while True:
        try:
            digits = int(input("Enter the number of digits to calculate e (limit is around 1000): "))
            if digits <= 0:
                print("Please enter a positive integer.")
                continue
            elif digits > 1000:
                print("The limit for the number of digits is around 1000.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input.  Please enter a valid integer.")

    calculated_e = calculate_e(digits)
    rounded_e = round(calculated_e, digits)  # Round to the specified number of decimals
    print(f"e to {digits} decimal places is: {rounded_e}")


if __name__ == '__main__':
    main()
