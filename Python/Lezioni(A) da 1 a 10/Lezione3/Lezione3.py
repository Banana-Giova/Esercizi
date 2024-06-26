#Giovanni di Giuseppe   18/04/2024
#Esercizi Lezione 3

"""
4-1. Pizzas: 
- Think of at least three kinds of your favorite pizza. 
Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. 
For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

4-2. Animals: 
- Think of at least three different animals that have a common characteristic. 
Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common. 
You could print a sentence, such as Any of these animals would make a great pet!

4-3. Counting to Twenty: 
- Use a for loop to print the numbers from 1 to 20, inclusive.
4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. 
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
4-5. Summing a Million: 
- Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.
4-6. Odd Numbers: 
- Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
4-7. Threes: 
- Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.
4-8. Cubes: 
- A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. 
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
4-9. Cube Comprehension: 
- Use a list comprehension to generate a list of the first 10 cubes.

4-10. Slices: 
- Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.


4-11. My Pizzas, Your Pizzas: 
- Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
Make sure each new pizza is stored in the appropriate list.

4-12. More Loops: 
- All versions of foods.py in this section have avoided using for loops when printing, to save space. 
Choose a version of foods.py, and write two for loops to print each list of foods.

4-14. PEP 8: 
- Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008. 
You won’t use much of it now, but it might be interesting to skim through it.

4-15. Code Review: 
- Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.

5-1. Conditional Tests: 
- Write a series of conditional tests. 
Print a statement describing each test and your prediction for the results of each test. 
Your code should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

5-2. More Conditional Tests: 
You don’t have to limit the number of tests you create to 10. 
If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
Have at least one True and one False result for each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list

5-3. Alien Colors #1: 
- Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)


5-4. Alien Colors #2: 
- Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.

5-5. Alien Colors #3: 
- Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.


5-6. Stages of Life: 
- Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.

5-7. Favorite Fruit: 
- Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit is in your list. 
If the fruit is in your list, the if block should print a statement, such as You really like Apples!

5-8. Hello Admin: 
- Make a list of five or more usernames, including the name 'admin'. 
Imagine you are writing code that will print a greeting to each user after they log in to a website. 
Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.


5-9. No Users: 
- Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct message is printed.

5-10. Checking Usernames: 
- Do the following to create a program that simulates how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already been used. 
If it has, print a message that the person will need to enter a new username. 
If a username has not been used, print a message saying that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
(To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)


5-11. Ordinal Numbers: 
- Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
"""

if False:
    #4-1. Pizzas:
    pizzas:list[str] = ["Rossa", "Patate e Salsiccia", "Salsiccia e Friarielli"]
    for i in pizzas:
        print(f"I love pizza {i}")
    print(f"I'm a pizza devourer!\nThe best pizza is pizza {pizzas[0]},\nbut {pizzas[1]} is a classic.\n{pizzas[-1]} beats them only if the friarielli are fresh!")

if False:
    #4-2. Animals:
    animals:list[str] = ["Cat", "Caracal", "Cougar"]
    for i in animals:
        print(f"A {i} would make a great pet")
    print("All these animals are felines")

if False:
    #4-3. Counting to Twenty & 4-6. Odd Numbers:
    print("Normal 1 to 20")
    for i in range(1, 21):
        print(i)
    print("Only odd numbers")
    for i in range(1, 20, 2):
        print(i)

if False:
    #4-4. One Million & 4-5. Summing a Million:
    billions:list[int] = []
    for i in range(1, 1000001):
        billions.append(i)
    print(min(billions), max(billions))
    print(sum(billions))

if False:
    #4-7 Threes:
    threes:list[int] = []
    for i in range(3, 31, 3):
        threes.append(i)
    print(threes)

if False:
    #4-8 Cubes & 4-9. Cube Comprehension:
    cubes:list[int] = []
    for i in range(1, 11):
        cubes.append(i**3)
    print(cubes)

if False:
    #4-10. Slices:
    animals:list[str] = ["Cat", "Caracal", "Cheetah", "Cougar", "Leopard", "Lion", "Lynx", "Puma", "Tiger"]
    print(f"The first three felines are {animals[0:3]}")
    print(f"The middle three felines are {animals[3:6]}")
    print(f"The last three felines are {animals[-3:]}")

