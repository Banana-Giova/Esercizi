"""
9-1. Restaurant: 
- Make a class called Restaurant. 
The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating that the restaurant is open. 
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

9-2. Three Restaurants: 
- Start with your class from Exercise 9-1. Create three different instances from the class, 
and call describe_restaurant() for each instance.
9-3. Users: 
- Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user. 
Create several instances representing different users, and call both methods for each user.

9-4. Number Served: 
- Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. Print the number of customers the restaurant has served, 
and then change this value and print it again. 
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again. 
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business. 

9-5. Login Attempts: 
- Add an attribute called login_attempts to your User class from Exercise 9-3. 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0.

9-6. Ice Cream Stand: 
- An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. 
Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. 
Write a method that displays these flavors. 
Create an instance of IceCreamStand, and call this method. 

9-7. Admin: 
- An administrator is a special kind of user. 
Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 or Exercise 9-5. 
Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 
Write a method called show_privileges() that lists the administrator’s set of privileges. 
Create an instance of Admin, and call your method. 

9-8. Privileges: 
- Write a separate Privileges class. 
The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.

9-9. Battery Upgrade: 
- Use the final version of electric_car.py from this section. 
Add a method to the Battery class called upgrade_battery(). 
This method should check the battery size and set the capacity to 65 if it isn’t already. 
Make an electric car with a default battery size, call get_range() once, 
and then call get_range() a second time after upgrading the battery. 
You should see an increase in the car’s range.

9-10. Imported Restaurant: 
- Using your latest Restaurant class, store it in a module. 
Make a separate file that imports Restaurant. 
Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
9-11. Imported Admin: 
- Start with your work from Exercise 9-8. 
Store the classes User, Privileges, and Admin in one module. 
Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
9-12. Multiple Modules: 
- Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
9-13. Dice: 
- Make a class Die with one attribute called sides, which has a default value of 6. 
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
9-14. Lottery: 
- Make a list or tuple containing a series of 10 numbers and 5 letters. 
Randomly select 4 numbers or letters from the list 
and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
9-15. Lottery Analysis: 
- You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 
Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. 
Print a message reporting how many times the loop had to run to give you a winning ticket.
"""


    #9-1. Restaurants, 9-2. Three Restaurants & 9-4. Number Served:
class Restaurant:
    def __init__(self, rest_name:str, cusine_type:str,
                number_served:int=0) -> None:
        self.rest_name = rest_name
        self.cusine_type = cusine_type
        self.number_served = number_served

    def describe_restaurant(self):
        return f"{self.rest_name} is specialised "\
            f"in {self.cusine_type} and "\
            f"served {self.number_served} customers."
    
    def open_restaurant(self):
        return f"{self.rest_name} is open today!"
    
    def set_number_served(self, new_n:int):
        self.number_served = new_n

    def increment_number_served(self, increment:int):
        self.number_served += increment

if False:
    betto_e_mary:Restaurant = Restaurant("Betto e Mary",
                                         "cucina romana")
    reinbo:Restaurant = Restaurant("Reinbo Sushi",
                                   "cucina orientale", 22)
    viecce:Restaurant = Restaurant("Viecce",
                                   "cucina da pub", 713)
    
    print(betto_e_mary.describe_restaurant())
    print(reinbo.describe_restaurant())
    print(viecce.describe_restaurant())

    print(betto_e_mary.open_restaurant())
    print(reinbo.open_restaurant())
    print(viecce.open_restaurant())

    viecce.increment_number_served(101)
    viecce.set_number_served(42)
    print(viecce.describe_restaurant())
    betto_e_mary.set_number_served(1000)
    print(betto_e_mary.describe_restaurant())



