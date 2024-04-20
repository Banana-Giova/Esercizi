#Giovanni di Giuseppe   18/04/2024

if False:
    print("I gonfaloni")

def digit_inputter() -> float:
    """
        Questa funzione permette di inputtare rapidamente numeri, 
        senza incorrere in errori nel qual caso venga inserita
        una stringa come input.
    """
    inputted_number = "No"
    while inputted_number == "No":
        
        inputted_number = input()
        try:
            float(inputted_number)
        except ValueError:
            print("Errore, inserire un numero valido")
            inputted_number = "No"
            continue
    return float(inputted_number)

"""
2-3. Personal Message: 
- Use a variable to represent a person’s name, and print a message to that person. 
Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
2-4. Name Cases: 
- Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.
2-5. Famous Quote: 
- Find a quote from a famous person you admire. Print the quote and the name of its author. 
Your output should look something like the following, including the quotation marks: 
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
2-6. Famous Quote 2: 
- Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
Then compose your message and represent it with a new variable called message. Print your message. 
2-8. File Extensions: 
- Python has a removesuffix() method that works exactly like removeprefix(). 
Assign the value 'python_notes.txt' to a variable called filename. 
Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
"""
if False:
    #2-3. Personal Message
    nome:str = "Mario"      #variabile del nome
    print(f"{nome} s'annamo a pija' un gelato?")      #print del messaggio

if False:
    #2-4. Name Cases
    nome:str = "Mario"      #variabile del nome
    nome_mini:str = nome.casefold()
    nome_norm:str = nome.capitalize()       #utilizzo degli string methods sulla stringa
    nome_big:str = nome.upper()
    print(f"{nome_mini}, {nome_norm}, {nome_big}")     #print della modifica

if False:
    #2-5. Famous Quote & 2-6. Famous Quote 2
    nome_famoso:str = "Ghandi"      #variabile del nome
    messaggio_mistico:str = 'Ghandi once said, “Be the change you want in the world.”'       #messaggio
    print(messaggio_mistico)        #print del messaggio

if False:
    #2-8. File Extensions
    filename:str = 'python_notes.txt'       #variabie
    filename_nosuffix:str = filename.removesuffix('.txt')       #variabile privata del suffisso
    print(f"{filename_nosuffix}")       #print della modifica