if False:
    #4-11. My pizzas, Your pizzas & 4-12. More Loops:
    pizzas:list[str] = ["Rossa", "Patate e Salsiccia", "Salsiccia e Friarielli"]
    friends_pizzas:list = pizzas.copy()
    pizzas.append("Focaccia con mortadella")
    friends_pizzas.append("Diavola")
    for i in pizzas:
        print(f"I love pizza {i}")
    for i in friends_pizzas:
        print(f"My friends' favorite pizza is pizza {i}")

if False:
    #4-14. PEP 8 & 4-15. Code Review:
    
    #PEP8 Remake 4-8 Cubes & 4-9. Cube Comprehension:
    cubes:list[int] = [(i**3) for i in range(1, 11)]
    """Used comprehension instead of the full loop"""

    print(cubes)
    
    print("------------------------------------------------------------")

    #PEP8 Remake 4-10. Slices:
    animals:list[str] = ["Cat", "Caracal", "Cheetah", "Cougar", 
                         "Leopard", "Lion", "Lynx", "Puma", "Tiger"]
    """A line shouldn't be over 79 characters. 
    Indentation has to remain on the same level as the list origin.
    """

    print(f"""The first three felines are {animals[0:3]}\n
          The middle three felines are {animals[3:6]}\n
          The last three felines are {animals[-3:]}
          """)
    """A line shouldn't be over 79 characters.
    Printing multiline strings is more easy to read.
    """
    
    print("------------------------------------------------------------")

    #PEP8 Remake 4-11. My pizzas, Your pizzas & 4-12. More Loops:
    pizzas:list[str] = ["Rossa", "Patate e Salsiccia", 
                        "Salsiccia e Friarielli"]
    """A line shouldn't be over 79 characters. 
    Indentation has to remain on the same level as the list origin.
    """

    friends_pizzas:list = pizzas.copy()
    pizzas.append("Focaccia con mortadella")
    friends_pizzas.append("Diavola")

    for i, fri in zip(pizzas, friends_pizzas):
        print(f"I love pizza {i}")
        print(f"My friends' favorite pizza is pizza {fri}")
    """In place of a double for, a zipped for is more clean."""



if False:
    #5-1. Conditional Tests: 
    cat = "Evil"
    print("Is cat == \"Evil\"? I predict True.")
    print(cat == "Evil")
    print("Is cat == \"Stinky\"? I predict False.")
    print(cat == "Stinky")

    car = "Volkswagen"
    print("\nIs car == \"Volkswagen\"? I predict True.")
    print(car == "Volkswagen")
    print("Is car == \"Subaru\"? I predict False.")
    print(car == "Subaru")

    juice = "Peach"
    print("\nIs juice == \"Orange\"? I predict False.")
    print(juice == "Orange")
    print("Is juice == \"Peach\"? I predict True.")
    print(juice == "Peach")

    kiwi = ["Brown", "Green"]
    print("\nIs kiwi == \"Brown\"? I predict True.")
    print("Brown" in kiwi)
    print("Is kiwi == \"Green\"? I predict True.")
    print("Green" in kiwi)

    water = "Moist"
    print("\nIs water == \"Evil\"? I predict False.")
    print(water == "Evil")
    print("Is water == \"Blue\"? I predict False.")
    print(water == "Blue")

if False:
    #5-3 to 5-5. Alien Colors:
    alien_colors:dict[str] = {"1": "Green", "2": "Yellow", "3": "Red"}        #I'll just make one version for all of the three alien colors exercises
    valid_nos:list[int, str] = [1, 2, 3, "1", "2", "3"]                       #it's more interisting, faster and it doesn't hinder my understanding

    inputted_number:str = "No"
    while inputted_number == "No":
        
        inputted_number = input("Inserire un numero da 1 a 3 -> ")
        if inputted_number in valid_nos:
            str(inputted_number)
        else:
            print("Errore, inserire un numero valido.\n")
            inputted_number = "No"
            continue

    shot_alien:str = alien_colors[inputted_number]
    if shot_alien == "Green":
        print("You scored 5 points!")
    elif shot_alien == "Yellow":
        print("You scored 10 points!!")
    else:
        print("You scored 15 points!!!")

