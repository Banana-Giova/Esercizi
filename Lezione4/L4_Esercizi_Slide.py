#Giovanni di Giuseppe   19/04/2024

def digit_inputter() -> float:
    """
        Questa funzione permette di inputtare rapidamente numeri, 
        senza incorrere in errori nel qual caso venga inserita
        una stringa come input.
    """
    inputted_number = "No"
    while inputted_number == "No":
        
        inputted_number = input("Inserire un numero -> ")
        try:
            float(inputted_number)
        except ValueError:
            print("Errore, inserire un numero valido")
            inputted_number = "No"
            continue
    return float(inputted_number)
    


if False:
    #Esercizio 0
    def subtract(x:float, y:float) -> float:     #funzione per sottrarre due numeri
        subt = x - y        #scope
        return subt     #valore returnato
    
    x, y = (17, 7)      #variabili da una tupa spacchettata
    print(subtract(x, y))       #print della funzione

if False:
    #Esercizio 1
    def check_value(x:float, check:float):
        if x > check:
            print(f"{x} is bigger than {check}")
        elif x == check:
            print(f"{x} is equal to {check}")           #funzione per rilevare quale fra due numeri e' piu' grande
        else:
            print(f"{x} is smaller than {check}")
    x = digit_inputter()
    check = digit_inputter()        #utilizzo della funzione digit_inputter
    check_value(x, check)

if False:
    #Esercizio 2
    def check_length(x:str, y:float):
        xlen = len(x)
        if xlen > y:
            print(f"The length of the string is bigger than {y}")
        elif xlen == y:
            print(f"The length of the string is equal to {y}")      #funzione per rilevare quale fra un numero
        else:                                                       #e la lunghezza di una stringa e' piu' grande
            print(f"The length of the string is smaller than {y}")
    
    x:str = "hcijcioqoi"
    y:float = 11            #variabili
    check_length(x, y)

if False:
    #Eserizio 3
    def print_numbers(x:list):      #funzione print_numbers
        for i in x:
            print(i)
    
    listanumerosa:list = [1, 4, 3, 6]       #lista di integers
    print_numbers(listanumerosa)

if False:
    #Esercizio 4
    def check_each(x:list, y:float):        #funzione per rilevare quale fra un numero in una lista ed un int e' piu' grande
        for i in x:
            if i > y:
                print(f"{i} is bigger than {y}")
            elif i == y:
                print(f"{i} is equal to {y}")
            else:
                print(f"{i} is smaller than {y}")
    
    lista_numerevole:list[float] = [4.2, 5.5, 532.532, 53, -5]      #lista di integers
    check_each(lista_numerevole, digit_inputter())

if False:
    #Esercizio 5
    def add_one(addint:int):        #funzione per sommare 1 ad un int
        addint += 1
        return addint
    
    def add_one_to_list(lint:list[int]):        #funzione per sommare 1 ad ogni elemento di una lista
        new_list:list[int] = []
        for i in lint:
            new_list.append(add_one(i))
        print (new_list)
    
    lint:list[int] = [4,1,412,341,134,6,8,0]        #lista di integers
    add_one_to_list(lint)