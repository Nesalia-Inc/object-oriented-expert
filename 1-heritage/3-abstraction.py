from abc import ABC, abstractmethod

""" 

Un animal est un concept abstrait, on ne peut pas directement définir un animal dans le monde réel. 
On représente toujours un animal avec quelque chose de concret. Un chat ou un chien est un animal. 
Un animal seul n'est rien. 

Une représentation abstraite contient uniquement des caractéristiques communes entre toutes les
implémentations concrètes. Tous les animaux grandissent, perdent ou prennent du poids et font du bruit. 

Certaines caractéristiques sont communes à tous les animaux dans leurs implémentations. Tous les animaux grandissent 
d'une année chaque année et finissent par mourir à un moment. Malgré tout, il y des éléments communs 
qui n'ont pas les mêmes implémentations. Un exemple est que chaque animal possède un bruit
mais chaque type d'animal possède un bruit unique. 

Quand on a une représentation abstraite comme pour notre animal, on va créer ce que l'on appelle une classe abstraite. 
C'est une classe qui est uniquement là pour servir de classe mère pour chaque implémentation concrète. 

Ce n'est pas parce qu'une classe est abstraite qu'elle ne peut pas définir des éléments concrets. Comme je l'ai dit, il y a des caractéristiques 
qui sont identiques pour chaque animal. 

"""


# Pour définir qu'une classe est abstraite, on va la faire hériter de la classe
# ABC qui vient du module abc. On a rien de plus à faire pour définir qu'elle est abstraite. 
class Animal(ABC):
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
        
    # Une classe abstraite possède des méthodes abstraites
    # Si ce n'est pas le cas, elle n'est pas abstraite, c'est une classe concrète. 
    # Pour créer une méthode abstraite, on va utiliser le décorateur `@abstractmethod`
    # Qui vient aussi du module abc. On implémente pas cette fonction, on lui mets uniquement 
    # un pass. 
    @abstractmethod
    def bruit(self) -> None:
        pass 


class Chien(Animal):
    # Chaque implémentation concrète de la classe abstraite 
    # doit implémenter toutes les méthodes abstraites de la classe mère. 
    # Si ce n'est pas le cas, une erreur sera renvoyée. 
    # Ici, on a rien de spécial à faire. 
    def bruit(self) -> None:
        print("Woof")


class Chat(Animal):
    def bruit(self) -> None:
        print("Miaou")


def afficher_animal(animal : Animal) -> None:
    # Désormais, cette fonction est consciente que chaque animal possède une méthode bruit, il n'est pas conscient 
    # que c'est une méthode abstraite mais ça ne pose aucun problème puisqu'on va uniquement lui mettre
    # en paramètre des implémentations concrètes qui possèdent une implémentation de cette méthode abstraite. 
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
    