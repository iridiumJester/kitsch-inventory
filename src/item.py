"""
item.py
by iridiumJester
Class for list items.
"""

class Item():
    count = 0
    def __init__(self, name, count):
        self.name = name
        self.count = count


if __name__ == "__main__":
    print(Item.count)
