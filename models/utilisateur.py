from database.db import db
from tinydb import Query


class Utilisateur:
    def __init__(self, nom:str, email:str, mdp:str, role:str)->None:
        self._nom = nom
        self._email = email
        self._mdp = mdp
        self._role = role

    @property
    def nom(self)->str:
        return self._nom
    @nom.setter
    def nom(self, nom:str)->None:
        self._nom = nom

    @property
    def email(self)->str:
        return self._email
    @email.setter
    def email(self, email:str)->None:
        self._email = email

    @property
    def mdp(self)->str:
        return self._mdp
    @mdp.setter
    def mdp(self, mdp:str)->None:
        self._mdp = mdp

    @property
    def role(self)->str:
        return self._role
    @role.setter
    def role(self, role:str)->None:
        self._role = role

    def sauvegarder(self):
        table_utilisateur = db.table("utilisateur")
        table_utilisateur.insert({
            "nom": self._nom,
            "email": self._email,
            "mdp": self._mdp,
            "role": self._role
        })
    @staticmethod
    def trouver_par_email(email:str)->"Utilisateur":
        table_utilisateur = db.table("utilisateur")
        User = Query()
        return table_utilisateur.get(User.email==email)
    



