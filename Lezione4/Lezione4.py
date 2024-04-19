#Giovanni di Giuseppe   19/04/2024

def digit_inputter():
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
            print(f"{x} is equal to {check}")
        else:
            print(f"{x} is smaller than {check}")
    x = digit_inputter()
    check = digit_inputter()
    check_value(x, check)

if False:
    #Esercizio 2
    def check_length(x:str, y:float):
        xlen = len(x)
        if xlen > y:
            print(f"The length of the string is bigger than {y}")
        elif xlen == y:
            print(f"The length of the string is equal to {y}")
        else:
            print(f"The length of the string is smaller than {y}")
    
    x:str = "hcijcioqoi"
    y:float = 11
    check_length(x, y)

if False:
    #Eserizio 3
    def print_numbers(x:list):
        for i in x:
            print(i)
    
    listanumerosa:list = [1, 4, 3, 6]
    print_numbers(listanumerosa)

if True:
    #Esercizio 4
    def check_each(x:list, y:float):
        for i in x:
            if i > y:
                print(f"{i} is bigger than {y}")
            elif i == y:
                print(f"{i} is equal to {y}")
            else:
                print(f"{i} is smaller than {y}")
    
    lista_numerevole:list[float] = [4.2, 5.5, 532.532, 53, -5]
    check_each(lista_numerevole, digit_inputter())