"""
6. Password Generator:

    Create a function that generates a random password with a specified length 
    and desired character types (lowercase letters, uppercase letters, numbers, symbols).
    Allow the user to specify the password length and desired character types.
    Generate and return a random password that meets the user's criteria.
"""

import random
import sys
sys.path.append('/home/banana/Desktop/Coding/Esercizi')
from Personal_Collection import int_inputter

low_alphabet:list = list(map(chr, range(ord('a'), ord('z')+1)))
upp_alphabet:list = []
for i in low_alphabet:
        upp_alphabet.append(i.capitalize())
numbers_list:list[int] = [i + 1 for i in range(10)]
symbols_list:list[str] = ["!","(", ")", "-", "[", "]", "{", "}", ";", ":",
                          "<", ">" , ".", "?", "@", "#", "$", "%", "^",
                          "&", "*", "_", "~"]


def password_generator() -> str:
    print("Welcome to the Password Generator!\n"\
          "Input the lenght that your new password will have!")
    pass_lenght:int = int_inputter()
    print("Great! Now input your desired character types.\n"\
          "You can choose between:\n"
          "lowercase letters, uppercase letters, numbers, symbols!")
    
    password_list:list = []

    while True:
        choice:str = (input("Do you want lowercase letters?(Y/n)")).casefold()
        if choice == "y":
            print("Ok, your password will contain lowercase letters.")
            password_list.extend(low_alphabet)
            break
        elif choice == "n":
            print("Ok, your password won't contain lowercase letters.")
            break
        else:
            print("Invalid choice, type 'Y' or 'n'.")
    choice = ""
    
    while True:
        choice:str = (input("Do you want uppercase letters?(Y/n)")).casefold()
        if choice == "y":
            print("Ok, your password will contain uppercase letters.")
            password_list.extend(upp_alphabet)
            break
        elif choice == "n":
            print("Ok, your password won't contain uppercase letters.")
            break
        else:
            print("Invalid choice, type 'Y' or 'n'.")
    choice = ""

    while True:
        choice:str = (input("Do you want numbers?(Y/n)")).casefold()
        if choice == "y":
            print("Ok, your password will contain numbers.")
            password_list.extend(numbers_list)
            break
        elif choice == "n":
            print("Ok, your password won't contain numbers.")
            break
        else:
            print("Invalid choice, type 'Y' or 'n'.")
    choice = ""

    while True:
        choice:str = (input("Do you want symbols?(Y/n)")).casefold()
        if choice == "y":
            print("Ok, your password will contain symbols.")
            password_list.extend(symbols_list)
            break
        elif choice == "n":
            print("Ok, your password won't contain symbols.")
            break
        else:
            print("Invalid choice, type 'Y' or 'n'.")
    
    password:str = ""
    for i in range(pass_lenght):
        password += str(random.choice(password_list))

    return password

print("\n", password_generator())