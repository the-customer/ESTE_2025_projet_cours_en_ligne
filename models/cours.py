from database.db import db

class Cours:
    def __init__(self, titre:str, description:str, prix:int, professeur_email:str)->None:
        self.titre = titre
        self.description = description
        self.prix = prix
        self.professeur_email = professeur_email
        self.etudiants_inscrits = []


    def sauvegarder(self):
        table_cours = db.table('cours')
        table_cours.insert({
            'titre': self.titre,
            'description': self.description,
            'prix': self.prix,
            'professeur_email': self.professeur_email,
            'etudiants_inscrits': self.etudiants_inscrits
        })


