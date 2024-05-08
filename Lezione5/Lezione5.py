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
"""

if False:
    #9-1. Restaurants, 9-2. Three Restaurants & 9-4. Number Served:
    class Restaurant:
        def __init__(self, rest_name:str, cusine_type:str,
                     number_served:int=0):
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

if False:
    #9-3. Users & 9-5. Login Attempts:
    class User:
        def __init__(self, first_name:str, last_name:str,
                     date_of_birth:str, gender:str):
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