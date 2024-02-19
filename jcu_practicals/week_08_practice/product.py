"""Product class module"""
import json


class Product:
    def __init__(self, name="", price=0.0):
        """Initialize the Product object."""
        self.name = name
        self.price = price


class ProductCollection:
    def __init__(self):
        """Initialize the Product Collection object."""
        self.products = []

    def load_products(self, filename):
        """Load the products from the specified file and append them to a list."""
        try:
            with open(filename) as input_file:
                data = json.load(input_file)
                for item in data:
                    product = Product(item["name"], item["price"])
                    self.products.append(product)
        except FileNotFoundError as e:
            print(f"File not found: {filename}.  Error: {e}.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON in file: {filename}. Error: {e}.")
        except Exception as e:
            print(f"An error occurred while loading products from {filename}. Error: {e}.")

    def get_products(self):
        """Return the list of products."""
        return self.products
