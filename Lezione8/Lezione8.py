class Animal:
    def __init__(self, specie:str, età:int) -> None:
        self.specie = specie
        self.età = età

    def __str__(self):
        return f"{self.__class__.__name__}, specie={self.specie}, età={self.età}"

class Person(Animal):
    def __init__(self, età: int, nome:str, 
                 cognome:str, cf:str) -> None:
        super().__init__("Homo Sapiens", età)
        self.età = età
        self.nome = nome
        self.cognome = cognome
        self.cf = cf

    def __str__(self):
        return super().__str__()\
        + f", nome={self.nome}, cognome={self.cognome} "\
        + f"cf={self.cf}"

class Student(Person):
    def __init__(self, età: int, nome: str, cognome:str,
                 cf: str, n_matricola:int) -> None:
        super().__init__(età, nome, cognome, cf)
        self.n_matricola = n_matricola
    
    def __str__(self):
        return super().__str__()\
        + f", n_matricola={self.n_matricola} "

class Cat(Animal):
    def __init__(self, età: int, nome:str, 
                 cat_id:str) -> None:
        super().__init__("Felis Silvestris Catus", età)
        self.nome = nome
        self.cat_id = cat_id

    def __str__(self):
        return super().__str__()\
        + f", nome={self.nome}, cat ID={self.cat_id}"

class Rabbit(Animal):
    def __init__(self, età: int, nome:str, 
                 rab_id:str) -> None:
        super().__init__("Oryctolagus Cuniculus", età)
        self.nome = nome
        self.rab_id = rab_id

    def __str__(self):
        return super().__str__()\
        + f", nome={self.nome}, rab ID={self.rab_id}"



giovanni:Student = Student(nome="Giovanni",
                           cognome="di Giuseppe",
                           età=21,
                           cf="F1TT1Z10",
                           n_matricola=420)

print(giovanni)

isa:Cat = Cat(nome="Isa",
              età=5,
              cat_id="M3G451UM")

print(isa)