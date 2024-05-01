"""
2. Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
"""

def rngesus(userange:int) -> str:
    import random
    n_to_guess:int = random.randint(1, userange)
    print("RNGesus initialized.")
    count:int = 0

    while True:
        count += 1
        if count < 11:
            guess = input("Make your guess! -> ")
            try:
                guess = int(guess)
                if guess > n_to_guess:
                    print("Wrong guess, your number is too high!")
                elif guess < n_to_guess:
                    print("Wrong guess, your number is too low!")
                else:
                    print("Correct, you won!")
                    break
            except ValueError:
                print("""Insert a valid int number, 
strings and floats are not accepted!""")
        else: 
            print("Attempts ran out, you lost! Try again!")
            break

import sys
sys.path.append('/home/banana/Desktop/Coding/Esercizi')
from Personal_Collection import int_inputter

rngesus(int_inputter())