"""
3-1. Names: 
- Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.
3-2. Greetings: 
- Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. 
The text of each message should be the same, but each message should be personalized with the person’s name.
3-3. Your Own List: 
- Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

3-4. Guest List: 
- If you could invite anyone, living or deceased, to dinner, who would you invite? 
Make a list that includes at least three people you’d like to invite to dinner. 
Then use your list to print a message to each person, inviting them to dinner.

3-5. Changing Guest List: 
- You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. 
You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. 
Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.

3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. 
Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.

3-7. Shrinking Guest List: 
- You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. 
Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program.

3-8. Seeing the World: 
- Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.

3-9. Dinner Guests:
- Working with one of the programs from Exercises 3, 
use len() to print a message indicating the number of people you’re inviting to dinner.

3-10. Every Function: 
- Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""

if False:
    #3-1. Names & 3-2. Greetings
    invitati:list = ["Mario", "Luigi", "Peach", "Bowser"]        #lista nomi
    print(f"Hello sir {invitati[0]}, \n Buongiorno signor {invitati[1]}, \n Hola signorina {invitati[2]}, \n Namasté signor {invitati[-1]}")     #print del messaggio

if False:
    #3-3. Your Own List
    my_own_list:list = ["Monocycle", "Hovercraft", "Space Shuttle"]     #lista di mezzi di trasporto
    print(f"I would like to be know how to ride a {my_own_list[0]}, \n to use a {my_own_list[1]} \n and to own a {my_own_list[2]}")        #print del messaggio

if False:
    #From 3-5 to 3-7, and also 3-9
    guest_list:list = ["Freddie Mercury", "Caius Giulius Caesar Octavianus Augustus", "Albert Einstein"]        #lista dei famosi
    print(f"Let's have a good time together {guest_list[0]} \nA vobis peto, venit {guest_list[1]} \nKomm zu mir nach Haus {guest_list[2]}")      #print del messaggio
    print(f"Oh no, {guest_list[0]} can't come!")        #print dell'ospite che va via
    guest_list[0] = "Totti"     #modifica alla lista
    print(f"Daje Roma {guest_list[0]} vie' 'mpo' che famo festa \nA vobis peto, venit {guest_list[1]} \nKomm zu mir nach Haus {guest_list[2]}")     #print del messaggio
    print("Rega ho trovato un tavolo più grande")       #print tavolo
    guest_list.insert(0, "Pippo Baudo")
    guest_list.insert(2, "Peppe Brescia")      #aggiunta ospiti
    guest_list.append("Topolino")
    print(f"Daje Roma {guest_list[1]} vie' 'mpo' che famo festa, c'è pure {guest_list[0]} \nA vobis peto, venit {guest_list[3]} cum {guest_list[2]},  \nKomm zu mir nach Haus {guest_list[4]} es gibt auch {guest_list[-1]}")     #print del messaggio
    print("Nevvero, c'è posto solo per 2")
    lost_guest1:str = guest_list.pop(0)
    lost_guest2:str = guest_list.pop(0)     #rimozione ospiti di troppo
    lost_guest3:str = guest_list.pop(0)
    lost_guest4:str = guest_list.pop(0)
    print(f"Cari {lost_guest1}, {lost_guest1}, {lost_guest2}, {lost_guest3}, {lost_guest4} mi spiace, ma non potete più venire")     #messaggio di addio
    print(f"Cari {guest_list[0]} e {guest_list[1]}, voi siete ancora invitati")     #inviti rimanenti

    print(f"Alla fine quindi invito solo {len(guest_list)} persone")        #3-9, numero di invitati

    guest_list.clear()      #svuotare la lista
    print(guest_list)

if False:
    #3-8. Seeing the World
    za_warudo:list = ["Japan", "China", "Iceland", "Switzerland", "Greece"]      #lista di posti nel mondo che vorrei visitare
    print(f"Ordine originale della lista => {za_warudo}")        #raw print
    print(sorted(za_warudo))        #lista ordinata
    print(za_warudo)        #raw print
    print(sorted(za_warudo, reverse=True))        #lista invertita
    print(za_warudo)        #raw print
    za_warudo.reverse()     #invertire la lista
    print(za_warudo)        #reverse print
    za_warudo.reverse()     #reinvertire la lista
    print(za_warudo)        #re-reverse print
    za_warudo.sort()     #oridnare la lista
    print(za_warudo)        #sorted print
    za_warudo.sort(reverse=True)    #ordinare al contrario la lista
    print(za_warudo)        #reverse-sorted print

if False:
    #3-10. Every Function:
    comic_villains:list = ["Joker", "Ultron", "poste.it", "Darkseid", "Magneto", "Lex Luthor"]
    print(f"Ordine originale della lista => {comic_villains}")        #raw print
    comic_villains.append("Thanos")     #append
    print(comic_villains)
    comic_villains.insert(-1, "Nemesis")        #insert
    print(comic_villains.pop(-2))       #pop
    print(comic_villains)
    comic_villains.remove("Magneto")        #remove
    print(comic_villains)
    comic_villains.reverse()        #reverse
    print(comic_villains)
    print(sorted(comic_villains, reverse=True))     #sorted
    comic_villains.sort()       #sort
    print(comic_villains)
    comic_villains_nosu:list[str] = []      #lista vuota per contenere la copia della lista precedente
    for i in comic_villains:        #removesuffix
        if ".it" in i:      #ciclo per verificare quale variabile ha il suffisso e rimuoverlo
            comic_villains_nosu.append(i.removesuffix(".it"))        #una volta individuato si inserisce in una nuova variabile senza suffisso e la si appende
        else:
            comic_villains_nosu.append(i)       #riempire la nuova lista, senza il suffisso
    print(comic_villains_nosu)
    comic_villains.clear()      #clear
    print(comic_villains)
    del comic_villains      #del



"""
6-1. Person: 
- Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city. 
Print each piece of information stored in your dictionary.
6-2. Favorite Numbers: 
- Use a dictionary to store people’s favorite numbers. 
Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary. 
Print each person’s name and their favorite number. 
For even more fun, poll a few friends and get some actual data for your program.
6-3. Glossary: 
- A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. 
Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, 
or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

