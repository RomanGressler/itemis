from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from item import *


class TaxCalculator(App):
    def build(self):
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
        dropdown = DropDown()
        basic = Label()

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
        self.item = Label(
            text=self.item_name.text,
            size_hint=(1, 0.1),
        )
        self.window.add_widget(self.item)
        self.item = Label(
            text="1.0€",
            size_hint=(1, 0.1),
        )
        self.window.add_widget(self.item)

    def submit_items(self):
        return


# run Say Hello App Calss
if __name__ == "__main__":
    TaxCalculator().run()
