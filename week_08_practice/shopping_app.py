"""
Shopping App
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from product import ProductCollection


class ShoppingApp(App):
    """"""

    def __init__(self, **kwargs):
        """"""
        super(ShoppingApp, self).__init__(**kwargs)

        self.title = "Shopping App"

        self.product_collection = ProductCollection()
        self.product_collection.load_products("products.json")

        self.total_price = 0
        self.total_label = Label(text="Total: $0")

    def build(self):
        """"""
        layout = BoxLayout(orientation="vertical")

        for product in self.product_collection.get_products():
            button = Button(text=f"{product.name} - ${product.price}")
            button.bind(on_press=lambda instance, p=product: self.add_to_total(p.price))
            layout.add_widget(button)

        bottom_row = BoxLayout(orientation="horizontal")

        clear_button = Button(text="Clear Total")
        clear_button.bind(on_press=self.clear_total)

        bottom_row.add_widget(self.total_label)
        bottom_row.add_widget(clear_button)

        layout.add_widget(bottom_row)

        return layout

    def add_to_total(self, price):
        """Add the price to the total price."""
        self.total_price += price
        self.total_label.text = f"Total: ${self.total_price:.2f}"

    def clear_total(self, instance):
        """Clear the current total and reset to 0"""
        self.total_price = 0
        self.total_label.text = "Total: $0.00"


if __name__ == '__main__':
    ShoppingApp().run()