6-7. People: 
- Start with the program you wrote for Exercise 6-1. 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
Loop through your list of people. As you loop through the list, print everything you know about each person.

6-8. Pets: 
- Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. 
Next, loop through your list and as
you do, print everything you know about each pet. 

6-9. Favorite Places: 
- Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
Loop through the dictionary, and print each person’s name and their favorite places.
6-10. Favorite Numbers: 
- Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.
6-11. Cities: 
- Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, 
its approximate population, and one fact about that city. 
The keys for each city’s dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.

6-12. Extensions: 
- We’re now working with examples that are complex enough that they can be extended in any number of ways. 
Use one of the example programs from this chapter, and extend it by adding new keys and values, 
changing the context of the program, or improving the formatting of the output.
"""

if False:
    #6-1. Person:
    person_info:dict[str, {str, int}] = {"Nome": "Carlo", "Cognome": "Conti", "Age": 63, "City": "Firenze" }     #dizionario sulle info di Carlo Conti
    for i in person_info:       #ciclo for per iterare
        print(person_info[i])       #print delle value del dict

if False:
    #6-2. Favorite Numbers:
    best_nums:dict[str, int] = {"Giovanni": 47, "Emanuele": 10, "Lorenzone": 7, "Lollino": 22, "Marco": 69}     #lista dei numeri preferiti
    for ki, vi in best_nums.items():       #ciclo for per iterare
        print(f"{ki}: {vi}\n")       #print del dict

if False:
    #6-3. Glossary:
    new_python_words:dict[str, str] = {"Runtime Error": "Errore che avviene nel terminale.", 
                                       "Syntax Error": "Errore di sintassi nel linguaggio di programmazione.",
                                       "Logical Error": "Errore nella logica del programma, anche se funziona.",          #dizionario su python
                                       "Iterare": "Scorrere in un ciclo fra gli elementi di una collezione indicizzata.",
                                       "Castare": "Specificare il tipo di una variabile." }
    for ki, vi in new_python_words.items():       #ciclo for per iterare
        print(f"{ki}:\n {vi}\n")       #print del dict

if False:
    #6-7. People:
        carlo_info:dict[str, {str, int}] = {"Nome": "Carlo", "Cognome": "Conti", "Age": 63, "City": "Firenze" }     #dizionario sulle info di Carlo Conti
        amadeus_info:dict[str, {str, int}] = {"Nome": "Amedeo", "Cognome": "Sebastiani", "Age": 62, "City": "Ravenna" }     #dizionario sulle info di Amadeus
        gerry_info:dict[str, {str, int}] = {"Nome": "Virginio", "Cognome": "Scotti", "Age": 67, "City": "Pavia" }     #dizionario sulle info di Gerry Scotti
        conduttori_italiani:list[dict] = [carlo_info, amadeus_info, gerry_info]     #lista di dizionari
        for i in conduttori_italiani:
            for ki, vi in i.items():        #doppio ciclo per legghere tutti i dizionari
                print(f"{ki}: {vi}")

if False:
    #6-8 Pets:
    albicocca:dict[str, str] = {"Nome": "Albicocca", "Tipo di animale": "Gatto", "Padrone": "Ludovica"}
    isa:dict[str, str] = {"Nome": "Isa", "Tipo di animale": "Gatto", "Padrone": "Giovanni"}
    ariel:dict[str, str] = {"Nome": "Ariel", "Tipo di animale": "Cane", "Padrone": "Eleonora"}      #dizionari degli animali
    koda:dict[str, str] = {"Nome": "Koda", "Tipo di animale": "Cane", "Padrone": "Nicola"}
    cowo:dict[str, str] = {"Nome": "Cowo", "Tipo di animale": "Porcellino d'India", "Padrone": "Flavio"}
    animali:list[dict] = [albicocca, isa, ariel, koda, cowo]        #lista di dizionari
    for i in animali:
            for ki, vi in i.items():        #doppio ciclo per leggere tutti i dizionari
                print(f"{ki}: {vi}")

if False:
    #6-9 Favorite Places:
    favorite_places:dict[str, list[str]] = {"Anakin": ["Death Star", "Cities of the Empire", "The Bathroom"],
                                            "Solo": ["Millenium Falcon", "Where Chewbe is", "Graphite"],            #dizionario con liste
                                            "R2D2": ["On top of a cruiser", "With C3PO", "The Broom Closet"]}
    for ki, vi in favorite_places.items():       #ciclo for per iterare
        print(f"{ki}:\n {vi}\n")       #print del dict
    
if False:
    #6-10 Favorite Numbers (part 2):
    best_nums:dict[str, list[int]] = {"Giovanni": [47, 11], "Emanuele": [10, 1], 
                                      "Lorenzone": [7, 77], "Lollino": [22, 27], "Marco": [69, 96]}     #lista dei numeri preferiti
    for ki, vi in best_nums.items():       #ciclo for per iterare
        print(f"{ki}: {vi}\n")       #print del dict

if False:
    #6-11. Cities:
    cities:dict[str, dict[str, str, int]] = {"Rome": {"Country": "Italy", "Population": 4355000, "Fact": "Rome was the first city in the world to reach 1 million citizens"},
                                             "Stockholm": {"Country": "Sweden", "Population": 2450000, "Fact": "People live in the area Stockholm is built in since the Stone Age"},    #dizionari sulle citta'
                                             "Barcelona": {"Country": "Spain", "Population": 1460000, "Fact": "Barcelona has 12 completely abandoned underground stations"}}
    for ki, vi in cities.items():
            print(ki)
            for ki2, vi2 in vi.items():        #doppio ciclo per leggere tutti i dizionari, con print della chiave
                print(f"{ki2}: {vi2}")

if False:
    #6-12. Extensions:
    dong:dict[str, dict[str, str, int]] = {"noot.space": {"Name": "Noot-Space", "Creation Date": "26/02/2015", "Function": "Has a GIF of Pingu in infinite loop and interacting with the page makes Pingu say \"Noot Noot\"."},
                                           "isthiswhite.com": {"Name": "Is-It-White.com", "Creation Date": "27/02/2015", "Function": "Informs the user that the background of the website is in fact not white. However, the font on the website indeed is white."},    
                                           "pixelfighting.com": {"Name": "Pixel-Fighting.com", "Creation Date": "22/11/2012", "Function": "Shows a battle between clumps of pixels, in which the winning pixel clump takes over the space of the losing clump."}, 
                                           "pointerpointer.com": {"Name": "Pointer-Pointer.com", "Creation Date": "08/06/2012", "Function": "When the pointer of the mouse rests on the screen for a few seconds finds an image containing a person pointing at the pointer."},         #dizionario su siti divertenti
                                           "staggeringbeauty.com": {"Name": "Staggering-Beauty.com", "Creation Date": "30/07/2012", "Function": "It tracks the movements of the pointer associating it with a pool noodle-like creature. \nIf the pointer is moved fast enough the screen and the creature will flicker. The website also has an epilepsy warning."}, 
                                           "papertoilet.com": {"Name": "Paper-Toilet.com", "Creation Date": "03/05/2006", "Function": "There's a roll of toilet paper. When pulling the paper it will unroll the roll of toilet paper. \nWhen it ends, it won't come back."},
                                           "cat-bounce.com": {"Name": "Cat-Bounce.com", "Creation Date": "14/09/2012", "Function": "When opening the website cats will fall from the top of your screen and bounce around when they hit the bottom. \nYou can also manipulate the cats using your pointer."}, 
                                           "eelslap.com": {"Name": "Eel-Slap.com", "Creation Date": "02/03/2011", "Function": "When moving the pointer back and forth in this website, a man will get repeatedly slapped by an eel. \nThe position of your pointer on the screen determines where the eel will be."}}
    for ki, vi in dong.items():    
        for ki2, vi2 in vi.items():                 #doppio ciclo per leggere tutti i dizionari
            vi3 = vi2.replace("-", " ")             #replace per rimuovere i trattini e inserire uno spazio vuoto
            if ".com" in vi2:                       #if per verificare se c'e' un suffisso ed eventualmente rimuoverlo
                vi3 = vi3.removesuffix(".com")      #else per gli altri casi
                print(f"{ki2}: {vi3}\n")            #print di tutto con un divisore per ogni iterazione
            else:
                print(f"{ki2}: {vi2}\n")
        print("--------------------")