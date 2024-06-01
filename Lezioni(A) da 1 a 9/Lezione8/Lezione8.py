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

if False:
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



"""
Exercise 4: University Management System


Create a system to manage a university with departments, 
courses, professors, and students. 

Create an abstract class Person:
Attributes:

    name (string)
    age (int)

Methods:

    __init__ method to initialize the attributes.
    Abstract method get_role to be implemented by subclasses.
    __str__ method to return a string representation of the person.

Create subclasses Student and Professor that inherit from Person 
and implement the abstract methods:

Student:
Additional attributes: student_id (string), courses (list of Course instances)
Method enroll(course) to enroll the student in a course.
Professor:
Additional attributes: professor_id (string), department (string), 
courses (list of Course instances)
Method assign_to_course(course) to assign the professor to a course.


Create a class Course:
Attributes:

    course_name (string)
    course_code (string)
    students (list of Student instances)
    professor (Professor instance)

Methods:

    __init__ method to initialize the attributes.
    add_student(student) to add a student to the course.
    set_professor(professor) to set the professor for the course.
    __str__ method to return a string representation of the course.

Create a class Department:

Attributes:

    department_name (string)
    courses (list of Course instances)
    professors (list of Professor instances)


Methods:

    __init__ method to initialize the attributes.
    add_course(course) to add a course to the department.
    add_professor(professor) to add a professor to the department.
    __str__ method to return a string representation of the department.

Create a class University:

Attributes:

    name (string)
    departments (list of Department instances)
    students (list of Student instances)


Methods:

    __init__ method to initialize the attributes.
    add_department(department) to add a department to the university.
    add_student(student) to add a student to the university.
    __str__ method to return a string representation of the university.


Create a script:

Create instances of departments, courses, professors, and students.
Add them to the university.
Enroll students in courses and assign professors to courses.
Display the state of the university.
"""
class Course:
    pass

class Person(ABC):
    @abstractmethod
    def __init__(self, name:str, age:int) -> None:
        super().__init__()
        self.name = name
        self.age = age
    
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

class Student(Person):
    def __init__(self, name: str, age: int,
                 student_id:str) -> None:
        super().__init__(name, age)
        self.student_id = student_id
        self.courses:list[Course] = []

    def enroll(self, course:Course) -> None:
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)

    def __str__(self) -> str:
        to_print:str = ""
        to_print += f"Name: {self.name}, Age: {self.age}, "\
                  + f"ID: {self.student_id}, Courses:\n"
        for i in self.courses:
            to_print += f"{i.course_name}\n"
        to_print += "\n"
        return to_print


    def get_role(self) -> str:
        return f"{self.name} is a student."

class Professor(Person):
    def __init__(self, name: str, age: int,
                 professor_id:str) -> None:
        super().__init__(name, age)
        self.professor_id = professor_id
        self.department:str = ''
        self.courses:list[Course] = []

    def assing_to_course(self, course:Course) -> None:
        if course not in self.courses:
            self.courses.append(course)
        course.set_professor(self)

    def __str__(self) -> str:
        to_print:str = ""
        to_print += f"Name: {self.name}, Age: {self.age}, "\
                  + f"ID: {self.professor_id}"
        return to_print

    def get_role(self) -> str:
        return f"{self.name} is a professor."

class Course:
    def __init__(self, course_name:str, 
                 course_code:str) -> None:
        self.course_name = course_name
        self.course_code = course_code
        self.students:list[Student] = []
        self.professor:Professor = None

        self.department:None = None

    def add_student(self, student:Student) -> None:
        if student not in self.students:
            self.students.append(student)
        if self.department != None:
            if self.department.university != None:
                self.department.university.add_student(student)


    def set_professor(self, professor:Professor) -> None:
        self.professor = professor
        if self.department != None:
            self.department.add_professor(professor)

    def __str__(self) -> str:
        to_print:str = ''
        to_print += f"Course Name: {self.course_name}, Code: {self.course_code}\n"\
                  + f"Professor's {self.professor.__str__()} \nStudents:\n\n"
        for i in self.students:
            to_print += f" {i.__str__()}"
        to_print = to_print[:-1]
        return to_print
        
class Department:
    def __init__(self, department_name:str) -> None:
        self.department_name = department_name
        self.courses:list[Course] = []
        self.professors:list[Professor] = []

        self.university:None = None

    def add_course(self, course:Course) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def add_professor(self, professor:Professor) -> None:
        if professor not in self.professors:
            self.professors.append(professor)
            professor.department = self.department_name

    def __str__(self) -> str:
        to_print:str = ''
        to_print += f"Department Name: {self.department_name}\n\nCourses:\n"
        for i in self.courses:
            to_print += f" {i.__str__()}"
        to_print = to_print[:-1]
        return to_print
    
class University:
    def __init__(self, name:str) -> None:
        self.name = name
        self.departments:list[Department] = []
        self.students:list[Student] = []

    def add_department(self, department:Department) -> None:
        if department not in self.departments:
            self.departments.append(department)
        department.university = self

    def add_student(self, student:Student) -> None:
        if student not in self.students:
            self.students.append(student)

    def __str__(self) -> str:
        to_print:str = ''
        to_print += f"University Name: {self.name}\n\nDepartments:\n"
        for i in self.departments:
            to_print += f" {i.__str__()}"
        to_print = to_print[:-1]
        return to_print
    


