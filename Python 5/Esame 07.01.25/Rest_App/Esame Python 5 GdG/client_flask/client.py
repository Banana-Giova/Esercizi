from flask import Flask, request # type: ignore
import json
import requests
from datetime import date
accesso_filiale = True

def fetchOrCasa(context:dict={}) -> dict:
    try:
        data = { 'context': context }
        url = 'http://localhost:4160/'
        headers = { 'Content-Type': 'application/json' }
        response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
        response.raise_for_status()
        #data = json.load((response.json()))
        output = response.json()

        return output
    except Exception as e:
        raise Exception(f"Error during Fetch Or Casa:\n{e}")

def cerca_vendita():

    metri_min = input("Inserire i metri quadri minimi\n>>> ")
    metri_max = input("Inserire i metri quadri massimi\n>>> ")
    vani_min = input("Inserire i vani minimi\n>>> ")
    vani_max = input("Inserire i vani massimi\n>>> ")
    prezzo_min = input("Inserire il prezzo minimo\n>>> ")
    prezzo_max = input("Inserire il prezzo massimo\n>>> ")
    while True:
        input_stato = input("La si vuole Libera o Occupata? Digita L per Libera e O per Occupata.\n>>> ")
        match str(input_stato.upper()):
            case "L":
                stato = "LIBERO"
                break
            case "O":
                stato = "OCCUPATO"
                break
            case _:
                print("Selezione invalida.")

    new_query = {"metri_min" : metri_min, "metri_max" : metri_max, 
                    "vani_min" : vani_min, "vani_max" : vani_max, 
                    "prezzo_min": prezzo_min, "prezzo_max" : prezzo_max, "stato":stato}
    sendata = {'operation':1, 'new_query':new_query}
    response = fetchOrCasa(sendata)
    print(f"Ecco ciò che risulta dai nostri database per i parametri specificati:\n {response}")

def cerca_affitto():
    while True:
        input_tipo = input("La si vuole Parziale o Totale? Digita P per Parziale e T per Totale.\n>>> ")
        match str(input_tipo.upper()):
            case "P":
                tipo = "PARZIALE"
                break
            case "T":
                tipo = "TOTALE"
                break
            case _:
                print("Selezione invalida.")
    while True:
        input_bagno = input("E' richiesto un bagno personale? (S/n)\n>>> ")
        match str(input_bagno.upper()):
            case "S":
                bagno = "TRUE"
                break
            case "N":
                bagno = "FALSE"
                break
            case _:
                print("Selezione invalida.")
    prezzo_min = input("Inserire un prezzo mensile minimo.\n>>> ")
    prezzo_max = input("Inserire un prezzo mensile massimo.\n>>> ")

    new_query = {"tipo":tipo, "bagno":bagno, 
                 "prezzo_max":prezzo_max, "prezzo_min":prezzo_min}
    sendata = {'operation':2, 'new_query':new_query}
    response = fetchOrCasa(sendata)
    print(f"Ecco ciò che risulta dai nostri database per i parametri specificati:\n {response}")

def metti_in_vendita():
    catastale = input("Inserire la catastale (max 50 caratteri)\n>>> ")
    indirizzo = input("Inserire l'indirizzo (max 255 caratteri)\n>>> ")
    numero_civico = int(input("Inserire il numero civico (numero intero)\n>>> "))
    piano = int(input("Inserire il piano (numero intero)\n>>> "))
    metri = float(input("Inserire i metri quadri (numero decimale)\n>>> "))
    vani = int(input("Inserire il numero di vani (numero intero)\n>>> "))
    prezzo = int(input("Inserire il prezzo (numero intero)\n>>> "))
    
    # Ciclo per chiedere lo stato
    while True:
        stato = input("La casa è Libera o Occupata? Digita 'L' per Libera e 'O' per Occupata.\n>>> ").upper()
        if stato == 'L':
            stato = 'LIBERO'
            break
        elif stato == 'O':
            stato = 'OCCUPATO'
            break
        else:
            print("Selezione invalida. Riprova.")

    new_query = {
        "catastale": catastale,
        "indirizzo": indirizzo,
        "civico": numero_civico,
        "piano": piano,
        "metri": metri,
        "vani": vani,
        "prezzo": prezzo,
        "stato": stato,
    }

    sendata = {'operation': 3, 'new_query': new_query}
    response = fetchOrCasa(sendata)
    print(f"Risultati per la messa in vendita dell'immobile:\n{response}")

