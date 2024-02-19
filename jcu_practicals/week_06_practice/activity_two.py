"""Activity Two"""
from jcu_practicals.week_06_practice.product import Product

products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]

on_sale_products = [product for product in products if product.is_on_sale]
print(on_sale_products)
