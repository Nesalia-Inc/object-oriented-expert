

class Animal:
    def __init__(self, nom : str, age : int) -> None:
        self.nom = nom 
        self.age = age 



if __name__ == '__main__':
    animal = Animal("Médor", 4)
    animal2 = Animal("Garfield", 6)
    
    
    print(animal.age)
    
    animal.age = 5
    
    print(animal.age)
    print(animal2.age)
    