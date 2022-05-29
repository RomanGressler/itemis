import unittest
from item import *


class ItemTestCase(unittest.TestCase):
    def test_tax_calculator(self):
        game = Item("Game", Item_type.DEFAULT, 10, False, 2)
        med = Item("Med", Item_type.MEDICAL, 100, False, 1)
        apple = Item("Apple", Item_type.FOOD, 1, False, 1)
        book = Item("Book", Item_type.BOOK, 1, False, 1)
        imported_book = Item("Imported Book", Item_type.BOOK, 1, True, 1)
        self.assertEqual(game.calc_tax(), 2)
        self.assertEqual(med.calc_tax(), 0)
        self.assertEqual(apple.calc_tax(), 0)
        self.assertEqual(book.calc_tax(), 0)
        self.assertEqual(imported_book.calc_tax(), 0.05)


if __name__ == '__main__':
    unittest.main()