if False:
    #5-6. Stages of Life:
    valid_nos:list = []
    for i in range(1, 123):
        valid_nos.append(int(i))

    inputted_number = "No"
    while inputted_number == "No":
        
        inputted_number = input("Inserire un numero -> ")
        if int(inputted_number) in valid_nos:
            inputted_number = int(inputted_number)
        else:
            print("Errore, inserire un numero valido")
            inputted_number = "No"
            continue

    if inputted_number == 0 or inputted_number == 1:
        print("You are a baby.")
    elif inputted_number == 2 or inputted_number == 3 or inputted_number == 4:
        print("You are a toddler.")
    elif inputted_number in valid_nos[4:12]:
        print("You are a kid.")
    elif inputted_number in valid_nos[12:19]:
        print ("You are a teenager.")
    elif inputted_number in valid_nos[19:64]:
        print ("You are an adult.")
    elif inputted_number in valid_nos[64:99]:
        print ("You are an elder.")
    else: 
        print("You are as old as Methuselah.")

if False:
    #5-7. Favorite Fruit:
    favorite_fruits:list[str] = ["Apples", "Mandarins", "Peaches"]

    if "Mandarins" in favorite_fruits:
        print("You really like mandarins!")
    else:
        print("You don't like mandarins!")
    if "Tangerines" in favorite_fruits:
        print("You really like tangerines!")
    else:
        print("You don't like tangerines!")
    if "Apples" in favorite_fruits:
        print("You really like apples!")
    else:
        print("You don't like apples!")
    if "Kiwis" in favorite_fruits:
        print("You really like kiwis!")
    else:
        print("You don't like kiwis!")
    if "Peaches" in favorite_fruits:
        print("You really like peaches!")
    else:
        print("You don't like peaches!")

if False:
    #5-8. Hello Admin & 5-9. No Users:
    usernames:list[str] = ["Peppino", "Mimmo", "Ciro", "admin", "Pasquale"]
    empty_usernames:list = usernames.copy()
    empty_usernames.clear()

    def user_greeter(users:list[str]) -> str:       #I made a function here instead of a copy of the loop
        print("Accessing the list of users...")     #simply because it's faster and more interesting
        if users:       #"if len(users) !=" it's the same as "if users"
            for i in users:
                if i != "admin":
                    print(f"Hello {i}, thank you for logging in again")
                else:
                    print(f"Hello {i}, would you like to see a status report?")
        else:
                print("We need to find some users!")

    user_greeter(usernames)
    user_greeter(empty_usernames)

if False:
    #5-10. Checking Usernames:
    current_users:list[str] = ["Peppino", "Mimmo", "Ciro", "admin", "Pasquale"]
    new_users:list[str] = ["Pino", "Toni", "Ciro", "Gianni", "Pasquale"]
    current_users_case:list = [i.casefold() for i in current_users]    #creation of the control list

    for i in new_users:
        if i.casefold() not in current_users_case:
            print(f"{i} is available!")
            current_users.append(i)
            current_users_case.append(i.casefold())    #it's important to update the control list
        else:
            valid:bool = False          #this while detects already used usernames
            while valid == False:       #and makes the user input a new valid one, accounting for errors
                print(f"{i} is not available! You need to enter a new username!")
                i = input(f"Write your new username! Here's the list of the taken usernames:\n {current_users}\nBe careful, the database is case insensitive!\n>")
                if i.casefold() not in current_users_case:
                    print(f"{i} is available!")
                    current_users.append(i)
                    current_users_case.append(i.casefold())
                    valid = True

    print(f"Here's the list of users with the new usernames!\n{current_users}")
 
if False:
    #5-11. Ordinal Numbers:
    ordinal_numbers:list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in ordinal_numbers:
        if i == 1:
            print(f"{i}st")
        elif i == 2:
            print(f"{i}nd")
        else:
            print(f"{i}th")