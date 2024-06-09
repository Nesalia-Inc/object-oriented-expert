

""" 

La solution à ce problème s'appelle l'héritage. Ce concept va nous permettre de prendre une classe
et lui ajouter toutes les fonctionnalités d'une autre classe. La classe qui possède ces fonctionnalités 
est la classe mère. La classe qui obtient ces nouvelles fonctionnalités est la classe fille. 

"""


# On a pris toutes les fonctionnalités communes à tous les animaux 
# et on les a mises dans une classe appelée `Animal`. Cette classe
# est notre classe mère. 

# Il est possible d'initialiser un animal directement. Tu verras 
# dans la troisième partie comme pousser cette classe encore plus 
# loin pour la rendre abstraite.
class Animal:
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



# En utilisant la syntaxe `ClasseFille(ClasseMere)` on crée un héritage direct
# de la classe fille vers la classe mère. Ici, on peut considérer que la classe Chien 
# est exactement la même que dans le code initial. On lui a donner toutes les méthodes
# et attributs de la classe mère. 

# Ca veut donc dire qu'il n'est pas nécessaire de redéfinir le constructeur dans la classe 
# fille puisqu'il existe déjà dans la classe mère. 
class Chien(Animal):
    
    # Comme tu peux le voir, il n'est pas possible de mettre dans la classe mère 
    # cette méthode puisque son implémentation est différente pour chaque classe 
    # fille. C'est con parce qu'on aimerait définir que toutes les classes filles possèdent
    # une méthode bruit directement depuis la classe mère sans pour autant définir une implémentation. 
    
    # C'est ce que tu vas voir juste après avec les méthodes abstraites 
    def bruit(self) -> None:
        print("Woof")


# Le fonctionnement est exactement le même pour la classe du Chat. 
class Chat(Animal):
    def bruit(self) -> None:
        print("Miaou")


# Quelque chose qu'il faut comprendre avec l'héritage est que la classe fille est du même type que la classe mère. 
# Ca veut donc dire que pour le code, un Chien est de type Chien ET Animal. Il est donc possible d'avoir en annotation
# Uniquement un Animal sans qu'il y ait d'erreurs. 
def afficher_animal(animal : Animal) -> None:
    print(f"Je suis un {type(animal).__name__}, je m'appelle {animal.nom}, j'ai {animal.age} ans et je pèse {animal.poids}kg")


if __name__ == '__main__':
    # Ici, le code ne change pas du tout donc on est content 
    chien = Chien("Médor", 4, 12)
    chat = Chat("Garfield", 8, 3.2)
    
    chat.grossir(0.4)
    chien.maigrir(1.6)
    chien.grandir()
    
    afficher_animal(chien)
    afficher_animal(chat)
    
    chien.bruit()
    chat.bruit()
    