from database.db import db
from tinydb import Query

class Paiement:
    def __init__(self, email_etudiant,montant):
        self.email_etudiant = email_etudiant
        self.montant = montant

    def enregistrer_paiement_credit(self):
        paiement_table = db.table('paiements')
        paiement_table.insert({
            'email_etudiant': self.email_etudiant, 'montant': self.montant
        })
        # Mettre a jour le solde de l'etudiant:
        etudiant_table = db.table('utilisateur')
        User = Query()
        etudiant = etudiant_table.get(User.email == self.email_etudiant)

        if etudiant:
            nouveau_solde = etudiant['solde'] + self.montant
            etudiant_table.update({"solde":nouveau_solde},User.email == self.email_etudiant)
            print(f"Dépot réussi ! Nouveau solde : {nouveau_solde} FCFA")
        else:
            print("Etudiant non trouvé!!!")