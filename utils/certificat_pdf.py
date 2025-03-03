import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class CertificationPDF:
    @staticmethod
    def generer_certificat(nom_etudiant: str, titre_cours: str):
        dossierCertificats = "certificats"
        os.makedirs(dossierCertificats, exist_ok=True)

        fichier_pdf = f"{dossierCertificats}/{nom_etudiant}_{titre_cours}.pdf"

        c = canvas.Canvas(fichier_pdf, pagesize=letter)
        c.setFont("Helvetica-Bold", 20)

        # titre du certificat
        c.drawCentredString(300, 700, "CERTIFICAT DE RÈUSSITE")
        c.setFont("Helvetica", 14)
        c.drawCentredString(300, 650, f"Décerné à {nom_etudiant}")
        c.drawCentredString(300, 620, f"Pour la réussite du cours : {titre_cours}")

        # Signature
        c.setFont("Helvetica-Oblique", 12)
        c.drawCentredString(300, 500, "Félicitations pour votre réussite !")
        c.drawCentredString(300, 470, "Breukh-Scool 😎: Plateforme de Cours en Ligne")

        # Finaliser et enregistrer le PDF
        c.save()
        print(f"📜 Certificat généré : {fichier_pdf}")

        return fichier_pdf