def metti_in_affitto():
    catastale = input("Inserire la catastale (max 50 caratteri)\n>>> ")
    indirizzo = input("Inserire l'indirizzo (max 255 caratteri)\n>>> ")
    civico = int(input("Inserire il numero civico (numero intero)\n>>> "))
    
    while True:
        tipo_affitto = input("Il tipo di affitto è Parziale o Totale? Digita 'P' per Parziale e 'T' per Totale.\n>>> ").upper()
        if tipo_affitto == 'P':
            tipo_affitto = 'PARZIALE'
            break
        elif tipo_affitto == 'T':
            tipo_affitto = 'TOTALE'
            break
        else:
            print("Selezione invalida. Riprova.")

    while True:
        input_bagno = input("E' richiesto un bagno personale? (S/n)\n>>> ")
        match str(input_bagno.upper()):
            case "S":
                bagno = "TRUE"
                break
            case "N":
                bagno = "FALSE"
                break
            case _:
                print("Selezione invalida.")

    prezzo_mensile = int(input("Inserire il prezzo mensile (numero intero)\n>>> "))

    new_query = {
        "catastale": catastale,
        "indirizzo": indirizzo,
        "civico": civico,
        "tipo_affitto": tipo_affitto,
        "bagno": bagno,
        "prezzo_mensile": prezzo_mensile,
    }

    sendata = {'operation': 4, 'new_query': new_query}
    response = fetchOrCasa(sendata)
    print(f"Risultati per la messa in affitto dell'immobile:\n{response}")

def acquista_casa():
    id_select = input("Inserire id della casa che si desidera acquistare\n>>> ")
    prezzo_accordato = input("Inserire il prezzo di vendita accordato con l'agenzia\n>>> ")

    new_query = {
        "id_select":id_select,
        "prezzo_vendita":prezzo_accordato
    }

    sendata = {'operation': 5, 'new_query': new_query}
    response = fetchOrCasa(sendata)
    print(f"Risultati per la vendita immobile:\n{response}")

def affitta_casa():
    id_select = input("Inserire id della casa che si desidera affittare\n>>> ")
    prezzo_accordato = input("Inserire il prezzo di affitto accordato con l'agenzia\n>>> ")
    durata_contratto = input("Inserire la durata del contratto stabilita con l'agenzia\n>>> ")

    new_query = {
        "id_select":id_select,
        "prezzo_affitto":prezzo_accordato,
        "durata_contratto":durata_contratto
    }

    sendata = {'operation': 6, 'new_query': new_query}
    response = fetchOrCasa(sendata)
    
    print(f"Risultati per la vendita immobile:\n{response}")

def operazione_utente(username:str):
    while True:
        print(f"Cosa vuoi fare oggi {username}?\n1) Cerca una casa in vendita\n2) Cerca una casa in affitto\n3) Metti in vendita una casa\n4) Metti in affitto una casa\n5) Acquista una casa\n6) Affitta una casa\n7) Esci\n")
        risposta = input(">>> ")
        match int(risposta):
            case 1:
                cerca_vendita()
            case 2:
                cerca_affitto()
            case 3:
                metti_in_vendita()
            case 4:
                metti_in_affitto()
            case 5:
                acquista_casa()
            case 6:
                affitta_casa()
            case 7:
                print("Grazie per aver scelto Immobiliare Romano!")
                break
            case _:
                print("Selezione invalida, riprovare!")

def accesso_utente():
    accesso = False
    while not accesso:
        print("Per accedere alla sezione utenti, si è pregati di inserire i propri dati.\nQualora non risultassero nel database verrà creato un account usando tali dati.")
        username = input("Inserire nome utente\n>>> ")
        password = input("Inserire password\n>>> ")
        new_query = {
            'username':username,
            'password':password
        }
        sendata = {'operation':7, 'new_query':new_query}
        response = fetchOrCasa(sendata)

        if response['utente_nuovo']:
            print("Account creato, grazie per aver scelto Immobiliare Romano!")
            accesso = True
        else:
            if not response['password_errata']:
                print(f"Accesso effettuato! Benvenuto/a {username}!")
                accesso = True
            else:
                print("L'username non coincide con la password, riprova!")
    operazione_utente(username=username)

def accesso_marketing():
    pass

while accesso_filiale:

    filiale = input("Da quale filiale stai accedendo?\n>>> ")
    sendata = {'operation':0, 'filiale':filiale}
    response = fetchOrCasa(sendata)

    if response["filiale_presente"]:
        accesso_filiale = False
    else:
        print("Nessuna filiale con tale partita IVA. Riprovare!")

print("Benvenuto in Immobiliare Romano, compra case a Roma con facilità!")
while True:
    print("Seleziona a quale sezione accedere!\n1) Accedi alla sezione Utenti\n2) Accedi alla sezione Marketing\n3) Esci\n")
    risposta = input(">>> ")
    match int(risposta):
        case 1:
            accesso_utente()
        case 2:
            accesso_marketing()
        case 3:
            print("Grazie per aver scelto Immobiliare Romano!")
            break
        case _:
            print("Selezione invalida, riprovare!")