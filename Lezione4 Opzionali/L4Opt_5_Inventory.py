"""
5. Inventory Management System:

    Create a function that defines an item with a code, name, price and quantity.
    Create a database or dictionary to store the items in inventory.
    Implement functions to add, remove, search, and update items in the inventory.
    Use for loops and conditional statements to manage the various inventory operations.
"""

import sys
sys.path.append('/home/banana/Desktop/Coding/Esercizi')
from Personal_Collection import int_inputter

items_list:dict = {
}
def items_maker(code:str, name:str, price:float, quantity:int
                    ) -> dict[str: list[str, float, int]]:
    items_list[code] = [name, price, quantity]
    return items_list

inventory:dict = {
}
def inventory_program(all_items:dict):
    print("""Welcome to your shopping inventory, what do you need?
Type 'Add' to add an item to your inventory.
Type 'Remove' to remove an item from your inventory.
Type 'Search' to search for an item currently in your inventory.
Type 'Update' to update the info of an item from your inventory.
Type 'Exit' to close your inventory manager.""")
    
    while True:
        user_choice:str = (input("Type in a command -> ")).casefold()
        
        if user_choice == "add":
            for ki, vi in items_list.items():
                print("Item loading...")
                print(f"Item Code: {ki}, Name: {vi[0]}, Price: {vi[1]}$, Quantity: {vi[2]}")
                
                choice:str = (input(f"Input 'Y' to add {ki} to your inventory.")).capitalize()
                if choice == "Y":
                    print("Input quantity to add.")
                    how_many:int = int_inputter()
                    if (vi[2] - how_many) >= 0:
                        if vi[2] > 0 and ki not in inventory:
                            inventory[ki] = [vi[0], vi[1], how_many]
                            vi[2] -= how_many
                            print("The item(s) was added successfully.")
                        elif ki in inventory:
                            inventory[ki][1] += how_many
                            vi[2] -= how_many
                            print("The item(s) was added successfully.")
                        elif vi[2] == 0:
                            print("Your warehouse ran out of this product!")
                    else:
                        print("Invalid quantity.")
            print("Main menu loading...")
        
        elif user_choice == "remove":
            if len(inventory) > 0:
                for ki, vi in inventory.items():
                    print("Item loading...")
                    print(f"Item Code: {ki}, Name: {vi[0]}, Price: {vi[1]}$, Quantity: {vi[2]}")
                    
                    choice:str = (input(f"Input 'Y' to remove {ki} from your inventory.")).capitalize()
                    if choice == "Y":    
                        print("Input quantity to remove.")
                        how_many:int = int_inputter()
                        if (vi[2] - how_many) >= 0:  
                            if choice == "Y":
                                vi[2] -= how_many
                                items_list[ki][1] -= how_many
                                print("The item(s) was removed successfully.")
                            elif len(inventory) == 0:
                                print("You can't remove items from your inventory, it's empty!")
                        else:
                            print("Invalid quantity.")
            else:
                print("You can't remove items from your inventory, it's empty!")
            print("Main menu loading...")
        
        elif user_choice == "search":
            choice:str = input("""What item do you want to search?
Input the code of the item -> """)
            if choice in inventory:
                print(f"""Item found! 
Here's the info of the item -> {inventory[choice]}""")
            else:
                print("Error, invalid code or item absent.")
        
        elif user_choice == "update":
            choice:str = input("""What item do you want to update?
Input the code of the item -> """)
            if choice in inventory:
                up_choice:str = (input("""What do you want to update?
Input 'Name' or 'Price' -> """)).casefold()
                if up_choice == "name":
                    new_choice:str = input("Input the new name -> ")
                    inventory[choice][0] = new_choice
                if up_choice == "price":
                    new_choice:str = input("Input the new price -> ")
                    inventory[choice][2] = new_choice

            else:
                print("Error, invalid code or item absent.")

        elif user_choice == "exit":
            print("Goodbye!")
            break

        else:
            print("Error, invalid choice.")

        if len(inventory) > 0:
            for ki in items_list:
                if ki in inventory:
                    if inventory[ki][2] == 0:
                        del inventory[ki]

items_maker("IP234J2H", "Banana", 1.2, 5)
items_maker("9UYF289D", "Tomato", 0.2, 10)
items_maker("CD2FWMW9", "Apple", 0.45, 8)
items_maker("H892FN2J", "Peach", 0.6, 8)
items_maker("MN3S2XC0", "Walnuts", 0.05, 20)
items_maker("34GAW4FG", "Dark Chocolate", 1.9, 3)
items_maker("23GAFGH6", "Milk Chocolate", 1.5, 3)
items_maker("ASGXB63V", "Loaf of Bread", 1.5, 5)
items_maker("XZB6SG4G", "Water Bottle", 0.5, 18)
items_maker("JMFDJ56X", "Cola Can", 0.8, 8)
items_maker("HER5ZGEW", "Honey Mustard", 3.0, 1)
inventory_program(items_list)