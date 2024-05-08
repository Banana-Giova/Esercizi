#Giovanni di Giuseppe   18/04/2024
#Esercizi Lezione 5

"""
1. Create a Playlist:

Write a function called create_playlist() that accepts a playlist name and a variable number of song titles. 
The function should return a dictionary with the playlist name and a set of songs. 
Call the function with different numbers of songs to demonstrate flexibility.

Example: create_playlist("Road Trip", {"Song 1", "Song 2"})

Write a function called add_like() that accepts a dictionary, the name of a playlist, 
and a boolean value indicating whether it is liked (True or False). 
This function should return an updated dictionary.

Example: add_like(dictionary, “Road Trip”, liked=True)

2. Book Collection:

Write a function called add_book() that accepts an author's name and a variable number of book titles authored by them. 
This function should return a dictionary where the author's name is the key and the value is a list of their books. 
Demonstrate this function by adding books for different authors.

Example: add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])

Write a function called delete_book() that accepts a dictionary and the name of the author from whom to remove all details. 
This function should return an updated dictionary.

Example: delete_book(dictionary, “Mark Twain”)

3. Personal Info:

Write a build_profile() function that accepts the name , surname,  occupation, location, and age  of a person. 
Make occupation, location, and age optional parameters. Use this function to create profiles for different people, 
demonstrating how it handles these optional parameters.

Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)

4. Event Organizer:

Write a function called plan_event() that accepts an event name, a list of participants, and an hour. 
The function should return a dictionary that includes the event name and a list of the participants. 
Call this function with varying numbers of participants to plan different events.

Example: plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],”4pm”)

Write a function called modify_event() that accepts a dictionary, an event name, and new details to modify an already planned event.

Example: modify_event(dictionary, "Code Workshop", ["Alice", "Bob", "Charlie"], ”4pm”)

5. Shopping List:

Write a function called create_shopping_list() that accepts a store name and any number of items as arguments. 
It should return a dictionary with the store name and a set of items to buy there. 
Test the function with different stores and item lists.

Example: create_shopping_list("Grocery Store", {"Milk", "Eggs", "Bread"})

Write a function called print_shopping_list() that accepts a dictionary and a store name, 
then prints each item from that store's shopping list.

Example: print_shopping_list(dictionary, "Grocery Store")
"""

if False:
    #1. Create Playlist
    def create_playlist(play_name:str, songs:set) -> dict:

        book_dict:dict = {
        }
        book_dict[play_name] = songs

        return book_dict

    def add_like(prev_play:dict[str, set], prev_name:str, 
                 liked:bool) -> dict:
        
        prev_play[prev_name] = liked

        return prev_play

    print(create_playlist("Road Trip", {"Song 1", "Song 2"}))
    print(create_playlist("Imagine Humans", {"Monster", "Thuder", "Demons", "Sharks"}))
    print(create_playlist("Termonli Core", {"Luigi il Pugilista"}))

    pino = create_playlist("Road Trip", {"Song 1", "Song 2"})
    print(add_like(pino, "Road Trip", True))

if False:
    #2. Book Collection.
    def add_book(auth_name:str, books:int, prev_libr:None=None) -> dict:
        
        book_dict:dict = {
        }
        if prev_libr == None:
            book_dict[auth_name] = books
        else:
            prev_libr[auth_name] = books
            book_dict = prev_libr

        return book_dict
    
    archginnasio:dict = add_book("Mark Twain", ["The Adventures of Tom Sawyer", "Life on the Mississippi"])
    print(archginnasio)
    add_book("Herman Hesse", ["Il Lupo della Steppa", "Siddharta"], archginnasio)
    print(archginnasio)

    def delete_book(prev_libr:dict, auth_name:str) -> dict:

        if auth_name in prev_libr:
            del prev_libr[auth_name]

        return prev_libr
    
    delete_book(archginnasio, "Mark Twain")
    print(archginnasio)

if False:
    #3. Personal Info:
    def build_profile(name:str, surname:str, 
                      occupation:None=None, location:None=None, 
                      age:None=None) -> dict:
        profile:dict = {
        }

        profile["Name"] = name
        profile["Surname"] = surname

        if occupation != None:
            profile["Occupation"] = occupation
        if location != None:
            profile["Location"] = location
        if age != None:
            profile["Age"] = age
        
        return profile
    
    john_doe:dict = build_profile("John", "Doe", occupation="Developer", location="USA", age=30)
    print(john_doe)
    carlo_conti:dict = build_profile("Carlo", "Conti", occupation="TV Host", age=63)
    print(carlo_conti)
    andrea_paddington:dict = build_profile("Andrea", "Paddington")
    print(andrea_paddington)

if False:
    #4. Event Organizer:
    def plan_event(event_name:str, participants:list[str], hour:str) -> dict:
        event_dict:dict = {
        }
        
        event_dict[event_name] = (participants, hour)

        return event_dict
    
    megarave_viterbo:dict = plan_event("Code Workshop", ["Alice", "Bob", "Charlie"],"4pm")
    print(megarave_viterbo)

    def modify_event(prev_event:dict, event_name:str, *details) -> dict:

        if event_name in prev_event:
            prev_event[event_name] = details

        return prev_event
    
    modify_event(megarave_viterbo, "Code Workshop", ["Alice", "Bob", "Charlie"], "6pm")
    print(megarave_viterbo)

if False:
    #5. Shopping List:
    def create_shopping_list(store_name:str, *items) -> dict:

        cart:dict = {
        }
        cart[store_name] = set(items)

        return cart


    shopshop:dict = create_shopping_list("Grocery Store", "Milk", "Eggs", "Bread")

    def print_shopping_list(shopping_list:dict, store_name:str) -> str:
        
        for i in shopping_list[store_name]:
            print(i)

    print_shopping_list(shopshop, "Grocery Store")