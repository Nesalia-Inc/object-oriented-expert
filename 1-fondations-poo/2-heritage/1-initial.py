

""" 

On cherche à représenter un système d'animaux. Tu peux voir que l'on a deux classes
qui représente un chien et un chat. Le problème est que ces deux classes sont quasiment
identiques, la seule différence est dans la méthode `bruit` qui affiche une valeur différente
pour chaque animal. 

Ici, ça n'est pas une catastrophe parce qu'il y a uniquement deux types d'animaux mais que 
se passerait t-il s'il y en avait +10 par exemple ? Ca serait absolument illisble. On veut donc 
trouver une solution pour regrouper toutes les fonctionnalités communes dans une classe et partager 
ces fonctionnalités dans chaque classe d'animal. 

"""


class Chien:
    def __init__(self, nom : str, age : int, poids : float) -> None:
        self.nom = nom 
        self.age = age 
        self.poids = poids 


    def grandir(self) -> None:
        self.age += 1 

    def grossir(self, kilos : float) -> None:
        self.poids += kilos 

    def maigrir(self, kilos : float) -> None:
        self.poids -= kilos
        
    def bruit(self) -> None:
        print("Woof")


class Chat:
    def __init__(self, nom : str, age : int, poids : float) -> None:
        self.nom = nom 
        self.age = age 
        self.poids = poids 


    def grandir(self) -> None:
        self.age += 1 

    def grossir(self, kilos : float) -> None:
        self.poids += kilos 

    def maigrir(self, kilos : float) -> None:
        self.poids -= kilos

    def bruit(self) -> None:
        print("Miaou")



# Cette fonction cherche à afficher des informations sur un animal
# Cette fonction peut donc prendre en paramètre soit un chien soit un chat. 

# Le problème avec cette fonction est que son annotation serait beaucoup trop grande
# Si on avait d'autres types d'animaux. On aimerait avoir une classe commune qui représente tous les animaux
def afficher_animal(animal : Chien | Chat) -> None:
    print(f"Je suis un {type(animal).__name__}, je m'appelle {animal.nom}, j'ai {animal.age} ans et je pèse {animal.poids}kg")


if __name__ == '__main__':
    chien = Chien("Médor", 4, 12)
    chat = Chat("Garfield", 8, 3.2)
    
    chat.grossir(0.4)
    chien.maigrir(1.6)
    chien.grandir()
    
    afficher_animal(chien)
    afficher_animal(chat)
    
    chien.bruit()
    chat.bruit()
    