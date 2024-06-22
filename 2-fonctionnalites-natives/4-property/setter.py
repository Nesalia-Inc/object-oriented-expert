
class CompteBancaire:
    TAILLE_CODE = 4
    
    def __init__(self, code : str, argent_initial : float) -> None:
        self.__code = code 
        self.__argent = argent_initial
        
    
    @property
    def code(self) -> str:
        return self.__code
    
    @code.setter
    def code(self, nouveau_code : str) -> None:
        if len(nouveau_code) != CompteBancaire.TAILLE_CODE:
            raise ValueError("La taille du code est incorrecte")
        
        self.__code = nouveau_code
        
        
    @property
    def argent(self) -> float:
        return self.__argent
    
    @argent.setter
    def argent(self, nouvel_argent : float) -> None:
        if nouvel_argent < 0:
            raise ValueError("L'argent ne peut pas être négatif")
        
        self.__argent = nouvel_argent
        
        

if __name__ == '__main__':
    compte = CompteBancaire("1234", 0.0)
    
    compte.code = "5678"
    
    compte.argent += 100
    
    print(compte.code, compte.argent)