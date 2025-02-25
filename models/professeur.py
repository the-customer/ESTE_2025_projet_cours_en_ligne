from models.utilisateur import Utilisateur

class Professeur(Utilisateur):
    def __init__(self, nom:str, email:str, mdp:str)->None:
        super().__init__(nom, email, mdp, "professeur")