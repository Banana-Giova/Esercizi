"""
3. E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
    Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
    Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
"""
import sys
sys.path.append('/home/banana/Desktop/Coding/Esercizi')
from Personal_Collection import int_inputter

products_list:dict = {
}
def product_maker(name:str, price:float, quantity:int
                    ) -> dict[str: list[float, int]]:
    products_list[name] = [price, quantity]
    return products_list

shopping_cart:dict = {
}
def cart_program(products:dict):
    print("""Welcome to your shopping cart, what do you need?
Type 'Add' to add an item.
Type 'Remove' to remove an item.
Type 'View' to view the items currently in your cart and the total.
Type 'Exit' to close your shopping cart.""")
    
    while True:
        user_choice:str = (input("Type in a command -> ")).casefold()
        
        if user_choice == "add":
            for ki, vi in products_list.items():
                print("Item loading...")
                print(f"Products Name: {ki}, Price: {vi[0]}$, Quantity: {vi[1]}")
                
                choice:str = (input(f"Input 'Y' to add {ki} to your cart.")).capitalize()
                if choice == "Y":
                    print("Input quantity to add.")
                    how_many:int = int_inputter()
                    if (vi[1] - how_many) >= 0:
                        if vi[1] > 0 and ki not in shopping_cart:
                            shopping_cart[ki] = [vi[0], how_many]
                            vi[1] -= how_many
                            print("The item(s) was added successfully.")
                        elif ki in shopping_cart:
                            shopping_cart[ki][1] += how_many
                            vi[1] -= how_many
                            print("The item(s) was added successfully.")
                        elif vi[1] == 0:
                            print("The store ran out of this product!")
                    else:
                        print("Invalid quantity.")
            print("Main menu loading...")
        
        elif user_choice == "remove":
            if len(shopping_cart) > 0:
                for ki, vi in shopping_cart.items():
                    print("Item loading...")
                    print(f"Products Name: {ki}, Price: {vi[0]}$, Quantity: {vi[1]}")
                    
                    choice:str = (input(f"Input 'Y' to remove {ki} from your cart.")).capitalize()
                    if choice == "Y":    
                        print("Input quantity to remove.")
                        how_many:int = int_inputter()
                        if (vi[1] - how_many) >= 0:  
                            if choice == "Y":
                                vi[1] -= how_many
                                products_list[ki][1] -= how_many
                                print("The item(s) was removed successfully.")
                            elif len(shopping_cart) == 0:
                                print("You can't remove items from your cart, it's empty!")
                        else:
                            print("Invalid quantity.")
            else:
                print("You can't remove items from your cart, it's empty!")
            print("Main menu loading...")

        elif user_choice == "view":
            total:float = 0.0
            for ki, vi in shopping_cart.items():
                print(f"Products Name: {ki}, Price: {vi[0]}$, Quantity: {vi[1]}")
                total += vi[0]
            discount:str = input("Do you have a discount? If you do type it here ->")
            if discount == "Totti":
                print("Discount accepted!")
                total *= 0.9
            else:
                print("Invalid discount or none input given.")
            print(f"Your total is {round((total*1.1), 2)}$, taxes included")
            print("Main menu loading...")
        
        elif user_choice == "exit":
            print("Goodbye!")
            break

        else:
            print("Error, invalid choice.")

        if len(shopping_cart) > 0:
            for ki in products_list:
                if ki in shopping_cart:
                    if shopping_cart[ki][1] == 0:
                        del shopping_cart[ki]



product_maker("Banana", 1.2, 5)
product_maker("Tomato", 0.2, 10)
product_maker("Apple", 0.45, 8)
product_maker("Peach", 0.6, 8)
product_maker("Walnuts", 0.05, 20)
product_maker("Dark Cholocate", 1.9, 3)
product_maker("Milk Cholocate", 1.5, 3)
product_maker("Loaf of Bread", 1.5, 5)
product_maker("Water Bottle", 0.5, 18)
product_maker("Cola Can", 0.8, 8)
product_maker("Honey Mustard", 3.0, 1)

cart_program(products_list)