from models.utilisateur import Utilisateur
from database.db import db

class Etudiant(Utilisateur):
    def __init__(self, nom:str, email:str, mdp:str)->None:
        super().__init__(nom, email, mdp, "etudiant")
        self.solde = 0

    def ajounter_solde(self, montant:int)->None:
        self.solde += montant
    
    def sauvegarder(self):
        table_utilisateur = db.table("utilisateur")
        table_utilisateur.insert({
            "nom": self._nom,
            "email": self._email,
            "mdp": self._mdp,
            "role": self._role,
            "solde": self.solde
        })