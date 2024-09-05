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

if False:
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

#Esercizio 3

if False:
    class Animal:
        def __init__(self, name:str, legs:int=0):
            self.name = name
            self.setLegs(legs)

        def __str__(self):
            return f"{self.name}, Legs => {self.legs}"
        
        def setLegs(self, legs:int):
            if legs >= 0:
                self.legs = legs
            else:
                self.legs = 0
        
        def getLegs(self):
            return self.legs

    cat = Animal("Ciccio")
    spider = Animal("Carlo")

    print(cat.name)
    print(spider.name)

    print(spider.legs)
    spider.legs = 8
    print(spider.legs)

    spider.setLegs(7)
    print(spider.getLegs())

    print(spider.__str__())

#Esercizio 4

class Food:
    def __init__(self, name:str, price:float=0.0, 
                 description:str=""):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return (f"{self.name}, {self.price}, {self.description}")


ragù = Food("Pasta al Ragù", 10.7, 
            "Pasta con sugo di pomodoro e carne")
carbonara = Food("Pasta alla Carbonara", 11.2,
                 "Pasta con uova, guanciale, pecorino e pepe")
forno = Food("Pasta al Forno", 13.0,
                 "Pasta con condimenti variabili, cotta al forno")
print(ragù)

class Menu:
    def __init__(self, FoodsList:list=[]):
        self.FoodsList = FoodsList
    
    def addFood(self, new_food:Food):
        self.FoodsList.append(new_food)

    def removeFood(self, re_food:Food):
        if re_food in self.FoodsList:
            self.FoodsList.remove(re_food)

    def printPrices(self, FoodsList:list):
        avg:float = 0.0
        for i in FoodsList:
            avg += i.price
        avg = avg/len(FoodsList)
        return avg

    def __str__(self):
        repr:str = ''
        for i in self.FoodsList:
            repr += "\n" + i.__str__()
        return repr

osteria_del_sium = Menu()
osteria_del_sium.addFood(ragù)
osteria_del_sium.addFood(carbonara)
osteria_del_sium.addFood(forno)

print(osteria_del_sium)
print(osteria_del_sium.printPrices())