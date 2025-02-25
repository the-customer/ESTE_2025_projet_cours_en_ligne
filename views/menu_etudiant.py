from controllers.cours_controller import CoursController
from controllers.paiement_controller import PaiementController

class MenuEtudiant:
    @staticmethod
    def afficher_menu(email):
        while True:
            print("\n=============+ Menu Etudiant +=============")
            print("1........................... Voir mes cours")
            print("2.................... M'inscrire à un cours")
            print("3........................ Acheter du credit")
            print("4.............................. Déconnexion")
            choix = input("Entrez votre choix : ")

            if choix == "1":
                print("📚 Fonctionnalité en développement...")
            elif choix == "2":
                CoursController.inscrire_etudiant(email)
            elif choix == "3":
                PaiementController.ajouter_solde(email)
            elif choix == "4":
                print("⏼ Déconnexion...")
                break
            else:
                print("❌ Choix invalide, veuillez réessayer.")