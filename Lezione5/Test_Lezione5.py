#Esercizio 1
"""
Scrivi una funzione che calcola la media di una lista di numeri 
e ritorna il valore arrotondato all'intero più vicino.
"""

if False:
    def rounded_average(numbers: list[int]) -> int:
        # cancella pass e scrivi il tuo codice
        average:int = round(sum(numbers)/len(numbers))
        
        return average

#Esercizio 2
"""
Il codice dovrebbe stampare i numeri all'interno di una lista.

TROVA L'ERRORE E CORREGGI IL CODICE
"""
#Codice originale
"""
numbers: list[int] = [1, 2; 3, 4, 5)

for i in range(numbers):
    print('Number:, i)
"""
#Codice corretto
if False:
    numbers: list[int] = [1, 2, 3, 4, 5]

    for i in range(1, len(numbers)+1):
        print('Number:', i)

#Esercizio 3
"""
Scrivi una funzione che accetti tre parametri: 
username, password e status di attivazione dell'account (attivo/non attivo). 
L'accesso è consentito solo se il nome utente è "admin", 
la password corrisponde a "12345" e l'account è attivo. 
La funzione ritorna "Accesso consentito" oppure "Accesso negato".
"""

if False:
    def check_access(username: str, password: ..., is_active: bool) -> str:
        # cancella ... è definisci il tipo di dato per password, successivamente cancella pass e scrivi il tuo codice
        if username == 'admin'\
        and password == '12345'\
        and is_active == True:
            return ('Accesso consentito')
        else:
            return('Accesso negato')
    
#Eserizio 4
"""
Scrivi una funzione che, data una lista, 
ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
"""

if False:
    def frequency_dict(elements: list) -> dict:
        # cancella pass e scrivi il tuo codice
        count_dict:dict = {
        }
        
        for i in elements:
            current_niter:int = elements.count(i)
            count_dict[i] = current_niter

        return count_dict
    
#Esercizio 5
"""
Scrivi una funzione che converte una temperatura da gradi Celsius 
a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. 
Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.
"""

if False:
    def convert_temperature(to_conv:int, 
                            to_fahrenheit:None=None) -> float:
        # cancella ... e definisci i parametri della funzione, successivamente cancella pass e scrivi il tuo codice
        if to_fahrenheit == None:
            conved:float = (to_conv - 32)/1.8
        else:
            conved:float = to_conv*9/5 + 32

        return conved

#Esercizio 6
"""
Scrivi una funzione che rimuove tutti i duplicati da una lista, 
contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
"""

if False:
    def remove_duplicates(lint:list) -> list:
    # definidici i parametri, cancella pass e scrivi il tuo codice
        lunt:list = lint.copy()
        lont:list = []
        lint.reverse()
        for i in lunt:
            if i not in lont:
                lont.append(i)
            else:
                lint.remove(i)

        lint.reverse()
        return lint
    
#Esercizio 7
"""
Scrivi una funzione che verifica se in una stringa le parentesi 
'(' e ')' sono bilanciate, cioè per ogni parentesi 
che apre c'è la corrispondente parentesi che chiude.
"""

if False:
    def check_parentheses(expression:str) -> bool:
        if expression.startswith('()') == True\
        and expression.endswith(')') == True:
            return True
        else:
            return False
         	
    print(check_parentheses("((()))"))

#Esercizio 8
"""
Scrivi una funzione che conta e ritorna quante volte 
un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato 
sia a destra che a sinistra da elementi uguali.
"""

if False:
    def count_isolated(bub:list[int]) -> int:
        counter:int = 0
        for i in range(len(bub)):
            try:
                if bub[i] != bub[i+1]\
                and bub[i] != bub[i-1]:
                    counter += 1
            except Exception:
                try:
                    if bub[i] != bub[i+1]:
                        counter += 1
                except Exception:
                    if bub[i] != bub[i-1]:
                        counter += 1
        return counter

    print(count_isolated([1, 2, 2, 3, 3, 3, 4]))

#Esercizio 9
"""
Scrivi una funzione che, dato un insieme 
e una lista di numeri interi da rimuovere, 
ritorni un nuovo insieme senza i numeri specificati nella lista.
"""

if False:
    def remove_elements(original_set:set[int], 
                        elements_to_remove:set[int]) -> set[int]:

        set_copy:list = list(original_set).copy()
        for i in set_copy:
            if i in elements_to_remove:
                original_set.remove(i)

        return original_set

    print(remove_elements({1, 2, 3, 4}, [2, 3]))

#Esercizio 10
"""
Scrivi una funziona che unisca due dizionari.
Se una chiave è presente in entrambi, somma i loro valori.
"""

def merge_dictionaries(dict1:dict, dict2:dict) -> dict:
    dict3:dict = {
    }
    if dict1:
        for ki1, vi1 in dict1.items():
            for ki2, vi2 in dict2.items():
                if ki1 in dict2:
                    dict3[ki1] = vi1 + dict2[ki1]
                else:
                    dict3[ki1] = vi1
                    dict3[ki2] = vi2
    else:
        dict3 = dict2

    return dict3

print(merge_dictionaries({}, {'a': 10, 'b': 20}))