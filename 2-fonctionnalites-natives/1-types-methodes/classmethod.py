


class Personne:
    def __init__(self, nom : str, age : int) -> None:
        self.nom = nom 
        self.age = age 
        
    
    def afficher_informations(self) -> None:
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")
        
        
    @classmethod
    def verifier_attributs(cls, nom : str, age : int) -> bool:
        return len(nom) <= 1 or age <= 0
        
    
    @classmethod
    def creer(cls, nom : str, age : int) -> "Personne":
        if not cls.verifier_attributs(nom, age):
            raise ValueError("Un des attributs n'est pas correct") 
        
        return cls(nom, age) 
    
    
    
