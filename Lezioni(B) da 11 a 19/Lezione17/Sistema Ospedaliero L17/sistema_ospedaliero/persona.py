class Persona: 
    def __init__(self, first_name:str, last_name:str) -> None:
        
        if isinstance(first_name, str):
            self._first_name = first_name
        else:
            print("Il nome inserito non è una stringa!")
            self._first_name = None
        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            print("Il cognome inserito non è una stringa!")
            self._last_name = None

        if isinstance(first_name, str)\
        and isinstance(last_name, str):
            self._age = 0
        else:
            self._age = None
            
    def setName(self, first_name) -> None:
        if isinstance(first_name, str):
            self._first_name = first_name
        else:
            print("Il nome inserito non è una stringa!")
            self._first_name = None

    def setLastName(self, last_name) -> None:
        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            print("Il cognome inserito non è una stringa!")
            self._last_name = None

    def setAge(self, age) -> None:
        if isinstance(age, int):
            self._age = age
        else:
            print("Il età deve essre un numero intero!")
            self._age = None

    def getName(self) -> str:
        return self._first_name
    
    def getLastName(self) -> str:
        return self._last_name
    
    def getAge(self) -> int:
        return self._age
    
    def greet(self) -> str:
        return f"Ciao, sono {self._first_name} {self._last_name}! Ho {self._age} anni!"