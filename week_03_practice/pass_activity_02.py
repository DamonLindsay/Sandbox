"""
Write a program that calculates which of two products is cheaper based on a quantity and price.
The first function will take 2 parameters - a product price and quantity. It should calculate and return the
total price of the product.
The second function will take 2 parameters - the total price of product 1 and the total price of product 2
and return which product is cheaper.
The program will then print either "Product 1" or "Product 2" if the respective product is cheaper.
Ignore the case where the products are the same price.
"""


def main():
    """This program will calculate two different product quantities and totals and then compare the two values."""
    price_of_product_one = 10.00
    quantity_of_product_one = 3

    price_of_product_two = 20.00
    quantity_of_product_two = 2

    product_one_total = calculate_total_price(price_of_product_one, quantity_of_product_one)
    product_two_total = calculate_total_price(price_of_product_two, quantity_of_product_two)

    cheaper_option = determine_cheapest_choice(product_one_total, product_two_total)
    print(cheaper_option)


def calculate_total_price(price, quantity):
    """Calculate the total price."""
    return price * quantity


def determine_cheapest_choice(first_total, second_total):
    """Compare two values and return the cheapest."""
    if first_total < second_total:
        return "Product One"
    elif second_total < first_total:
        return "Product Two"
    else:
        return "Both products are the same price."


main()
