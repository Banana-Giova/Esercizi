"""
8. ATM Machine Simulator:

    Create a function that simulates an ATM machine.
    Initialize an account with a starting balance.
    Allow the user to perform transactions such as deposit, withdraw, and check balance.
    Validate transactions against the account balance and available funds.
    Provide appropriate feedback to the user for each transaction.
"""

import sys
sys.path.append('/home/banana/Desktop/Coding/Esercizi')
from Personal_Collection import float_inputter, int_inputter

def atm_sim(available_funds:int, balance:bool=False) -> str:
    print("Hello! Welcome to the ATM Service Software!")
    if balance == False:
        print("It appears that you don't have an account.\n"\
              "You need to create an account to be able to use this ATM Machine.")
        
        while True:
            choice:str = (input("Would you like to create an account?(Y/n)")).lower()
            if choice == "y" or choice == "n":
                print("Okay.")
                break
            else:
                print("Invalid choice, type 'Y' or 'n'.")
        if choice == "y":
            print("To create an account you need a starting balance.\n"\
                  "How much would you like to deposit for your starting balance?\n"\
                  f"- Available Funds: {available_funds}$.")
            while True:    
                how_much:int = int_inputter()
                if (available_funds - how_much) >= 0:
                    available_funds -= how_much
                    balance += how_much
                    print("The cash was deposited successfully.\n"\
                          f"- Balance: {balance}$.\n"\
                          f"- Available Funds: {available_funds}$.")
                    break
                elif (available_funds - how_much) < 0:
                    print(f"Your available funds amount to {available_funds}$.\n"\
                          f"To deposit {how_much}$ insert more cash.")
                else:
                    print("Invalid quantity.")
    if balance != False:
        print("Welcome back to the ATM Service Software, what do you need?\n"\
              "Type 'Deposit' to deposit cash in your balance.\n"\
              "Type 'Withdraw' to withdraw cash from your balance.\n"\
              "Type 'Check' to check your current balance.\n"\
              "Type 'Exit' to close the ATM Service Software.")
    while True:
        if balance != False:
            user_choice:str = (input("Type in a command -> ")).casefold()
        else:
            user_choice:str = "exit"
        
        if user_choice == "deposit":
            print("Input cash how much cash you want to deposit.")
            how_much:int = int_inputter()
            if (available_funds - how_much) >= 0:
                    available_funds -= how_much
                    balance += how_much
                    print(f"The cash was deposited successfully.\n"\
                          f"- Balance: {balance}$.\n"\
                          f"- Available Funds: {available_funds}$.")
            elif (available_funds - how_much) < 0:
                print(f"Your available funds amount to {available_funds}$.\n"\
                      f"To deposit {how_much}$ insert more cash.")
            else:
                print("Invalid quantity.")
            print("Main menu loading...")
        
        elif user_choice == "withdraw":
            print("Input cash how much cash you want to withdraw.")
            how_much:int = int_inputter()
            if (balance - how_much) >= 0:
                    balance -= how_much
                    available_funds += how_much
                    print(f"The cash was deposited successfully.\n"\
                          f"- Balance: {balance}$.\n"\
                          f"- Available Funds: {available_funds}$.")
            elif (available_funds - how_much) < 0:
                print(f"Your balance amount to {balance}$.\n"\
                      f"You can't withdraw {how_much}$.")
            else:
                print("Invalid quantity.")
            print("Main menu loading...")

        elif user_choice == "check":
            print(f"- Your balance amounts to {balance}$.\n"\
                  f"- Your available funds amount to {available_funds}$.")
            print("Main menu loading...")
        
        elif user_choice == "exit":
            print("Goodbye!")
            break

        else:
            print("Error, invalid input.")

atm_sim(500)