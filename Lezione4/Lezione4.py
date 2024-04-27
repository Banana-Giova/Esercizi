"""
8-1. Message: 
- Write a function called display_message() that prints one sentence telling everyone what you are learning about 
in this chapter. Call the function, and make sure the message displays correctly.
8-2. Favorite Book: 
- Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
Call the function, making sure to include a book title as an argument in the function call.

8-3. T-Shirt: 
- Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

8-4. Large Shirts: 
- Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
8-5. Cities: 
- Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value. 
Call your function for three different cities, at least one of which is not in the default country.

8-6. City Names: 
- Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this: "Santiago, Chile". 
Call your function with at least three city-country pairs, and print the values that are returned.

8-7. Album: 
- Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, 
and it should return a dictionary containing these two pieces of information. 
Use the function to make three dictionaries representing different albums. 
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary.
Make at least one new function call that includes the number of songs on an album.
8-8. User Albums: 
- Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.

8-9. Messages: 
- Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
8-10. Sending Messages: 
- Start with a copy of your program from Exercise 8-9. Write a function called send_messages() 
that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.

8-11. Archived Messages: 
- Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.

8-12. Sandwiches: 
- Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides, 
and it should print a summary of the sandwich that’s being ordered. Call the function three times, 
using a different number of arguments each time.

8-13. User Profile: 
- Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that describe you. 
All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67".

8-14. Cars: 
- Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True). 
Print the dictionary that’s returned to make sure all the information was stored correctly. 

8-15. Printing Models: 
- Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
8-16. Imports: 
- Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
8-17. Styling Functions: 
- Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.
"""

if False:
    #8-1 Message:
    def display_message() -> str:
        print("Sto studiando Python!")

    display_message()

if False:
    #8-2 Favorite Book:
    def favorite_book(x: str) -> str:
        print(f"One of my favorite books is {x}")

    favorite_book("The Metamorphosis")

if False:
    #8-3. T-Shirt:
    def make_shirt(x: str, y: str) -> str:
        print(f"The shirt is size {x} and on it there's written the following message: ' {y} '")

    make_shirt("XS", "Vendo CD falsi di Gigi D'Alessio")        #print with positional arguments
    make_shirt(y="Vendo CD falsi di Gigi D'Alessio", x="XS")    #print with keyword arguments
    L_shirt:str = "L"                                           #setting the default variable for the function
    py_message:str = "I love Python"
    make_shirt(L_shirt, py_message)                             #print with default variable
    make_shirt("M", py_message)                                 #print with a positional argument and a default variable
    make_shirt("XL", "Metro boomin' make it boom")



if False:
    #8-5. Cities:
    def describe_city(x:str, y:str) -> str:
        print(f"{x} is in {y}")

    var_country:str = "Italy"                   #setting the default variable for the function
    describe_city("Sassari", var_country)
    describe_city("Benevento", var_country)
    describe_city("Alnicco", var_country)

if False:
    #8-6. City Names:
    def city_country(x:str, y:str) -> str:
        print(f"{x}, {y}")

    city_country("Stockholm", "Sweden")
    city_country("Copenhagen", "Denmark")
    city_country("Oslo", "Norway")

if False:
    #8-7. Album & 8-8. User Album:
    def make_album(x:str, y:str, opt:None=None) -> dict[str, str]:                      
        #opt is an optional variable, a variable which already has a
        #definition, therefore in the definition of the args including
        #it is optional
        new_dict:dict[str, str] = {"Artist Name": x, "Album Title": y, "Songs": opt}
        return new_dict
    
    danger:dict = make_album("Nitro", "Danger")
    sincer:dict = make_album("Mostro", "Sinceramente Mostro")               #dictionaries of albums
    mood:dict = make_album("Nayt", "Mood", 15)

    for ki, vi in danger.items():       
        print(f"{ki}: {vi}")
    for ki, vi in sincer.items():       
        print(f"{ki}: {vi}")      #loop to iterate and print items
    for ki, vi in mood.items():       
        print(f"{ki}: {vi}")

    complete_ver:bool = False
    while complete_ver == False:
        try:             #try to avoid wrong inputs by the user
            art_name:str = input("Input the name of the artist -> ")
            art_name:str = str(art_name)
            alb_name:str = input("Input the name of the album -> ")
            alb_name:str = str(alb_name)
            dict_name:dict = make_album(art_name, alb_name)
            for ki, vi in dict_name.items():       #loop to iterate and print items
                print(f"{ki}: {vi}\n")
            complete_ver = True     #when the inputs has been given, the while loop ends by this conditon
        except Exception:
            print("An invalid value has been inserted, try again.")

if False:
    #8-9. Messages:
    suco_de_wosap:list[str] = ["Hello!", "Hi there!", "How are you doing?", "Fine :)"]
    def show_messages(x:list[str]) -> str:
        for i in x:     #loop to iterate and print every message
            print(i)
    
    show_messages(suco_de_wosap)

if False:
    #8-10. Sending Messages & 8-11. Archived Messages:
    suco_de_wosap:list[str] = ["Hello!", "Hi there!", "How are you doing?", "Fine :)"]
    copy_suco_de_wosap:list = suco_de_wosap.copy()
    def show_messages(x:list[str]) -> str:
        sent_messages:list = []
        for i in x:     #loop to iterate and print every message
            print(i)
            sent_messages.append(i)     #append the iterated value to the sent messages list
        x.clear()       #clearing the original list
        print(f"Here are the messages that were sent: \n{sent_messages}")

    show_messages(suco_de_wosap)
    print(f"Here's the original list of messages: \n{suco_de_wosap}")
    print(f"Here's a copy of the archived messages: \n{copy_suco_de_wosap}")