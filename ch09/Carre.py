from Rectangle import Rectangle

class Carre(Rectangle):


    def __init__(self, cote) -> None:
        super().__init__(cote, cote)
        print(f"def __init__(self, {cote})")
        self._cote = cote
    
    @property
    def cote(self):
        return self._cote
    
    @cote.setter
    def cote(self,cote):
        self.longueur = cote
        self.largeur = cote

        self._cote = cote
    

    def __str__(self):
        return f"{__class__.__name__} cote : {self._cote}"
