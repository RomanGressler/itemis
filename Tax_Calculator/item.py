import math

from itemtype import *


class Item:
    def __init__(self, name, item_type, price, imported, amount):
        self.name = name
        self.type = item_type
        self.price = price
        self.imported = imported
        self.amount = amount

    def calc_tax(self):
        """Calculate the tax of an item. Checks if the item is imported and in which tax group it is"""
        if self.type == ItemType.BOOK:
            tax = 0
        elif self.type == ItemType.MEDICAL:
            tax = 0
        elif self.type == ItemType.FOOD:
            tax = 0
        else:
            tax = 0.1
        if self.imported:
            tax += 0.05
        tax_rounded = self.round_tax(float(self.price) * float(tax))
        return tax_rounded * float(self.amount)

    def round_tax(self, value):
        return math.ceil(value / 0.05) * 0.05
