class Film:
    def __init__(self, id:int, title:str) -> None:
        self._id = id
        self._title = title

    def setID(self, id:int) -> None:
        self._id = id

    def setTitle(self, title:str) -> None:
        self._title = title

    def getID(self) -> int:
        return self._id
    
    def getTitle(self) -> str:
        return self._title
    
    def isEqual(self, otherFilm:"Film") -> bool:
        if self._id == otherFilm._id:
            return True
        else:
            return False
