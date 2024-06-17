from sistema_ospedaliero.persona import Persona

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str,
                 specialization:str, parcel:float) -> None:
        super().__init__(first_name, last_name)
        
        if isinstance(specialization, str):
            self._specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")
            self._specialization = None
        if isinstance(parcel, float):
            self._parcel = parcel
        else:
            print("La parcella inserita non è un float!")
            self._parcel = None

    def setSpecialization(self, specialization:str) -> None:
        if isinstance(specialization, str):
            self._specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")
            self._specialization = None

    def setParcel(self, parcel:float) -> None:
        if isinstance(parcel, float):
            self._parcel = parcel
        else:
            print("La parcella inserita non è un float!")
            self._parcel = None


    def getSpecialization(self) -> str:
        return self._specialization
    
    def getParcel(self) -> float:
        return self._parcel
    
    def isAValidDoctor(self):
        if self._age > 30:
            return f"Il dottor {self._first_name} {self._last_name} è valido!"
        else:
            return f"Il dottor {self._first_name} {self._last_name} non è valido!"
        
    def doctorGreet(self) -> str:
        return super().greet() + f" Sono un medico {self._specialization}."