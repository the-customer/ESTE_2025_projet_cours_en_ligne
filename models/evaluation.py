from tinydb import Query
from database.db import db

class Evaluation:
    def __init__(self, titre_cours: str, questions: list)->None:
        self.titre_cours = titre_cours
        self.questions = questions

    def sauvegarder(self):
        quiz_table = db.table('quiz')
        quiz_table.insert({
            'titre_cours': self.titre_cours, 
            'questions': self.questions
        })

    @staticmethod
    def obtenir_evaluation(titre_cours: str):
        quiz_table = db.table('quiz')
        Quiz = Query()
        return quiz_table.get(Quiz.titre_cours == titre_cours)