#9-3. Users & 9-5. Login Attempts:
class User:
    def __init__(self, first_name:str, last_name:str,
                    date_of_birth:str, gender:str) -> None:
    
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        return f"{self.first_name}, {self.last_name}, "\
                f"{self.date_of_birth}, {self.gender} | "\
                f"Login Attempts: {self.login_attempts}"
    
    def greet_user(self):
        return f"Hello {self.first_name}!"
    
    def increment_login_attempts(self, increment:int):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

if False:
    giovanni:User = User("Giovanni", "di Giuseppe",
                         "19/07/2002", "M")
    andrea:User = User("Andrea", "Paddington",
                       "27/01/2004", "M")
    marco:User = User("Marco", "De Stefano",
                      "14/10/2004", "M")
    
    print(giovanni.describe_user())
    print(andrea.describe_user())
    print(marco.describe_user())

    print(giovanni.greet_user())
    print(andrea.greet_user())
    print(marco.greet_user())

    giovanni.increment_login_attempts(5)
    print(giovanni.describe_user())
    giovanni.reset_login_attempts()
    print(giovanni.describe_user())

if False:
    #9-6. Ice Cream Stand:
    class IceCreamStand(Restaurant):
        def __init__(self, rest_name: str, flavors: list[str], 
                     cusine_type:str = "Ice Cream", 
                     number_served: int = 0) -> None:
            super().__init__(rest_name, cusine_type, 
                             number_served)
            
            self.rest_name = rest_name
            self.cusine_type = cusine_type
            self.number_served = number_served
            self.flavors = flavors

        def which_flavors(self):
            flavoring:str = ''
            print("Our flavors are:")
            for i in self.flavors:
                flavoring += i
                if i != self.flavors[-1]\
                and i != self.flavors[-2]:
                    flavoring += ', '
                elif i == self.flavors [-2]:
                    flavoring += ' and '
                else:
                    flavoring += '.'
            print(flavoring)

    the_gelatist:IceCreamStand\
               = IceCreamStand(rest_name="The Gelatist",
                               flavors=["Peach", 
                                        "Peruvian Chocolate",
                                        "Lemon", "Raffaello", 
                                        "Berries"])
    
    the_gelatist.which_flavors()
    print(the_gelatist.describe_restaurant())


#9-7. Admin:
class Admin(User):
    def __init__(self, first_name: str, last_name: str, 
                    date_of_birth: str, gender: str,
                    privileges: list[str]) -> None:
        super().__init__(first_name, last_name, 
                            date_of_birth, gender)
        
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.login_attempts = 0
        self.privileges = privileges
        
    def show_privileges(self):
        privilegium:str = ''
        print("The privileges of the admin are:")
        for i in self.privileges:
            privilegium += i
            if i != self.privileges[-1]\
            and i != self.privileges:
                privilegium += ', '
            else:
                privilegium += '.'
        print(privilegium)

if False:
    giovanni_admin:Admin = Admin("Giovanni", "di Giuseppe",
                           "19/07/2002", "M",
                           ["Modify documents", "Download updates",
                            "Seek larger souls", 
                            "Lest this land swallow us all"])
    
    giovanni_admin.show_privileges()

if False:
    #9-8. Privileges:
    
    class Privileges:
        def __init__(self, privileges:list[str]) -> None:
            self.privileges = privileges

        def show_privileges(self):
            privilegium:str = ''
            print("The privileges of the admin are:")
            for i in self.privileges:
                privilegium += i
                if i != self.privileges[-1]\
                and i != self.privileges:
                    privilegium += ', '
                else:
                    privilegium += '.'
            print(privilegium)
    
    class Admin(User):
        def __init__(self, first_name: str, last_name: str, 
                     date_of_birth: str, gender: str,
                     privileges: Privileges) -> None:
            super().__init__(first_name, last_name, 
                             date_of_birth, gender)
            
            self.first_name = first_name
            self.last_name = last_name
            self.date_of_birth = date_of_birth
            self.gender = gender
            self.login_attempts = 0
            self.privileges = privileges
            
        def show_privileges(self):
            privilegium:str = ''
            print("The privileges of the admin are:")
            for i in self.privileges:
                privilegium += i
                if i != self.privileges[-1]\
                and i != self.privileges:
                    privilegium += ', '
                else:
                    privilegium += '.'
            print(privilegium)

    giovannis_privileges:Privileges \
                       = Privileges(["Modify documents", "Download updates",
                                    "Seek larger souls", 
                                    "Lest this land swallow us all"])
    giovanni_admin:Admin = Admin("Giovanni", "di Giuseppe",
                           "19/07/2002", "M",
                           giovannis_privileges)
    
    giovanni_admin.privileges.show_privileges()


