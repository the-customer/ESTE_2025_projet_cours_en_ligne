from controllers.evaluation_controller import EvaluationController as evalCtrl


class MenuProfesseur:
    @staticmethod
    def afficher_menu(email):
        while True:
            print("\n=============+ Menu Professeur +=============")
            print("1.............................. Creer un cours")
            print("2............................. Ajouter un quiz")
            print("3................................. Deconnexion")
            choix = input("Choisissez une option : ")

            if choix == "1":
                print("📚 Fonctionnalité en développement...")
            elif choix == "2":
                evalCtrl.creer_quiz()
                pass
            elif choix == "3":
                print("⏼ Déconnexion...")
                break
            else:
                print("❌ Option invalide, veuillez réessayer.")