"""
Immaginiamo di avere un tipo speciale di sistema numerico 
in cui gli unici elementi costitutivi sono i numeri 2, 3 e 5.
Chiamiamo questi elementi costitutivi "fattori primi" 
perché non possono essere ulteriormente scomposti. 
Un "numero brutto" in questo sistema è un numero costruito 
utilizzando solo questi fattori primi (2, 3 o 5). 
Ad esempio, 6 (che può essere costruito come 2 x 3) è un numero brutto,
ma 7 (che ha un fattore primo pari a 7) non lo è.
"""

def ugly_number(num:int) -> bool:

    while True:
        if num % 2 == 0:
            num = num // 2
        if num % 3 == 0:
            num = num // 3
        if num % 5 == 0:
            num = num // 5
        if num % 2 != 0\
        and num % 3 != 0\
        and num % 5 != 0:
            break
    
    
    if num == 1:
        return True
    else:
        return False

"""
Dato un numero intero, restituisce una stringa 
che ne rappresenta la rappresentazione esadecimale. 
Per gli interi negativi viene utilizzato il metodo del complemento a due.

Tutte le lettere nella stringa di risposta dovrebbero 
essere caratteri minuscoli e non dovrebbero esserci 
zeri iniziali nella risposta tranne lo zero stesso.

Nota: non è consentito utilizzare alcun metodo di libreria 
integrato per risolvere direttamente questo problema.
"""

def to_hex(num: int) -> str:
    print("sium")




"""
Immagina di avere una raccolta di note musicali 
rappresentate da una serie di numeri interi. 
Queste note possono avere altezze (valori) diversi. 
Una sequenza armoniosa è come una melodia piacevole 
in cui la differenza di altezza tra la nota massimale 
e quella minimale è uguale a 1. 
Ad esempio, la serie di note [3,2,2,2,3] è armoniosa, 
perché la differenza fra 3 e 2 è 1.

Trovare l'armonia perfetta:

Il tuo compito è scrivere una funzione che prenda 
come input questa serie di note musicali (numeri). 
La funzione dovrebbe trovare la sequenza armoniosa 
più lunga che puoi creare da queste note. 
Ricorda, una sottosequenza è una selezione di note 
dalla lista originale che mantiene l'ordine degli elementi.

Colpire le note giuste:

Ad esempio, se nums è [1, 3, 2, 2, 5, 2, 3, 7], 
la sottosequenza armonica più lunga è [3, 2, 2, 2, 3]. 
La funzione dovrebbe restituire 5 (la lunghezza di questa sottosequenza).

"""

def find_lhs(nums: list[int]) -> int:
    counter:int = 0
    harm:list = []
    harm_val:str = ''
    compharm:list = []
    compharm_val:str = ''
    num_count:dict = {
    }

    for i in nums:
        if i not in num_count:
            num_count[i] = nums.count(i)
    
    prev_ki:str = ''
    for ki, vi in num_count.items():
        if prev_ki != '':
            if (ki == prev_ki\
            or ki - prev_ki == 1\
            or ki - prev_ki == -1)\
            and len(harm) == 0:
                harm.append(ki)
                harm.append(prev_ki)
                harm_val = vi + (num_count[prev_ki])
            else:
                if (ki == prev_ki\
                or ki - prev_ki == 1\
                or ki - prev_ki == -1)\
                and ki not in harm:
                    compharm_val = vi + (num_count[prev_ki])
                    if compharm_val > harm_val:
                        harm_val = compharm_val

        else:
            prev_ki == ki

    return harm_val

print(find_lhs([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]))

"""
Date due stringhe note e magazine, restituisci true se note 
può essere costruita utilizzando le lettere di magazine 
e false in caso contrario. 
Ogni lettera nella magazine può essere utilizzata 
solo una volta in note.
"""

def ransom(note: str, magazine: str) -> bool:
    note_list = list(note)
    magazine_list = list(magazine)

    note_count:dict = {
    }
    magazine_count:dict = {
    }
    krink:bool = True
    
    for i in note_list:
        if i not in note_count:
            note_count[i] = note_list.count(i)

    for i in magazine_list:
        if i not in magazine_count:
            magazine_count[i] = magazine_list.count(i)

    for ki, vi in note_count.items():
        if ki not in magazine_count.keys():
            krink = False
        else:
            if magazine_count[ki] < vi:
                krink = False
    
    return krink