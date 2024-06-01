if False:
    """
    Versione non funzionante
    """
    class Book:
        def __init__(self, isbn:str, title:str, author:str, 
                    is_borrowed:bool=False) -> None:
            self.isbn = isbn
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
            
        def __str__(self):
            return f"Title: {self.title}, Author: {self.author}, "\
                +  f"ISBN: {self.isbn}"

    class Member:
        def __init__(self, member_id:str, name:str,
                     borrowed_books:list=[]) -> None:   #modifica dalla funzionante
            self.member_id = member_id
            self.name = name
            self.borrowed_books = borrowed_books

        def borrow_book(self, book) -> None:
            if book.is_borrowed == False:
                self.borrowed_books.append(book.title)
            else:
                raise ValueError("Book is already borrowed")

        def return_book(self, book) -> None:
            if book.title in self.borrowed_books:
                self.borrowed_books.remove(book.title)
            else:
                raise ValueError("Book not borrowed by this member")

        def __str__(self):
            return f"Name: {self.name}, Member ID: {self.member_id}, "\
                +  f"Borrowed Books: {self.borrowed_books}"

    class Library:
        total_books:int = 0

        def __init__(self) -> None:
            self.books = {}
            self.members = {}

        def add_book(self, book:Book):    
            self.books[book.isbn] = book
            Library.total_books += 1

        def remove_book(self, book:Book):    
            del self.books[book.isbn]
            Library.total_books -= 1

        def register_member(self, member:Member): 
            self.members[member.member_id] = member
        
        def borrow_book(self, member:Member, book:Book):
            member_id = member.member_id
            isbn = book.isbn
            if member_id in self.members.keys() and isbn in self.books.keys():
                self.members[member_id].borrow_book(self.books[isbn])
                self.books[isbn].borrow()
            elif member_id not in self.members.keys():
                raise ValueError("Member not found")
            elif isbn not in self.books.keys():
                raise ValueError("Book not found")

        def return_book(self, member:Member, book:Book):
            member_id = member.member_id
            isbn = book.isbn
            if member_id in self.members.keys() and isbn in self.books.keys():
                self.members[member_id].return_book(self.books[isbn])
                self.books[isbn].return_book()
            elif member_id not in self.members.keys():
                raise ValueError("Member not found")
            elif isbn not in self.books.keys():
                raise ValueError("Book not found")

        def __str__(self) -> list[Book]:
            to_print:str = "- Books:\n"
            for i in self.books.values():
                to_print += i.__str__() + ";\n"
            to_print += "\n- Members:\n"
            for i in self.members.values():
                to_print += i.__str__() + ";\n"
            to_print += "\n----------------------------------------------------\n"
            return to_print

        @classmethod
        def library_statistics(cls):
            return f"Total books: {Library.total_books}"



    giancarlo:Member = Member(name="Giancarlo",
                            member_id="C4RL")
    gianpiero:Member = Member(name="Gianpiero",
                            member_id="P13R")

    principles:Book = Book(title="Principles",
                        author="Ray Dalio",
                        isbn="1501124021")
    sotto_le_cuffie:Book = Book(title="Sotto le Cuffie",
                        author="Favij",
                        isbn="8891802697")
    steppenwolf:Book = Book(title="The Steppenwolf",
                        author="Herman Hesse",
                        isbn="1324036818")

    archiginnasio:Library = Library()
    archiginnasio.register_member(giancarlo)
    archiginnasio.register_member(gianpiero)
    archiginnasio.add_book(principles)
    archiginnasio.add_book(sotto_le_cuffie)
    archiginnasio.add_book(steppenwolf)
    print(archiginnasio)
    archiginnasio.borrow_book(giancarlo, steppenwolf)
    archiginnasio.borrow_book(giancarlo, sotto_le_cuffie)
    archiginnasio.borrow_book(giancarlo, principles)
    print(archiginnasio)
    archiginnasio.return_book(giancarlo, sotto_le_cuffie)
    archiginnasio.borrow_book(gianpiero, sotto_le_cuffie)
    print(archiginnasio)
    print(Library.library_statistics())



