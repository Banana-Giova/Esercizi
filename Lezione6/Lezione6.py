#Intro

if False:
    class Person:
        # - name
        # -surname
        # -age
        def __init__(self, name:str,\
                    surname:str, age:int):
            self.name = name
            self.surname = surname
            self.age = age

    lorenzo = Person("Lorenzo", "Maggi", 24)

    print(lorenzo.name, lorenzo.surname, lorenzo.age)

#Esercizio 1

if False:
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    alice = Person("Alice W.", 45)
    bob = Person("Bob M.", 36)

    print(bob.age)

    if bob.age > alice.age:
        print(bob.age)
    else:
        print(alice.age)

    andrea = Person("Andrea P.", 20)
    manuel = Person("Manuel I.", 61)
    michele = Person("Michele Badassium", 21)

    people:list[Person] = [alice, bob, andrea,\
                        manuel, michele]

    youngest:None = None
    for i in people:
        if youngest == None:
            youngest = i.age
        else:
            if youngest > i.age:
                youngest = i.age

    print(youngest)

#Esercizio 3

class Student:
    def __init__(self, name:str, studyProgram:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age:str = "not specified"
        self.gender:str = "not specified"

    def printInfo(self):
        return f"{self.name} is studying {self.studyProgram} "\
               f"their age is {self.age} and his gender is {self.gender}"
    
    def add_age(self, age:int):
        self.age = age

    def add_gender(self, gender:str):
        self.gender = gender
    
manuel = Student("Manuel I.", "Fullstack Dev")
giovanni = Student("Giovanni d.G.", "Fullstack Dev")
markiyan = Student("Markiyan S.", "Fullstack Dev")

print(manuel.printInfo())

manuel.add_gender("M")
giovanni.add_age(21)

print(manuel.printInfo())
print(giovanni.printInfo())