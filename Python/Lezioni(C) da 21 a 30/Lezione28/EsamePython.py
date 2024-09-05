"""
Esercizio 1

Scrivi una funzione che unisce due dizionari. 
Se una chiave è presente in entrambi, moltiplica i loro valori.
"""

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    
    for ki, vi in dict2.items():
        if ki not in dict1:
            dict1[ki] = vi
        else:
            dict1[ki] *= vi

    return dict1

"""
Esercizio 2

Scrivi una funzione che moltiplica tutti i numeri interi 
di una lista che sono minori di un dato 
valore intero definito threshold.
"""

def moltiplica_numeri(numbers: list[int], threshold: int) -> int:
    output = 1
    for i in numbers:
        if i < threshold:
            if output == 1:
                output = i
            else:
                output *= i
    
    return output

"""
Esercizio 3

Scrivi una funzione che accetti tre parametri: 
user, passw e stato dell'account (attivo/non attivo). 
L'accesso è consentito solo se il nome utente è "manager", 
la password corrisponde a "67890" e l'account è attivo (True). 
La funzione ritorna "Ingresso consentito" 
oppure "Ingresso negato".
"""

def verifica_accesso(user: str, passw: str, stato: bool) -> str:
    if user == 'manager'\
    and passw == '67890'\
    and stato:
        return 'Ingresso consentito'
    else:
        return 'Ingresso negato'
    
"""
Esercizio 4

In questo esercizio, creeremo una gerarchia di classi per rappresentare diversi tipi di elettrodomestici.
 
1. Classe Base: Elettrodomestico
Crea una classe base chiamata Elettrodomestico con i seguenti attributi e metodi:
 
Attributi:

    marca: str
    modello: str
    potenza: int

Metodi:

    __init__(self, marca: str, modello: str, potenza: int): metodo costruttore che inizializza gli attributi marca, modello e potenza.
    descrivi_elettrodomestico(self): metodo che stampa una descrizione dell'elettrodomestico nel formato "Marca: {marca}, Modello: {modello}, Potenza: {potenza}W"

2. Classe Derivata: Frigorifero
Crea una classe derivata chiamata Frigorifero che eredita dalla classe Elettrodomestico e aggiunge i seguenti attributi e metodi:

Attributi:

    capacità: int

Metodi:

    __init__(self, marca: str, modello: str, potenza: int, capacità: int): metodo costruttore che inizializza gli attributi della classe base e capacità.
    descrivi_elettrodomestico(self): metodo che sovrascrive quello della classe base per includere anche la capacità nella descrizione, nel formato "Marca: {marca}, Modello: {modello}, Potenza: {potenza}W, Capacità: {capacità}L"

Classe Derivata: Lavatrice
Crea una classe derivata chiamata Lavatrice che eredita dalla classe Elettrodomestico e aggiunge i seguenti attributi e metodi:

Attributi:
- carico_max: int

Metodi:
- __init__(self, marca: str, modello: str, potenza: int, carico_max: int): metodo costruttore che inizializza gli attributi della classe base e carico_max.
- descrivi_elettrodomestico(self): metodo che sovrascrive quello della classe base per includere anche il carico massimo nella descrizione, nel formato "Marca: {self.marca}, Modello: {modello}, Potenza: {potenza}W, Carico massimo: {carico_max}kg".
"""

