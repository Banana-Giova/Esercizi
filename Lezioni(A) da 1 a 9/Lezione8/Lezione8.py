"""
Exercise 1: Creating an Abstract Class with Abstract Methods

Create an abstract class Shape with an abstract method area 
and another abstract method perimeter. 
Then, create two subclasses Circle and Rectangle 
that implement the area and perimeter methods.
"""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def area():
        pass

    def perimeter():
        pass

class Rectangle(Shape):
    def __init__(self, base:float, height:float) -> None:
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height
    
    def perimeter(self):
        return 2*(self.base + self.height)
    
class Circle(Shape):
    def __init__(self, ray:float) -> None:
        super().__init__()
        self.ray = ray

    def area(self):
        return pi*self.ray**2
    
    def perimeter(self):
        return 2*pi*self.ray
    
rectus:Rectangle = Rectangle(base=34, height=22)
circus:Circle = Circle(ray=16)

if False:
    print(rectus.area())
    print(rectus.perimeter())
    print(circus.area())
    print(circus.perimeter())

"""
Exercise 2: Implementing Static Methods

Create a class MathOperations with a static method add that takes two numbers 
and returns their sum, and another static method multiply that takes two numbers 
and returns their product.
"""

class MathOperations:

    def sum(x:float, y:float):
        return x+y
    
    def mult(x:float, y:float):
        return x*y

if False:
    print(MathOperations.sum(21, 19))
    print(MathOperations.mult(21, 19))

"""
Exercise 3: Library Management System 

Create a Book class containing the following attributes: title, author, isbn
The book class must contains the following methods:

    __str__ method to return a string representation of the book.

    @classmethod from_string(cls, book_str) to create a Book instance 
    from a string in the format "title, author, isbn". 
    It means that you must use the class reference cls 
    to create a new object of the Book class using a string.
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
        return f"Title: {self.title}, Author: {self.author} "\
            +  f"ISBN: {self.isbn}"

class Member:
    def __init__(self, member_id:str, name:str, 
                 borrowed_books:list=[]) -> None:
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
        return f"Name: {self.name}, Member ID: {self.member_id} "\
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
        to_print:str = "- Books\n"
        for i in self.books.values():
            to_print += i.__str__() + "\n"
        to_print += "\n- Members\n"
        for i in self.members.values():
            to_print += i.__str__() + "\n"
        return to_print



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
archiginnasio.return_book(gianpiero, steppenwolf)
print(archiginnasio)