from tinydb import Query
from database.db import db

class CoursController:
    @staticmethod
    def afficher_cours_disponible():
        cours_table = db.table('cours')
        cours = cours_table.all()
        
        if not cours:
            print("Aucun cours disponible.")
            return None
        print("+++++++++++ Cours disponibles +++++++++++")
        for i,c in enumerate(cours,start=1):
            print(f"{i}. {c['title'].capitalize()} - {c['prix']} fcfa")
        return cours
    
    @staticmethod
    def inscrire_etudiant(email_etudiant):
        cours = CoursController.afficher_cours_disponible()
        if cours is None:
            return
        choix = int(input("Choisissez un cours (numéro) : ")) - 1
        if choix < 0 or choix >= len(cours):
            print("Choix invalide!")
            return
        cours_choisi = cours[choix]
        #
        if email_etudiant in cours_choisi["etudiants_inscrits"]:
            print("Vous êtes déjà inscrit à ce cours.")
            return
        cours_table = db.table('cours')
        etudiants_table = db.table('utilisateur')
        User = Query()
        #
        etudiant = etudiants_table.get(User.email == email_etudiant)
        if etudiant is None:
            print("Etudiant non trouvé.")
            return
        if etudiant['solde'] < cours_choisi['prix']:
            print("❌ Solde insuffisant. Veuillez recharger votre compte.")
            return
        #
        nouveau_solde = etudiant['solde'] - cours_choisi['prix']
        etudiants_table.update({'solde': nouveau_solde}, User.email == email_etudiant)
        #
        cours_choisi["etudiants_inscrits"].append(email_etudiant)
        cours_table.update({'etudiants_inscrits': cours_choisi["etudiants_inscrits"]}, Query().title == cours_choisi['title'])
        print(f"✅ Vous êtes maintenant inscrit au cours '{cours_choisi['title']}' ! Nouveau solde: {nouveau_solde} fcfa")