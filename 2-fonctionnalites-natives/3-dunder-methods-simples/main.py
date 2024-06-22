



class Utilisateur:
    def __init__(self, email : str, mot_de_passe : str) -> None:
        self.email = email 
        self.mot_de_passe = mot_de_passe
        
        
    def __str__(self) -> str:
        return f"Mon email est {self.email} et le mot de passe est {self.mot_de_passe}"
    
    def __repr__(self) -> str:
        return f"Utilisateur(email={self.email}, mot_de_passe={self.mot_de_passe})"
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Utilisateur):
            raise ValueError("On peut uniquement comparer deux utilisateurs entre eux")
        
        return self.email == value.email and self.mot_de_passe == value.mot_de_passe
    
    
if __name__ == '__main__':
    utilisateur1 = Utilisateur("jean@gmail.com", "1234")
    utilisateur2 = Utilisateur("jean@gmail.com", "1234")
    
    print(utilisateur1)
    print(repr(utilisateur1))
    
    print("Est-ce que les deux utilisateurs sont égaux :", utilisateur1 == utilisateur2)