if True:
    """
    Versione funzionante.
    """
    class Book:
        def __init__(self, isbn:str, title:str, author:str, 
                    is_borrowed:bool=False) -> None:
            self.isbn = isbn
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
            
        def __str__(self):
            return f"Title: {self.title}, Author: {self.author}, "\
                +  f"ISBN: {self.isbn}"

    class Member:
        def __init__(self, member_id:str, name:str) -> None:
            self.member_id = member_id
            self.name = name
            self.borrowed_books = []

        def borrow_book(self, book) -> None:
            if book.is_borrowed == False:
                self.borrowed_books.append(book.title)
            else:
                raise ValueError("Book is already borrowed")

        def return_book(self, book) -> None:
            if book.title in self.borrowed_books:
                self.borrowed_books.remove(book.title)
            else:
                raise ValueError("Book not borrowed by this member")

        def __str__(self):
            return f"Name: {self.name}, Member ID: {self.member_id}, "\
                +  f"Borrowed Books: {self.borrowed_books}"

    class Library:
        total_books:int = 0

        def __init__(self) -> None:
            self.books = {}
            self.members = {}

        def add_book(self, book:Book):    
            self.books[book.isbn] = book
            Library.total_books += 1

        def remove_book(self, book:Book):    
            del self.books[book.isbn]
            Library.total_books -= 1

        def register_member(self, member:Member): 
            self.members[member.member_id] = member
        
        def borrow_book(self, member:Member, book:Book):
            member_id = member.member_id
            isbn = book.isbn
            if member_id in self.members.keys() and isbn in self.books.keys():
                self.members[member_id].borrow_book(self.books[isbn])
                self.books[isbn].borrow()
            elif member_id not in self.members.keys():
                raise ValueError("Member not found")
            elif isbn not in self.books.keys():
                raise ValueError("Book not found")

        def return_book(self, member:Member, book:Book):
            member_id = member.member_id
            isbn = book.isbn
            if member_id in self.members.keys() and isbn in self.books.keys():
                self.members[member_id].return_book(self.books[isbn])
                self.books[isbn].return_book()
            elif member_id not in self.members.keys():
                raise ValueError("Member not found")
            elif isbn not in self.books.keys():
                raise ValueError("Book not found")

        def __str__(self) -> list[Book]:
            to_print:str = "- Books:\n"
            for i in self.books.values():
                to_print += i.__str__() + ";\n"
            to_print += "\n- Members:\n"
            for i in self.members.values():
                to_print += i.__str__() + ";\n"
            to_print += "\n----------------------------------------------------\n"
            return to_print

        @classmethod
        def library_statistics(cls):
            return f"Total books: {Library.total_books}"



    giancarlo:Member = Member(name="Giancarlo",
                            member_id="C4RL")
    gianpiero:Member = Member(name="Gianpiero",
                            member_id="P13R")

    principles:Book = Book(title="Principles",
                        author="Ray Dalio",
                        isbn="1501124021")
    sotto_le_cuffie:Book = Book(title="Sotto le Cuffie",
                        author="Favij",
                        isbn="8891802697")
    steppenwolf:Book = Book(title="The Steppenwolf",
                        author="Herman Hesse",
                        isbn="1324036818")

    archiginnasio:Library = Library()
    archiginnasio.register_member(giancarlo)
    archiginnasio.register_member(gianpiero)
    archiginnasio.add_book(principles)
    archiginnasio.add_book(sotto_le_cuffie)
    archiginnasio.add_book(steppenwolf)
    print(archiginnasio)
    archiginnasio.borrow_book(giancarlo, steppenwolf)
    archiginnasio.borrow_book(giancarlo, sotto_le_cuffie)
    archiginnasio.borrow_book(giancarlo, principles)
    print(archiginnasio)
    archiginnasio.return_book(giancarlo, sotto_le_cuffie)
    archiginnasio.borrow_book(gianpiero, sotto_le_cuffie)
    print(archiginnasio)
    print(Library.library_statistics())