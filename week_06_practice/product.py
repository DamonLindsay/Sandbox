"""Product"""


class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        if self.is_on_sale:
            on_sale_string = "(on sale)"
        else:
            on_sale_string = ""

        return f"{self.name}, ${self.price:.2f} {on_sale_string}"

    def __repr__(self):
        return str(self)

    def put_on_sale(self, discount_percentage):
        """Put product on sale by discount_percentage as decimal (e.g. 0.2 is 20% off)."""
        self.price *= (1 - discount_percentage)
        self.is_on_sale = True


p = Product("Phone", 340, False)
print(p.name, "...")
print(p)
p.put_on_sale(0.1)
print(p)

products = [Product("Phone", 340, False), Product("PC", 1420.95, True),
            Product("Plant", 24.5, True)]

on_sale_products = [product for product in products if product.is_on_sale]