class Elettrodomestico:
    def __init__(self, marca:str, modello:str, 
                 potenza:int) -> None:
        self.marca = marca
        self.modello = modello
        self.potenza = potenza

    def descrivi_elettrodomestico(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W")

class Frigorifero(Elettrodomestico):
    def __init__(self, marca: str, modello: str, 
                 potenza: int, capacità:int) -> None:
        super().__init__(marca, modello, potenza)
        self.capacità = capacità

    def descrivi_elettrodomestico(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Capacità: {self.capacità}L")

class Lavatrice(Elettrodomestico):
    def __init__(self, marca: str, modello: str, 
                 potenza: int, carico_max:int) -> None:
        super().__init__(marca, modello, potenza)
        self.carico_max = carico_max

    def descrivi_elettrodomestico(self):
        print(f"Marca: {self.marca}, Modello: {self.modello}, Potenza: {self.potenza}W, Carico massimo: {self.carico_max}kg")

"""
Esercizio 5

Sviluppa un sistema per la gestione dei contatti in Python che permetta agli utenti di creare, modificare, e cercare contatti basati sui numeri di telefono. Il sistema dovrà essere capace di gestire una collezione (dizionario) di contatti e i loro numeri di telefono.

1. Classe ContactManager:
Gestisce tutte le operazioni legate ai contatti.
 
Attributi:

    contacts: dict[str, list[str]] - Dizionario che ha per chiave il nome del contatto e per valore una lista di numeri di telefono. I numeri di telefono sono espressi sottoforma di stringa.

Metodi:

    create_contact(name: str, phone_numbers: list[str]): Crea un nuovo contatto, aggiungendolo al dizionario contacts con il nome specificato e una lista di numeri di telefono. Restituisce un nuovo dizionario con il solo contatto appena creato o il messaggio di errore "Errore: il contatto esiste già." se il contatto esiste già.
    add_phone_number(contact_name: str, phone_number: str): Aggiunge un numero di telefono al contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono esiste già." se il numero di telefono è già presente per il contatto specificato.
    remove_phone_number(contact_name: str, phone_number: str): Rimuove un numero di telefono dal contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
    update_phone_number(contact_name: str, old_phone_number: str, new_phone_number: str): Sostituisce un numero di telefono con un altro nel contatto specificato. Restituisce un nuovo dizionario con il solo contatto aggiornato o i messaggi di errore "Errore: il contatto non esiste." se il contatto non esiste oppure "Errore: il numero di telefono non è presente." se il numero di telefono non esiste per il contatto specificato.
    list_contacts(): Ritorna una lista di tutte le chiavi all'interno del dizionario contacts.
    list_phone_numbers(contact_name: str): Mostra i numeri di telefono di un contatto specifico. Restituisce la lista dei numeri di telefono o il messaggio di errore "Errore: il contatto non esiste." se il contatto non esiste.
    search_contact_by_phone_number(phone_number: str): Trova e restituisce tutti i contatti che contengono un determinato numero di telefono. Restituisce una lista di tutte le chiavi all'interno del dizionario contacts che hanno il numero specificato tra i valori oppure il messaggio di errore "Nessun contatto trovato con questo numero di telefono." se nessun contatto contiene il numero di telefono.
"""

class ContactManager:
    def __init__(self) -> None:
        self.contacts:dict[str, list[str]] = {}

    def create_contact(self, name:str, phone_numbers:list[str]):
        if name not in self.contacts:
            self.contacts[name] = phone_numbers
            return {name:phone_numbers}
        else:
            return "Errore: il contatto esiste già."
    
    def add_phone_number(self, contact_name:str, phone_number:str):
        if contact_name in self.contacts:
            if phone_number not in self.contacts[contact_name]:
                self.contacts[contact_name].append(phone_number)
                return {contact_name:self.contacts[contact_name]}
            else:
                return "Errore: il numero di telefono esiste già."
        else:
            return "Errore: il contatto non esiste."

    def remove_phone_number(self, contact_name:str, phone_number:str):
        if contact_name in self.contacts:
            if phone_number in self.contacts[contact_name]:
                self.contacts[contact_name].remove(phone_number)
                return {contact_name:self.contacts[contact_name]}
            else:
                return "Errore: il numero di telefono non è presente."
        else:
            return "Errore: il contatto non esiste."

    def update_phone_number(self, contact_name:str, 
                            old_phone_number:str, new_phone_number:str):
        if contact_name in self.contacts:
            if old_phone_number in self.contacts[contact_name]:
                new_list = []
                for i in self.contacts[contact_name]:
                    if len(self.contacts[contact_name]) > 1:
                        if i == old_phone_number:
                            new_list.append(new_phone_number)
                        else:
                            new_list.append(i)
                        self.contacts[contact_name] = new_list
                    else:
                        self.contacts[contact_name] = [new_phone_number]
                return {contact_name:self.contacts[contact_name]}
            else:
                return "Errore: il numero di telefono non è presente."
        else:
            return "Errore: il contatto non esiste."
        
    def list_contacts(self):
        return list(self.contacts.keys())
    
    def list_phone_numbers(self, contact_name:str):
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            return "Errore: il contatto non esiste."
        
    def search_contact_by_phone_number(self, phone_number:str):
        out_list:list[str] = []
        for ki, vi in self.contacts.items():
            if phone_number in vi:
                out_list.append(ki)

        if not len(out_list):
            return "Nessun contatto trovato con questo numero di telefono."
        else:
            return out_list