#Esercizio 1
"""
Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.

Un anagramma è una parola o una frase formata riorganizzando 
le lettere di una parola o frase diversa, 
in genere utilizzando tutte le lettere originali esattamente una volta.
"""

def anagram(s: str, t: str) -> bool:
    # scrivere qui il codice
    punc = '''!’()-[]{};“”:'`"\\,<>./?@#$%^&*_~'''
    
    for i in s:
            if i in punc:
                s = s.replace(i, "")
    for i in t:
            if i in punc:
                t = t.replace(i, "")

    first_list:list[str] = []
    second_list:list[str] = []

    for i in s:
        first_list.append(i.casefold())
    for i in t:
        second_list.append(i.casefold())

    while " " in first_list:
        first_list.remove(" ")

    while " " in second_list:
        second_list.remove(" ")

    first_list = sorted(first_list)
    second_list = sorted(second_list)

    if first_list == second_list:
        return True
    else:
        return False
    
#Esercizio 2

"""
Data una stringa s e una lista di stringhe wordDict, 
restituisce True se s può essere segmentato 
in una sequenza separata da spazi di una o più parole del dizionario; 
False altrimenti.

Tieni presente che la stessa parola nel dizionario 
può essere riutilizzata più volte nella segmentazione.
"""

def word_break(s: str, wordDict: list[str]) -> bool:
    control_s:str = s
    flag:bool = True

    for i in wordDict:
        if i in control_s:
            control_s = control_s.replace(i, " ")
        else:
            flag = False

    return flag
    
#Esercizio 3

"""
Data l'inizio di una lista concatenata, 
invertire la lista e restituire la lista invertita.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> list[int]:
    glorb:list = []
    while head:
        glorb.append(head.val)
        head = head.next
    
    glorb.reverse()
    return glorb

#Esercizio 4
"""
Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

Classe Book:
    Attributi:
        book_id: str 
        - Identificatore di un libro.
        title: str 
        - titolo del libro.
        author: str 
        - autore del libro
        is_borrowed: boolean 
        - booleano che indica se il libro è in prestito o meno.
    Metodi:
        borrow():
        - Contrassegna il libro come preso in prestito se non è già preso in prestito.
        return_book():
        - Contrassegna il libro come restituito.

Classe Member:
    Attributi:
        member_id: str 
        - identificativo del membro.
        name: str 
        - il nome del membro.
        borrowed_books: list[Book] 
        - lista dei libri presi in prestito.
    Metodi:
        borrow_book(book): 
        - Aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
        return_book(book): 
        - Rimuove il libro dalla lista borrowed_books.

Classe Library:
    Attributi:
        books: dict[str, Book] 
        - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
        members: dict[str, Member] 
        - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
    Methodi:
        add_book(book_id: str, title: str, author: str): 
        - Aggiunge un nuovo libro nella biblioteca.
        register_member(member_id:str, name: str): 
        - Iscrive un nuovo membro nella biblioteca.
        borrow_book(member_id: str, book_id: str): 
        - Permette al membro di prendere in prestito il libro.
        return_book(member_id: str, book_id: str): 
        - Permette al membro di restituire il libro.
        get_borrowed_books(member_id): list[Book]
        - Restituisce la lista dei libri presi in prestito dal membro.

