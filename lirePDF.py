import unicodedata
# import fitz
import PyPDF2
import os, re

# #    ********************Récupération du contenu d'un fichier pdf*****************#
# #    ****************************************************************************#
# Prend en entrée un chemin vers nos fichier pdfs et retourne la liste des fichiers pdfs lus
import pdftotext
# from pdfminer.utils import unicode


def lecture_chemin_pdf(path):
    # print("Files ", path)
    filesReader = []
    for file in path:
        openFile = open("/home/ismael/Bureau/M1 IFI SIM/Echantillon_rapport_Bea/" + file, 'rb')
        filesReader.append(PyPDF2.PdfFileReader(openFile))
    return filesReader

# Avoir accès au contenu de chaque fichier pdf ou page pdf
def lecture_fichier_pdf(filesReader):
    rawDoc = []
    rawDocPage = []
    utf8_apostrophe = u"\u0027"
    for file in filesReader:
        # print(file)
        doc = ""
        for pageNum in range(file.numPages):
            docPage = ""
            page = file.getPage(pageNum)
            doc = doc + " " + str(page.extractText())
            docPage = page.extractText().replace('\n', '')
            docPage = docPage.replace('\n', ' ')
            docPage = unicodedata.normalize('NFD', docPage)
            docPage = docPage.replace(u"\u2122", ' ')
            docPage = docPage.replace(u"\u0027", '')
            # docPage = re.sub(utf8_apostrophe, " ", docPage)
            docPage = docPage.encode('ascii', 'ignore')
            # docPage = docPage.encode('utf-8')
            docPage = docPage.decode("utf-8")
            rawDocPage.append(docPage)

        try:
            doc = doc.replace(u"\u2122", ' ')
            # doc = unicode(doc, 'utf-8')
        except (TypeError, NameError):  # unicode is a default on python 3
            pass
        doc = re.sub(utf8_apostrophe, " ", doc)
        doc = unicodedata.normalize('NFD', doc)
        doc = doc.encode('ascii', 'ignore')
        doc = doc.decode("utf-8")
        rawDoc.append(doc)

    return rawDoc, rawDocPage


def lire_pdf(path):
    # print("Files ", path)
    filesReader = []
    text = ""
    for file in path:
        with open("/home/ismael/Bureau/M1 IFI SIM/Echantillon_rapport_Bea/" + file, "rb") as doc:
            pdf = pdftotext.PDF(doc)
            for page in pdf:
                text += page # Chargement de chaque page de du document dans la variable text
        # print(text)  # Affichage du contenu du document
    return text

def lire_pdf_doc(path):
    # print("Files ", path)
    filesReader = []
    for file in path:
        with open("/home/ismael/Bureau/M1 IFI SIM/Echantillon_rapport_Bea/" + file, "rb") as doc:
            pdf = pdftotext.PDF(doc)
            text = ""
            for page in pdf:
                text += page
            filesReader.append(text)
    # print(filesReader[0])
    return filesReader

def lire_pdf_page(path):
    # print("Files ", path)
    filesReader = []
    for file in path:
        with open("/home/ismael/Bureau/M1 IFI SIM/Echantillon_rapport_Bea/" + file, "rb") as doc:
            pdf = pdftotext.PDF(doc)
            for page in pdf:
                filesReader.append(page) # Chargement de chaque page de du document dans la variable text
    # print(filesReader[0])  # Affichage du contenu du document
    return filesReader





