#Esercizio 1

class Contatore:
    def __init__(self) -> None:
        self.conteggio = 0

    def setZero(self) -> None:
        self.conteggio = 0

    def add1(self) -> None:
        self.conteggio += 1

    def sub1(self) -> None:
        if self.conteggio != 0:
            self.conteggio -= 1
        else:
            print("Non è possibile eseguire la sottrazione")
        
    def get(self) -> str:
        return self.conteggio
    
    def mostra(self):
        print(f"Conteggio attuale: {self.conteggio}")

#Esercizio 2

class RecipeManager:
    def __init__(self) -> None:
        self.recipe_book = {}
    
    def create_recipe(self, name:str, 
                      ingredients:list[str]) -> dict[str, list[str]]:
        if name not in self.recipe_book:
            self.recipe_book[name] = ingredients

        return self.recipe_book

    def add_ingredient(self, recipe_name:str, 
                       ingredient:str) -> dict[str, list[str]]:
        if recipe_name in self.recipe_book:
            self.recipe_book[recipe_name].append(ingredient)
        else:
            return "Sium"
        
        return self.recipe_book

    def remove_ingredient(self, recipe_name:str, 
                          ingredient:str) -> dict[str, list[str]]:
        if recipe_name in self.recipe_book:
            try:
                self.recipe_book[recipe_name].remove(ingredient)
            except Exception:
                return "Sium"
        else:
            return "Sium"

        return self.recipe_book

    def update_ingredient(self, recipe_name:str, old_ingredient:str,
                          new_ingredient:str) -> dict[str, list[str]]:
        if recipe_name in self.recipe_book:
            i = 0
            while i < len(self.recipe_book[recipe_name]):
                if self.recipe_book[recipe_name][i] == old_ingredient:
                    self.recipe_book[recipe_name][i] = new_ingredient
                i += 1
        else:
            return "Sium"

        return self.recipe_book
    
    def list_recipes(self) -> list[str]:
        result:list[str] = []
        for ki in self.recipe_book.keys():
            result.append(ki)
        
        return result
    
    def list_ingredients(self, recipe_name:str) -> list[str]:
        if recipe_name in self.recipe_book:
            return self.recipe_book[recipe_name]
        else:
            return "Sium"
        
    def search_recipe_by_ingredient(self, ingredient:str) -> list[str]:
        search_result:dict[str, list[str]] = {}
        for ki, vi in self.recipe_book.items():
            if ingredient in vi:
                search_result[ki] = vi
        
        return search_result
    
#Esercizio 3

class Veicolo:
    def __init__(self, marca:str, modello:str,
                 anno:int) -> None:
        self.marca = marca
        self.modello = modello
        self.anno = anno
    
    def descrivi_veicolo(self) -> str:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}")
    
class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, 
                 anno: int, numero_porte:int) -> None:
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrivi_veicolo(self) -> str:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Numero di porte: {self.numero_porte}")

class Moto(Veicolo):
    def __init__(self, marca: str, modello: str, 
                 anno: int, tipo:int) -> None:
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrivi_veicolo(self) -> str:
        print(f"Marca: {self.marca}, Modello: {self.modello}, Anno: {self.anno}, Tipo: {self.tipo}")

#Esercizio 4

class Specie:
    def __init__(self, nome:str, popolazione:int,
                 tasso_crescita:float) -> None:
        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita

    def cresci(self):
        self.popolazione *= (1.00+(self.tasso_crescita/100))

    def anni_per_superare(self, altra_specie:'Specie') -> int:
        pass