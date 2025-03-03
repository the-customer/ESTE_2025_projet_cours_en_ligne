from tinydb import Query
from database.db import db
from utils.certificat_pdf import CertificationPDF


class CertificationController:
    @staticmethod
    def generer_certificat(email_etudiant: str, titre_cours: str):
        certificat_table = db.table('certifications')
        
        etudiant_table = db.table('utilisateur')
        User = Query()
        etudiant = etudiant_table.get(User.email == email_etudiant)

        if not etudiant:
            print("❌ L'étudiant n'existe pas.")
            return
        nom_etudiant = etudiant['nom']

        fichier_pdf = CertificationPDF.generer_certificat(nom_etudiant, titre_cours)

        certificat_table.insert({
            'email_etudiant': email_etudiant,
            'titre_cours': titre_cours,
            'fichier_pdf': fichier_pdf
        })
        print(f"Certificat 📜 enregistré avec succès pour {email_etudiant} - {titre_cours}!")
        print(f"📄 Certificat disponible : {fichier_pdf}")

    @staticmethod
    def voir_certificats(email_etudiant: str):
        certificat_table = db.table('certifications')
        Certif = Query()
        certifications = certificat_table.search(Certif.email_etudiant == email_etudiant)

        if not certifications:
            print("❌ Aucun certificat trouvé.")
            return

        print("📜 Mes Certificats: 📜")
        for certif in certifications:
            print(f" - {certif['titre_cours']} 📜")