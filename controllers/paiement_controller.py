from models.paiement import Paiement
class PaiementController:
    @staticmethod
    def ajouter_solde(email):
        montant = int(input("Entrez le montant du credit : "))
        paiement = Paiement(email, montant)
        paiement.enregistrer_paiement_credit()
        print("Le credit a ete ajoute avec succes !")