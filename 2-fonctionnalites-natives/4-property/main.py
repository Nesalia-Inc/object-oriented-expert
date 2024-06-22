



class Rectangle:
    def __init__(self, longueur : int, largeur : int) -> None:
        self.longueur = longueur
        self.largeur = largeur
        
        
    @property
    def aire(self) -> int:
        return self.longueur * self.largeur
    
    
    
if __name__ == '__main__':
    rect = Rectangle(10, 5)
    
    print("Avant modification : ", rect.aire)
    
    rect.largeur = 10
    
    print("Après modifications", rect.aire)