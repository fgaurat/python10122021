from ICalcGeo import ICalcGeo 



class Rectangle(ICalcGeo):
    
    _cpt=0

    def __init__(self,longueur,largeur) -> None:
        print(f"def __init__(self,{longueur},{largeur})")
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._cpt+=1

    def get_cpt():
        return Rectangle._cpt

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur

    @property
    def largeur(self):
        return self._largeur
    
    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur

    @property
    def surface(self):
        return self._longueur*self._largeur
    
    def __del__(self):
        print("def __del__(self)")
    
    def __eq__(self, __o: object) -> bool:
        # r = True if self._longueur == __o.longueur and self._largeur == __o.largeur() else False
        return self.longueur == __o.longueur and self.largeur == __o.largeur
    
    def __str__(self):
        return f"{__class__.__name__} longueur : {self._longueur}, largeur : {self._largeur}"

