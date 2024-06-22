import re



class Personne:
    def __init__(self, nom : str, prenom : str, adresse : str) -> None:
        self.__nom = nom 
        self.__prenom = prenom 
        self.adresse = adresse
        
    @property
    def nom(self) -> str:
        return self.__nom
    
    @property
    def prenom(self) -> str:
        return self.__prenom
    


class Compte:
    def __init__(self, email : str, password : str) -> None:
        self.__email = email 
        self.__password = password


    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter 
    def email(self, nouvel_email : str) -> None:
        if not self.__is_email_valide(nouvel_email):
            raise ValueError("L'adresse email est invalide")
            
        self.email = nouvel_email
        
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, nouveau_password : str) -> None:
        if not self.__is_password_valid(nouveau_password):
            raise ValueError("Le mot de passe est invalide")
        
        self.__password = nouveau_password
        
    
    @classmethod
    def __is_password_valid(cls, password : str) -> bool:
        CHECK = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        
        if re.match(CHECK, password):
            return True 
        return False
        
    
    @classmethod
    def __is_email_valide(cls, email : str) -> bool:
        CHECK = r'^[\w\.-]+@[\w\.-]+\.[\w-]{2,4}$'
        
        if re.match(CHECK, email):
            return True 
        return False
    
    
    @classmethod
    def create(cls, email : str, password : str) -> "Compte":
        if not cls.__is_email_valide(email):
            raise ValueError("L'adresse email est invalide")
        
        if not cls.__is_password_valid(password):
            raise ValueError("Le mot de passe est incorrect")
        
        return cls(email, password)




class Utilisateur:
    def __init__(self, personne : Personne, compte : Compte) -> None:
        self.__personne = personne
        self.__compte = compte
    
    @property
    def nom(self) -> str:
        return self.__personne.nom
    
    @property
    def prenom(self) -> str:
        return self.__personne.prenom
    
    @property
    def adresse(self) -> str:
        return self.__personne.adresse
    
    @property
    def email(self) -> str:
        return self.__compte.email
    
    @email.setter 
    def email(self, nouvel_email : str) -> None:
        self.__compte.email = nouvel_email
        
    @property
    def password(self) -> str:
        return self.__compte.password
    
    @password.setter
    def password(self, nouveau_password : str) -> None:
        self.__compte.password = nouveau_password
        


if __name__ == '__main__':
    utilisateur = Utilisateur(
        Personne("Doe", "Jean", "15 Rue des Rois"),
        Compte("jean@gmail.com", "jean1234!")
    )
    
    

    print(utilisateur.email)