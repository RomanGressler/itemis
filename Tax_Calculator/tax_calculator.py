from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from item import *


class TaxCalculator(App):
    def build(self):
        self.items = []
        # returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 2

        # Item name
        item_name_label = Label(
            text="Item:",
            size_hint=(1, 0.1)
        )
        self.window.add_widget(item_name_label)
        self.item_name = TextInput(
            multiline=False,
            size_hint=(1, 0.1)
        )
        self.window.add_widget(self.item_name)

        # Item price
        item_price_label = Label(
            text="Price:",
            size_hint=(1, 0.1)
        )
        self.window.add_widget(item_price_label)
        self.item_price = TextInput(
            multiline=False,
            size_hint=(1, 0.1)
        )
        self.window.add_widget(self.item_price)

        # Amount
        item_amount_label = Label(
            text="Amount:",
            size_hint=(1, 0.1)
        )
        self.window.add_widget(item_amount_label)
        self.item_amount = TextInput(
            multiline=False,
            size_hint=(1, 0.1)
        )
        self.window.add_widget(self.item_amount)

        # Imported
        imported_label = Label(
            text="Imported:",
            size_hint=(1, 0.1)
        )
        self.window.add_widget(imported_label)
        self.imported = CheckBox(size_hint=(1, 0.1))
        self.window.add_widget(self.imported)

        # Category
        item_type_label = Label(
            text="Item Type:",
            size_hint=(1, 0.1)
        )
        self.window.add_widget(item_type_label)
        dropdown = DropDown()
        # adding all possible types to dropdown
        for name in ItemType:
            button = Button(
                text=name.name,
                size_hint_y=None,
                height=44
            )
            button.bind(on_release=lambda button: dropdown.select(button.text))
            dropdown.add_widget(button)

        self.select_button = Button(
            text="Select",
            size_hint=(1, 0.1),
            on_release=dropdown.open
        )
        self.select_button.bind(on_release=dropdown.open)
        # setting the button text to selected type
        dropdown.bind(on_select=lambda instance, x: setattr(self.select_button, 'text', x))
        self.window.add_widget(self.select_button)

        add_button = Button(
            text="ADD",
            size_hint=(1, 0.1),
        )
        add_button.bind(on_press=self.add_item)
        self.window.add_widget(add_button)

        submit_button = Button(
            text="SUBMIT",
            size_hint=(1, 0.1),
        )
        submit_button.bind(on_press=self.submit_items)
        self.window.add_widget(submit_button)

        header1 = Label(
            text="Items",
            size_hint=(1, 0.3),
        )
        self.window.add_widget(header1)

        header2 = Label(
            text="Price",
            size_hint=(1, 0.3),
        )
        self.window.add_widget(header2)

        return self.window

    def add_item(self, instance):
        """adds an item in the gui"""
        item = Item(
            self.item_name.text,
            self.convert_back_to_enum(self.select_button.text),
            self.item_price.text,
            self.imported.active,
            self.item_amount.text)
        self.items.append(item)
        # check if item is imported
        imported = ""
        if (item.imported):
            imported = "imported "

        self.item = Label(
            text=item.amount + " " + imported + item.name + ":",
            size_hint=(1, 0.1),
        )
        self.window.add_widget(self.item)
        self.item = Label(
            text=self.calculate_price(item),
            size_hint=(1, 0.1),
        )
        self.window.add_widget(self.item)

    def submit_items(self, instance):
        """shows the final tax and amount in the gui"""
        tax_label = Label(
            text="Sales Taxes:",
            size_hint=(1, 0.1),
        )
        self.window.add_widget(tax_label)
        tax_amount = Label(
            text=" " + self.calculate_total_tax(),
            size_hint=(1, 0.1),
        )
        self.window.add_widget(tax_amount)
        total_label = Label(
            text="Total:",
            size_hint=(1, 0.1),
        )
        self.window.add_widget(total_label)
        total_amount = Label(
            text=self.calculate_total_amount(),
            size_hint=(1, 0.1),
        )
        self.window.add_widget(total_amount)

    def calculate_total_tax(self):
        """calculates the total tax of all added items"""
        tax = 0
        for item in self.items:
            tax += item.calc_tax() * float(item.amount)
        return str("{:.2f}".format(tax))

    def calculate_total_amount(self):
        """calculates the total price of all added items"""
        total = 0
        for item in self.items:
            total += float(item.price) * float(item.amount)
            total += float(item.calc_tax()) * float(item.amount)
        return str("{:.2f}".format(total))

    def calculate_price(self, item):
        """calculates the price of a single item"""
        result = float(item.price) * float(item.amount)
        result += float(item.calc_tax()) * float(item.amount)
        return str("{:.2f}".format(result))

    def convert_back_to_enum(self, enum):
        """converts the text value of the dropdown menu back to an enum"""
        if enum == "BOOK":
            return ItemType.BOOK
        if enum == "DEFAULT":
            return ItemType.DEFAULT
        if enum == "MEDICAL":
            return ItemType.MEDICAL
        if enum == "FOOD":
            return ItemType.FOOD


# run tax calculator
if __name__ == "__main__":
    TaxCalculator().run()
