"""
kitsch_inventory.py
by iridiumJester
"""
from produce import Produce


def main():
    print("Welcome to Kitsch-Inventory.")

    # its objects wowww
    lettuce = Produce("Lettuce", 1)
    print(lettuce)
    carrot = Produce("Carrot", 5)
    print(carrot)


if __name__ == "__main__":
    main()