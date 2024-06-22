from enum import Enum, auto 


class Couleur(Enum):
    ROUGE = (255, 0, 0)
    VERT = (0, 255, 0)
    BLEU = (0, 0, 255)
    
    
    @classmethod
    def from_value(cls, value : tuple[int, int, int]) -> "Couleur":
        for couleur in cls:
            if couleur.value == value:
                return couleur
        raise ValueError(f"{value} n'est pas une valeur valide pour {cls.__name__}")
        
        
        
class Permission(Enum):
    ADMINISTRATEUR = auto()
    MODERATEUR = auto()
    MESSAGES = auto()
        
        
        
if __name__ == '__main__':
    print(Couleur.from_value((255, 0, 0)))
    
    