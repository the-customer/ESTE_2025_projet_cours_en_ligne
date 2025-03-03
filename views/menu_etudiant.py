from controllers.cours_controller import CoursController
from controllers.paiement_controller import PaiementController
from controllers.evaluation_controller import EvaluationController as evalCtrl
from controllers.certification_controller import CertificationController as certCtrl

class MenuEtudiant:
    @staticmethod
    def afficher_menu(email):
        while True:
            print("\n=============+ Menu Etudiant +=============")
            print("1........................... Voir mes cours")
            print("2.................... M'inscrire à un cours")
            print("3........................ Acheter du credit")
            print("4................. Passer une certification")
            print("5..................... Voir mes certificats")
            print("6.............................. Déconnexion")
            choix = input("Entrez votre choix : ")

            if choix == "1":
                print("📚 Fonctionnalité en développement...")
            elif choix == "2":
                CoursController.inscrire_etudiant(email)
            elif choix == "3":
                PaiementController.ajouter_solde(email)
            elif choix == "4":
                titre_cours = input("Entrez le titre du cours : ")
                evalCtrl.passer_quiz(email,titre_cours)
            elif choix == "5":
                certCtrl.voir_certificats(email)
            elif choix == "6":
                print("⏼ Déconnexion...")
                break
            else:
                print("❌ Choix invalide, veuillez réessayer.")