if True:
    nunzi:Student = Student(name="Nunzi Gippone", age=21,
                            student_id="NUNZ1")
    piero:Student = Student(name="Piero Roderikus",
                            age=25, student_id="P13R0")
    peppe:Student = Student(name="Giuseppino Maria Bertolli",
                            age=47, student_id="P3PP3")
    irene:Student = Student(name="Irene Piccoli",
                            age=24, student_id="1R3N3")
    frida:Student = Student(name="Frida Palo",
                            age=20, student_id="FR1D4")
    dario:Student = Student(name="Dario Goccia", age=31,
                            student_id="D4R10")
    mario:Student = Student(name="Mario Brons",
                            age=45, student_id="M4R10")
    maria:Student = Student(name="Maria Ausilia Trice",
                            age=41, student_id="M4R14")
    sonia:Student = Student(name="Sonia Cydonia",
                            age=26, student_id="50N14")
    sonic:Student = Student(name="Sonic De Egiog",
                            age=15, student_id="50N1C")
    kirby:Student = Student(name="Kirby Giacomini",
                            age=90, student_id="K1R81")
    zelda:Student = Student(name="Zelda De Gasperi",
                            age=19, student_id="Z3LD4")

    prof_smusi:Professor = Professor(name="Pietro Smusi",
                                    age=32, professor_id="5MU51")
    prof_tzio:Professor = Professor(name="Giuseppa Tzio Bertolli",
                                    age=74, professor_id="8ERT0")
    prof_scalchi:Professor = Professor(name="Bruno Scalchi",
                                    age=39, professor_id="5C4LC")
    prof_nhom_e:Professor = Professor(name="Nhom E. Feet Hizio",
                                    age=3, professor_id="NH0M3")
    prof_riopan:Professor = Professor(name="Rino Pane",
                                    age=66, professor_id="R10P4")
    prof_gaviscon:Professor = Professor(name="Gavino Sconi",
                                    age=66, professor_id="G4V15")

    maestria_nei_richiamo_dei_felini:Course = Course(course_name="Catcalling Expertise",
                                                    course_code="C4TC4")
    ludopatia_applicata:Course = Course(course_name="Applied Ludopathy", 
                                        course_code="4LUD0")
    analisi_ornitologica:Course = Course(course_name="Birdwatching",
                                        course_code="81RDW")
    piromanzia_uno:Course = Course(course_name="Pyromancy 1",
                                course_code="PYR01")
    piromanzia_due:Course = Course(course_name="Pyromancy 2",
                                course_code="PYR02")
    magia_nera_applicata:Course = Course(course_name="Applied Black Magic",
                                course_code="8L4CK")

    scienze_della_scomunicazione:Department = Department(department_name="Science Scomunication")
    analisi_della_maleducazione:Department = Department(department_name="Discortesy Analysis")

    università_della_follia:University = University(name="Università della Follia")



università_della_follia.add_department(scienze_della_scomunicazione)
università_della_follia.add_department(analisi_della_maleducazione)

analisi_della_maleducazione.add_course(maestria_nei_richiamo_dei_felini)
analisi_della_maleducazione.add_course(ludopatia_applicata)
analisi_della_maleducazione.add_course(analisi_ornitologica)
scienze_della_scomunicazione.add_course(piromanzia_uno)
scienze_della_scomunicazione.add_course(piromanzia_due)
scienze_della_scomunicazione.add_course(magia_nera_applicata)

prof_smusi.assing_to_course(analisi_ornitologica)
prof_tzio.assing_to_course(ludopatia_applicata)
prof_scalchi.assing_to_course(maestria_nei_richiamo_dei_felini)
prof_riopan.assing_to_course(magia_nera_applicata)
prof_gaviscon.assing_to_course(piromanzia_uno)
prof_gaviscon.assing_to_course(piromanzia_due)

nunzi.enroll(maestria_nei_richiamo_dei_felini)
nunzi.enroll(analisi_ornitologica)
piero.enroll(piromanzia_uno)
peppe.enroll(piromanzia_due)
irene.enroll(maestria_nei_richiamo_dei_felini)
irene.enroll(ludopatia_applicata)
irene.enroll(analisi_ornitologica)
irene.enroll(magia_nera_applicata)
frida.enroll(magia_nera_applicata)
dario.enroll(ludopatia_applicata)
dario.enroll(maestria_nei_richiamo_dei_felini)
dario.enroll(maestria_nei_richiamo_dei_felini)
mario.enroll(piromanzia_uno)
mario.enroll(piromanzia_due)
maria.enroll(magia_nera_applicata)
maria.enroll(magia_nera_applicata)
sonic.enroll(ludopatia_applicata)
sonic.enroll(piromanzia_due)
kirby.enroll(analisi_ornitologica)
zelda.enroll(magia_nera_applicata)

print(università_della_follia)