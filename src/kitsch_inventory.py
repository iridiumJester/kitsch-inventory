"""
kitsch_inventory.py
by iridiumJester
An organizational/tracking tool for your kitchen.
"""

def main():
    print("Welcome to Kitsch-Inventory.")
    """
    DISPLAY additional instructions
    DISPLAY start a new file or begin import. [ new/import ]
    IF option 1
        SET inventory as an empty list
    ELSE
        idk how to do that yet so ignore for now
    SET option to 0
    WHILE option != 4
        DISPLAY what would you like to do? [ add/edit/view/save and exit ]
        GET option from user
        IF option 1
            IF no categories
                GET category name from user
            ELSE
                DISPLAY categories
                GET category from user by its number in the list
            add item
        ELSE IF option 2
            DISPLAY [ item/category ]
            GET user input
            then you give them a kabillion options
        ELSE IF option 3
            DISPLAY inventory
            this would print a little at a time so it would need user input for movement between pages
        ELSE IF option 4
            DISPLAY saving and exiting...
        ELSE
            DISPLAY not an option
        END IF
    END WHILE
    export data to a json or smtn somehow
    DISPLAY bye-bye!
    """


if __name__ == "__main__":
    main()
