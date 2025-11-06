"""
inventory.py
by iridiumJester
The inventory where items are stored and edited.
"""

from item import Item 

class Inventory():
    def __init__(self):    
        self.items = {}

    def add_item(self, item: Item):
        if item.name in self.items.keys():
            current_number = self.items.get(item.name)
            self.items[item.name] = item.count + current_number
        else:
            self.items[item.name] = item.count


if __name__ == "__main__":
    apples = Item("Apples", 4)
    pantry = Inventory()
    pantry.add_item(apples)
    apples = Item("Apples", 8)
    pantry.add_item(apples)