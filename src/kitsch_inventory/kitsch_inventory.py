"""
kitsch_inventory.py
by iridiumJester
An organizational/tracking tool for your kitchen.
"""
import json

try:
    with open('src/kitsch_inventory/messages.json', 'r') as user_file:
        data = json.load(user_file)
except FileNotFoundError:
    print("Error: 'messages.json' not found.")
except json.JSONDecodeError:
    print("Error: Could not decode JSON from 'messages.json'. Check file format.")

def main():
    print(data.get("welcome"))
    print(data.get("welcome_cont"))
    option = 0
    while option != 4:
        print(data.get("main_menu_options"))
        option = input()
        if option == 1:
            print(data.get("add_menu_options"))
            chosen_category = 0
            """
            GET categories
            IF no categories exist
                GET category name from user
            ELSE
                DISPLAY categories
                GET category from user by its number in the list
            SET chosen_category
            """
        elif option == 4:
            print(data.get("goodbye"))
            break
        else:
            print("whuh?")
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
