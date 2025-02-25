from controllers.utilisateur_controller import UtilisateurController as userCtrl

class Menu:
    @staticmethod
    def afficher_menu_principal():
        while True:
            print("====+ Plateforme de Cours en Ligne +====")
            print("1. Se connecter")
            print("2. S'inscrire")
            print("3. Quitter")
            choix  = input("Votre choix : ")


            if choix == "1":
                userCtrl.connexion()
            elif choix == "2":
                userCtrl.creer_utilisateur()
            elif choix == "3":
                print("Au revoir")
                break
            else:
                print("Choix invalide, veuillez réessayer")
