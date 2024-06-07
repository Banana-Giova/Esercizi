#Giovanni di Giuseppe, 08-16/05/2024



class Zoo:
    def __init__(self, fences:list=[], zoo_keepers:list=[]) -> None:

        self.fences = fences
        self.zoo_keepers = zoo_keepers


    def describe_zoo(self) -> str:
        
        print(f"Guardians:")
        if len(self.zoo_keepers) > 0:
          for keeper in self.zoo_keepers:
              print(f"\nZooKeeper(name={keeper.name}, "\
                + f"surname={keeper.surname}, id={keeper.id})")
            
        print("\nFences:")
        if len(self.fences) > 0:
          for fence in self.fences:
                print(f"\nFence(area={fence.area}, "\
                + f"temperature={fence.temperature}, habitat={fence.habitat})")
            
                if len(fence.animals) != 0:
                    print("\nwith animals:")

                    for animal in fence.animals:
                        print(f"\nAnimal(name={animal.name}, "\
                            f"species={animal.species}, age={animal.age})")
                    
                print("\n" + "#"*30)



class Animal:
    def __init__(self, name:str, species:str, age:int,
                 height:float, width:float, preferred_habitat:str) -> None:
        
        try:
            if height == None:
                height = 0
            elif height < 0:
                height = 0
        except TypeError or ValueError:
            height = 0

        try:
            if width == None:
                width = 0
            elif width < 0:
                width = 0
        except TypeError or ValueError:
            width = 0

        try:
            if age == None:
                age = 0.1
            elif age <= 0:
                age = 0.1
        except TypeError or ValueError:
            age = 0.1

        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.fence = None
        try:
            self.health:float = round(100*(1/age), 3)
        except Exception:
            self.health:float = 0.0
        try:
            self.area = height*width
        except Exception:
            self.area = 0

    def __str__(self) -> str:
        return f"Animal(name={self.name}, "\
             + f"species={self.species}, age={self.age}), "\
             + f"height={self.height}, width={self.width}, "\
             + f"preferred_habitat={self.preferred_habitat}"



class Fence:
    def __init__(self, area:float, temperature:float, habitat:str) -> None:

        try:
            if area == None:
                area = 0
            elif area < 0:
                area = 0
        except TypeError or ValueError:
            area = 0

        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
        self.og_area = area

    def __str__(self):
        to_print:str = ''
        to_print += f"Fence(area={self.area}, "\
                  + f"temperature={self.temperature}, habitat={self.habitat})"
            
        if len(self.animals) != 0:
            to_print += "\nwith animals:"

            for animal in self.animals:
                to_print += str(animal)
                
        return to_print



class ZooKeeper:
    def __init__(self, name:str, surname:str, id:str) -> None:

        self.name = name
        self.surname = surname
        self.id = id


    def add_animal(self, animal:Animal, fence:Fence) -> None:

        if animal.preferred_habitat == fence.habitat\
        and (animal.height*animal.width) <= fence.area\
        and animal.fence == None:
            
            fence.animals.append(animal)
            fence.area -= animal.area
            animal.fence = fence
                

    def remove_animal(self, animal:Animal, fence:Fence) -> None:

        if animal in fence.animals:
            fence.animals.remove(animal)
            fence.area += animal.area
            animal.fence = None


    def feed(self, animal:Animal) -> None:

        try:
            if animal.fence != None:
                try:
                    temp_area:float = animal.fence.area\
                                    - ((animal.area*1.04)-animal.area)
                except ZeroDivisionError:
                    temp_area:float = 0.0
                
                if temp_area >= 0:
                    animal_old_area = animal.area
                    animal.height *= 1.02
                    animal.width *= 1.02
                    animal.area = animal.height * animal.width
                    animal.fence.area -= animal.area - animal_old_area
                    animal.health *= 1.01
                    round(animal.health, 3)
        except Exception:
            pass


    def clean(self, fence:Fence) -> float:
        
        time_clean:float = 0.0
        if fence.area == 0 or fence.area == None:
            return fence.area
        else:
            time_clean = round((fence.og_area - fence.area)\
                               /fence.area, 3)
            return time_clean
        
    def __str__(self):
        return f"ZooKeeper(name={self.name}, "\
             + f"surname={self.surname}, id={self.id})"