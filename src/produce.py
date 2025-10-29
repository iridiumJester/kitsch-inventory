"""
produce.py
by iridiumJester
Produce object based on the Item.
"""
from item import Item

class Produce(Item):
    def __init__(self, name, count):
        super().__init__()

        # Add to count of LIST items. 
        Item.count += 1

        # Inst attributes
        self.name = name
        self.count = count

    def __str__(self):
        repr = "\n"
        repr += f"Name | Count\n"
        repr += f"{self.name}, {self.count}"
        return repr
    
if __name__ == "__main__":
    # Add some produce
    lettuce = Produce("Lettuce", 1)
    carrot = Produce("Carrot", 5)

    # Print the information girl
    print(lettuce)
    print(carrot)