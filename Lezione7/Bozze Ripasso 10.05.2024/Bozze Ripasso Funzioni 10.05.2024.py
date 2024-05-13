#Esercizio 1

def somma_condizionale(numeri: list[int]) -> int :
    
    numeri_accettati:list[int] = []

    for i in numeri:
        if i % 2 == 0 and i % 3 == 0:
            numeri_accettati.append(i)

    return sum(numeri_accettati)

#Esercizio 2

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    
    dict_sblebs:dict[str, int] = {'pari': [],
                                  'dispari': []}
    
    for i in lista:
        if i % 2 == 0:
            dict_sblebs['pari'].append(i)
        else:
            dict_sblebs['dispari'].append(i)

    return dict_sblebs

#Esercizio 3

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    
    counter:int = 0
    ctrl_c:list[int] = lista.copy()
    blacklist:list[int] = []

    for i in ctrl_c:
        if i in da_rimuovere and i not in blacklist:
            while counter != da_rimuovere[i]:
                try:
                    lista.remove(i)
                except Exception:
                    pass
                counter += 1
            counter = 0
            blacklist.append(i)

    return lista

#Esercizio 4

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:

    eggregora:dict = {
    }

    for i in voti:
        if i['nome'] not in eggregora:
            eggregora[i['nome']] = [i['voto']]
        else:
            eggregora[i['nome']].append(i['voto'])

    return eggregora

#Esercizio 5

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    
    sconti:dict[str:float] = {
    }

    for ki, vi in prodotti.items():
        if vi > 20:
            sconti[ki] = (vi*0.9)

    return sconti

#Esercizio 6

def create_contact(name: str, email: str=None, 
                   telefono: int=None) -> dict:
    
    contact:dict = {'profile': name, 
                    'email': email, 
                    'telefono': telefono}
    
    return contact



def update_contact(dictionary: dict, name: str, 
                   email: str =None, telefono: 
                   int=None) -> dict:

    dictionary['profile'] = name
    if email != None:
        dictionary['email'] = email
    if telefono != None:
        dictionary['telefono'] = telefono

    return dictionary