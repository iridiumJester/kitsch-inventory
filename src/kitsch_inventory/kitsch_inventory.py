"""
kitsch_inventory.py
by iridiumJester
An organizational/tracking tool for your kitchen.
"""
import json
from inventory import Inventory

try:
    with open('src/kitsch_inventory/messages.json', 'r') as user_file:
        data = json.load(user_file)
except FileNotFoundError:
    print("Error: 'messages.json' not found.")
except json.JSONDecodeError:
    print("Error: Could not decode JSON from 'messages.json'. Check file format.")

def main():
    print(data.get("welcome"))
    option = 0
    while option != 4:
        print(data.get("menu"))
        print(data.get("main_menu_options"))
        option = int(input())
        if option == 1:
            # show options for input, said input
            print(data.get("add_menu_options"))
            add_option = int(input())

            # different paths for adding item or category
            if add_option == 1:
                # display categories to add items to
                print(data.get("category_menu_options"))
                category_count = len(Inventory.categories)
                for i in range (category_count):
                    print(f"    {i + 1} - {Inventory.categories[i]}")
                
                # get user input for category (accessed later)
                chosen_category = int(input())
                item_input = 0
                print(data.get("add_item_msg"))

                # add items loop
                while item_input != "end":
                    item_input = str(input())
                    # add item
        elif option == 2:
            # show options for input, said input
            print(data.get("edit_menu_options"))
            edit_option = int(input())

            # display categories
            category_count = len(Inventory.categories)
            print(data.get("category_menu_options"))
            for i in range (category_count):
                print(f"    {i + 1} - {Inventory.categories[i]}")
            chosen_category = int(input())

            """
            if edit_option = 1:
                # limit how many items can be printed at a time
                visible_items = 0

                GET item count for chosen_category
                
                if j < item_count and visible_items < 9
                    if visible_items == 0:
                        DISPLAY Page ? of ? for (chosen_category)
                    keep printing :))
                else
                    if j >= item_count:
                        end loop
                    if visible_items >= 9
                        prompt user to continue printing
                        reset visible_items to 0




                # aforementioned item limit
                while visible_items < 9:
                    # print categories items with a number
                    for j in range (item_count):
                        print(f"    {j + 1} - {(given categories items)[j]}")
                        visible_items += 1

                DISPLAY choose an item or use the arrow keys to change pages
            else:
                DISPLAY category edit options (rename, delete)
                GET user input
                IF user input = rename
                IF user input = delete
            """
        elif option == 3:
            # show options for input, said input
            print(data.get("view_menu_options"))
            view_option = int(input())

            # will be used to limit how many items will be printed at a time
            visible_items = 0

            # different paths for viewing all or category
            if view_option == 1:
                category_count = len(Inventory.categories)
                i = 0
                """
                WHILE i != (category_count)
                    GET category
                    PRINT categories items in a loop like the categories
                    GET item count for given category
                    for j in range (item_count):
                        print(f"    {(given categories items)[j]}")
                        visible_items += 1
                    i += 1
                """
            else:
                # display categories
                print(data.get("category_menu_options"))
                category_count = len(Inventory.categories)
                for i in range (category_count):
                    print(f"    {i + 1} - {Inventory.categories[i]}")
                chosen_category = int(input())

        elif option == 4:
            print(data.get("goodbye"))
            break
        else:
            print(data.get("input_error"))
    """
    >> DISPLAY start a new file or begin import. [ new/import ]
    >> IF option 1
        SET inventory as an empty list
    >> ELSE
        idk how to do this so ignore for now. thats what the arrows mean
    SET option to 0
    WHILE option != 4
        DISPLAY what would you like to do? [ add/edit/view/exit ]
        GET option from user
        IF option 1
            SET chosen_category to nada
            IF no categories
                GET category name from user
            ELSE
                DISPLAY categories
                GET category from user by its number in the list
            SET chosen_category
            SET input to nada
                WHILE input != end
                    add item
                END WHILE
            APPEND new items to chosen_category in inventory
        ELSE IF option 2
            DISPLAY [ item/category ]
            GET user input
                IF option 1 
                    DISPLAY categories in numbered list
                    GET user input
                    DISPLAY items in sets of 9
                    DISPLAY choose an item or use the arrow keys to change pages



                    then you give them a kabillion options
        ELSE IF option 3
            DISPLAY inventory
            this would print a little at a time so it would need user input for movement between pages
        ELSE IF option 4
            DISPLAY saving...
        ELSE
            DISPLAY not an option
        END IF
    END WHILE
    export data to a json or smtn somehow
    DISPLAY bye-bye!
    """


if __name__ == "__main__":
    main()
