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
        with open(filename) as input_file:
            data = json.load(input_file)
            for item in data:
                product = Product(item["name"], item["price"])
                self.products.append(product)

    def get_products(self):
        """Return the list of products."""
        return self.products