if False:
    #9-9. Battery Upgrade:
    """
    electric_car.pu assente
    Esercizio non completabile
    """

if False:
    #9-10. Imported Restaurant, 9-11. Imported Admin & 9-12. Multiple Modules:
    from module_import1 import Restaurant, User
    from module_import2 import Admin, Privileges

    betto_e_mary:Restaurant = Restaurant("Betto e Mary",
                                         "cucina romana")
    reinbo:Restaurant = Restaurant("Reinbo Sushi",
                                   "cucina orientale", 22)
    viecce:Restaurant = Restaurant("Viecce",
                                   "cucina da pub", 713)
    
    print(betto_e_mary.describe_restaurant())
    print(reinbo.describe_restaurant())
    print(viecce.describe_restaurant())

    print(betto_e_mary.open_restaurant())
    print(reinbo.open_restaurant())
    print(viecce.open_restaurant())

    viecce.increment_number_served(101)
    viecce.set_number_served(42)
    print(viecce.describe_restaurant())
    betto_e_mary.set_number_served(1000)
    print(betto_e_mary.describe_restaurant())

    print("\n------------------------------------------------------\n")

    giovannis_privileges:Privileges \
                       = Privileges(["Modify documents", "Download updates",
                                    "Seek larger souls", 
                                    "Lest this land swallow us all"])
    giovanni_admin:Admin = Admin("Giovanni", "di Giuseppe",
                           "19/07/2002", "M",
                           giovannis_privileges)
    
    giovanni_admin.privileges.show_privileges()

if False:
    #9-13. Dice:
    import random
    class Die:
        def __init__(self, sides:int=6) -> None:
            self.sides = sides

        def roll_die(self):
            return f"Rolling... {random.randint(1, self.sides)}!\n"\
                   f"This die has {self.sides} faces."

    d6:Die = Die()
    d10:Die = Die(10)
    d20:Die = Die(20)

    if True:
        for i in range(10):
            print (d6.roll_die())
    if True:
        for i in range(10):
            print (d10.roll_die())
    if True:
        for i in range(10):
            print (d20.roll_die())

if True:
    #9-14. Lottery & 9-15. Lottery Analysis:
    import random

    low_alphabet:list = list(map(chr, range(ord('a'), ord('z')+1)))
    upp_alphabet:list = []
    for i in low_alphabet:
        upp_alphabet.append(i.capitalize())
    letters:list = []
    letters.extend(low_alphabet)
    letters.extend(upp_alphabet)

    lottery:list = []
    for i in range(5):
        lottery.append(str(random.choice(letters)))
    for i in range(10):
        lottery.append(random.randint(0,9))
    
    if False:
        print("The alphanums are...")
        for i in range(4):
            print(str(random.choice(lottery)))

    my_ticket:list = ["4", "7", "7", "4"]

    counter = 0
    beb:bool = True
    while beb == True:
        lucky:list =[]
        for i in range(4):
            lucky.append(str(random.choice(lottery)))
        
        if lucky[0] == my_ticket[0]\
        and lucky[1] == my_ticket[1]\
        and lucky[2] == my_ticket[2]\
        and lucky[3] == my_ticket[3]:
            print(f"You won! It took {counter} tries.")
            beb = False
        else:
            counter += 1