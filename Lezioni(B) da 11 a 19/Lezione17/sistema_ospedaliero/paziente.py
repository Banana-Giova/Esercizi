from sistema_ospedaliero.persona import Persona

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str,
                 idCode:str) -> None:
        super().__init__(first_name, last_name)

        self._idCode = idCode

    def setIdCode(self, idCode:str) -> None:
        self._idCode = idCode

    def getidCode(self) -> str:
        return self._idCode
    
    def patientInfo(self) -> str:
        return f"Paziente: {self._first_name} {self._last_name}\nID: {self._idCode}"