#Giovanni di Giuseppe, 08/05/20247

"""
When multiplying floats round by 3.
"""

class Zoo:
    def __init__(self, fences:list, zoo_keepers:list):
        self.fences = fences
        self.zoo_keeper = zoo_keepers

    def describe_zoo(self):
        pass

class Animal:
    def __init__(self, name:str, species:str, age:int,
                 height:float, width:float, preferred_habitat:str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health:float = round(100*(1/age), 3)

class Fence:
    def __init__(self, area:float, temperature:int, habitat:str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat

class ZooKeeper:
    def __init__(self, name:str, surname:str, id:str):
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal:Animal, fence:Fence):
        pass

    def remove_animal(self, animal:Animal, fence:Fence):
        pass

    def feed(self, animal:Animal):
        pass

    def clean(self, fence:Fence):
        pass