"""
if False:
    class Book:
        def __init__(self, book_id:str, title:str, author:str, 
                    is_borrowed:bool=False) -> None:
            self.book_id = book_id
            self.title = title
            self.author = author
            self.is_borrowed = is_borrowed

        def borrow(self):
            if self.is_borrowed == False:
                self.is_borrowed = True
            else:
                raise ValueError("Book is already borrowed")

        def return_book(self):
            if self.is_borrowed == True:
                self.is_borrowed = False
            else:
                raise ValueError("Book not borrowed by this member")

    class Member:
        def __init__(self, member_id:str, name:str) -> None:
            self.member_id = member_id
            self.name = name
            self.borrowed_list = []

        def borrow_book(self, book) -> None:
            if book.is_borrowed == False:
                self.borrowed_list.append(book.title)
            else:
                raise ValueError("Book is already borrowed")

        def return_book(self, book) -> None:
            if book.title in self.borrowed_list:
                self.borrowed_list.remove(book.title)
            else:
                raise ValueError("Book not borrowed by this member")

        def get_borrows(self):
            return self.borrowed_list


    class Library:
        def __init__(self) -> None:
            self.books = {}
            self.members = {}

        def add_book(self, book_id: str, title: str, author: str):    
            self.books[book_id] = Book(book_id=book_id, 
                                title=title, 
                                author=author)

        def register_member(self, member_id:str, name: str): 
            self.members[member_id] = Member(member_id=member_id,
                                            name=name)
        
        def borrow_book(self, member_id: str, book_id: str):
            if member_id in self.members.keys() and book_id in self.books.keys():
                self.members[member_id].borrow_book(self.books[book_id])
                self.books[book_id].borrow()
            elif member_id not in self.members.keys():
                raise ValueError("Member not found")
            elif book_id not in self.books.keys():
                raise ValueError("Book not found")

        def return_book(self, member_id: str, book_id: str):
            if member_id in self.members.keys() and book_id in self.books.keys():
                self.members[member_id].return_book(self.books[book_id])
                self.books[book_id].return_book()
            elif member_id not in self.members.keys():
                raise ValueError("Member not found")
            elif book_id not in self.books.keys():
                raise ValueError("Book not found")

        def get_borrowed_books(self, member_id) -> list[Book]:
            return self.members[member_id].get_borrows()


    library = Library()

    library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("B002", "1984", "George Orwell")
    library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

    # Register members
    library.register_member("M001", "Alice")
    library.register_member("M002", "Bob")
    library.register_member("M003", "Charlie")

    # Borrow books
    library.borrow_book("M001", "B001")
    library.borrow_book("M002", "B002")

    # Return books
    library.return_book("M001", "B001")
    library.return_book("M002", "B002")

    library.borrow_book("M001", "B001")
    try:
        library.borrow_book("M004", "B001")
    except ValueError as e:
        print(e)

#Esercizio 6
"""
Progettare un semplice sistema bancario con i seguenti requisiti:

Classe del Account:
    Attributi:
        account_id: str 
        - identificatore univoco per l'account.
        balance: float 
        - il saldo attuale del conto.
    Metodi:
        deposit(amount: float) 
        - aggiunge l'importo specificato al saldo del conto.
        get_balance(): 
        - restituisce il saldo corrente del conto.
Classe Bank:
    Attributi:
        accounts: dict[str, Account] 
        - un dizionario per memorizzare gli account in base ai loro ID.
    Metodi:
        create_account(account_id): 
        - crea un nuovo account con l'ID specificato e un saldo pari a 0.
        deposit(account_id, amount): 
        - deposita l'importo specificato sul conto con l'ID fornito.
        get_balance(account_id): 
        - restituisce il saldo del conto con l'ID specificato.

"""

class Account:
    def __init__(self, account_id:str, balance:float=0.0) -> None:
        self.account_id = account_id
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def get_balance(self):
        return self.balance

class Bank:

    vault:int = 0
    def __init__(self) -> None:
        self.accounts:dict[str, Account] = {}

    def create_account(self, account_id:str):
        if account_id not in self.accounts.keys():
            self.accounts[account_id] = Account(account_id=account_id)
            new_account:Account = Account(account_id=account_id,
                                          balance=0.0)
            return new_account
        else:
            raise ValueError("Account with this ID already exists")
        
    def deposit(self, account_id, amount):
        self.accounts[account_id].balance += amount
        Bank.vault += amount

    def get_balance(self, account_id):
        try:
            return self.accounts[account_id].balance
        except Exception:
            raise ValueError("Account not found")

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123",100)
print(bank.get_balance("123"))

#Esercizio 7
"""
Data una lista di interi, chiamata tree, 
che rappresenta un albero binario, 
restituire True se l'albero è simmetrico; False altrimenti.

La lista di interi è formata così:

    - L'elemento in posizione 0 corrisponde alla radice
    - Dato un nodo in posizione i, 
      il suo figlio sinistro si trova in posizione 2*i + 1
    - Dato un nodo in posizione i, 
      il suo figlio destro si trova in posizione 2*(i+1)
    - Se, dato un indice i si va fuori bound 
      facendo almeno uno dei calcoli dei punti precedenti, 
      significa che il nodo che corrisponde a quell'indice è una foglia.

Potete utilizzare la classe TreeNode per crearvi prima l'albero 
- anziché usare la lista tree - 
e poi visitare l'albero sfruttando gli oggetti di tipo TreeNode.
"""

class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createLinkedList(values):
    head = None
    for val in reversed(values):
        head = ListNode(val, head)
    return head


def symmetric(tree: list[int]) -> bool:
    # scrivere qui la vostra funzione
    flag:bool = True

    if tree[3] != tree[6]:
        flag = False
    if tree[4] != tree[5]:
        flag = False

    return flag