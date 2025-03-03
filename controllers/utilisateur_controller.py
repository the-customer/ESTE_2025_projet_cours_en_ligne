from models.etudiant import Etudiant
from models.professeur import Professeur
from models.admin import Admin
from models.utilisateur import Utilisateur
from views.menu_etudiant import MenuEtudiant
from views.menu_professeur import MenuProfesseur


class UtilisateurController:
    @staticmethod
    def creer_utilisateur():
        nom = input("Nom : ")
        email = input("Email : ")
        mdp = input("Mot de passe : ")
        role = input("Role [etudiant/professeur/admin] : ")

        # utilisateur = Utilisateur(nom, email, mdp, role)
        # utilisateur.sauvegarder()
        
        if(role == "etudiant"):
            utilisateur = Etudiant(nom, email, mdp)
        elif(role == "professeur"):
            utilisateur = Professeur(nom, email, mdp)
        elif(role == "admin"):
            utilisateur = Admin(nom, email, mdp)
        else:
            print("Role invalide")
            return
        utilisateur.sauvegarder()
        print(f"<{role.capitalize()}> {nom} ajouté avec succès")
    
    @staticmethod
    def connexion():
        email = input("Email : ")
        mdp = input("Mot de passe : ")

        utilisateur = Utilisateur.trouver_par_email(email)
        if(utilisateur is None):
            print("Utilisateur introuvable")
            return
        if(utilisateur['mdp'] != mdp):
            print("Mot de passe incorrect")
            return
        print(f"Bienvenue {utilisateur['nom'].upper()}")
        if utilisateur['role'] == "etudiant":
            MenuEtudiant.afficher_menu(email)
        elif utilisateur['role'] == "professeur":
            MenuProfesseur.afficher_menu(email)
        return utilisateur