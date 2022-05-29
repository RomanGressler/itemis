import unittest

from item import *


class ItemTestCase(unittest.TestCase):
    def test_tax_calculator(self):
        game = Item("Game", ItemType.DEFAULT, 10, False, 2)
        med = Item("Med", ItemType.MEDICAL, 100, False, 1)
        apple = Item("Apple", ItemType.FOOD, 1, False, 1)
        book = Item("Book", ItemType.BOOK, 1, False, 1)
        imported_book = Item("Imported Book", ItemType.BOOK, 1, True, 1)
        self.assertEqual(game.calc_tax(), 2)
        self.assertEqual(med.calc_tax(), 0)
        self.assertEqual(apple.calc_tax(), 0)
        self.assertEqual(book.calc_tax(), 0)
        self.assertEqual(imported_book.calc_tax(), 0.05)

    def test_tax_rounding(self):
        bottle = Item("imported bottle of perfume", ItemType.DEFAULT, 47.5, True, 1)
        self.assertEqual(bottle.round_tax(bottle.price * 0.15), 7.15)
        bottle2 = Item("imported bottle of perfume", ItemType.DEFAULT, 27.99, True, 1)
        self.assertEqual(bottle2.round_tax(bottle2.price * 0.15), 4.2)


if __name__ == '__main__':
    unittest.main()
