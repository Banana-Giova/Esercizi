from sistema_ospedaliero.dottore import Dottore
from sistema_ospedaliero.paziente import Paziente

class Fattura:
    def __init__(self, patients:list[Paziente], doctor:Dottore) -> None:
        
        doc_val:str = doctor.isAValidDoctor()
        if doc_val == f"Il dottor {doctor._first_name} {doctor._last_name} è valido!":
            self._doctor = doctor
            self._patients = patients
            self._bills:int = len(patients)
            self._salary:int = self._bills*self._doctor._parcel
        else:
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")
            self._doctor = None
            self._patients = None
            self._bills = None
            self._salary = None
    
    def getFatture(self) -> None:
        self._bills = len(self._patients)
        return self._bills
    
    def getSalary(self) -> None:
        self._salary = self.getFatture()*self._doctor._parcel
        return self._salary
    
    def addPatient(self, newPatient:Paziente) -> None:
        self._patients.append(newPatient)
        self.getSalary()
        print(f"Alla lista del Dottor {self._doctor._last_name} "
            + f"è stato aggiunto il paziente {newPatient._idCode}")

    def removePatient(self, idCode:str) -> None:
        target = ''
        for i in self._patients:
            if isinstance(i, Paziente) == True:
                if i._idCode == idCode:
                    target = i
        if target != '':
            self._patients.remove(target)
        self.getSalary()
        print(f"Dalla lista del Dottor {self._doctor._last_name} "
            + f"è stato rimosso il paziente {idCode}")