from models.evaluation import Evaluation
from tinydb import Query
from database.db import db
from controllers.certification_controller import CertificationController as certifCtrl


class EvaluationController:
    @staticmethod
    def creer_quiz():
        titre_cours = input("Entrez le titre du cours : ")
        questions = []
        while True:
            question = input("Question : ")
            reponse_a = input("Option A : ")
            reponse_b = input("Option B : ")
            reponse_c = input("Option C : ")
            reponse = input("Réponse correcte (A/B/C) : ").upper()
            while reponse not in ['A', 'B', 'C']:
                reponse = input("Réponse correcte (A/B/C) : ").upper()
            #
            questions.append({
                'question': question,
                'options': {"A": reponse_a, "B": reponse_b, "C": reponse_c},
                'reponse': reponse
            })
            #
            continuer = input("Ajouter une autre question ? (O/N) : ").upper()
            if continuer == "N":
                break
        #
        quiz = Evaluation(titre_cours, questions)
        quiz.sauvegarder()
        print(f"✅ Quiz pour le cours '{titre_cours}' créé avec succès !")

    @staticmethod
    def passer_quiz(email_etudiant: str, titre_cours: str):
        evaluation = Evaluation.obtenir_evaluation(titre_cours)
        if not evaluation:
            print(f"❌ Aucun quiz trouvé pour le cours '{titre_cours}'")
            return
        print(f"====> 📝 Quiz pour le cours '{titre_cours}' <====")
        score = 0
        questions = evaluation['questions']
        for i, q in enumerate(questions,start=1):
            print(f"\nQuestion {i} : {q['question']}")
            for key, value in q['options'].items():
                print(f"{key}) {value}")

            reponse_etudiant = input("Votre réponse (A/B/C) : ").upper()
            if reponse_etudiant == q['reponse']:
                score += 1
        total_questions = len(questions)
        pourcentage = (score / total_questions) * 100
        #
        print(f"\n📝 Quiz terminé !\nVous avez obtenu {score} sur {total_questions} questions, soit {pourcentage:.2f}% de bonnes reponses")
        #
        if pourcentage >= 70:
            print("🎉 Félicitation ! Vous recevez un certificat 📜 pour ce cours.")
            certifCtrl.generer_certificat(email_etudiant, titre_cours)
        else:
            print("😔 Vous n'avez pas réussi le quiz, réessayez !")