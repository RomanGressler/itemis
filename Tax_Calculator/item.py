from item_type import *


class Item:
    def __init__(self, name, item_type, price, imported, amount):
        self.name = name
        self.type = item_type
        self.price = price
        self.imported = imported
        self.amount = amount

    def calc_tax(self):
        """Calculate the tax of an item. Checks if the item is imported and in which tax group it is"""
        if self.type == Item_type.BOOK:
            tax = 0
        elif self.type == Item_type.MEDICAL:
            tax = 0
        elif self.type == Item_type.FOOD:
            tax = 0
        else:
            tax = 0.1
        if self.imported:
            tax += 0.05
        return self.price * tax * self.amount
