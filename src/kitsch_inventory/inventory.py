"""
inventory.py
by iridiumJester
The inventory where items are stored and edited.
"""
from item import Item 

class Inventory():
    def __init__(self):    
        # Dictionary for items
        self.items = {}

    def add_item(self, item: Item):
        if item.name in self.items.keys():
            # current_number = self.items.get(item.name)
            # self.items[item.name] = item.count + current_number
            """
            if current item name is equal to another item
                add current item count to said item
                delete current item
            """
            pass
        else:
            self.items[item.name] = item.count


if __name__ == "__main__":
    # Create category to create items
    pantry = Inventory()

    # Create items and add to inventory
    apples = Item("Apples", 4)
    pantry.add_item(apples)
    apples = Item("Apples", 8)
    pantry.add_item(apples)