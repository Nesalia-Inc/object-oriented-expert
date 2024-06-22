

class MaClasse:
    def __init__(self) -> None:
        self.publique = 1
        self._protege = 2
        self.__prive = 3
        
    
    def methode_publique(self) -> None:
        print("Je suis une méthode publique")
        
    def _methode_protegee(self) -> None:
        print("Je suis une méthode protégée")
        
    def __methode_privee(self) -> None:
        print("Je suis une méthode privée")
        
        
    def methode(self) -> None:
        self._methode_protegee()
        self.__methode_privee()
        
        
class ClassFille(MaClasse):
    def methode_fille(self) -> None:
        super()._methode_protegee()
        
        
        

if __name__ == '__main__':
    fille = ClassFille()
    fille.methode_fille()
    
    mere = MaClasse()
    mere._methode_protegee() # Ca marche... 