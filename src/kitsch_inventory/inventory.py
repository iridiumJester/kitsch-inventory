"""
inventory.py
by iridiumJester
The inventory where items are stored and edited.
"""
from item import Item

"""
inventory {
    category1 
    category2
}

category1 {
    item
}

category2 {
    item
}
"""


class Inventory():
    categories = [
        "Pantry", "Fridge", "Freezer"
    ]

    def __init__(self):    
        # Dictionary for items 
        self.category = ""
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
    # # Create category to create items
    # smiths = Inventory()

    # # Create items and add to inventory
    # apples = Item("Apples", 4)
    # smiths.add_item(apples)
    # apples = Item("Apples", 8)
    # smiths.add_item(apples)
    # print(Inventory.categories)

    pantry = ["Cereal bars", 2, "Spaghetti", 1]

    pantry_count = int(len(pantry) / 2)
    print(pantry_count)

    for i in range(0, len(pantry), 2):
        if i + 1 < len(pantry):
            print(f"{pantry[i]}: {pantry[i+1]}")
        else:
            print(pantry[i])
