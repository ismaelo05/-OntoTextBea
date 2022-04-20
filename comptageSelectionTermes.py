import collections
from nltk import ngrams, word_tokenize, sent_tokenize
def creation_dicti_terme_valeur(token):
    # Création d'un dictionnaire clé valeur
    # La clé représente chaque mot
    # La valeur représente le nombre d'occurence de ce mot
    liste = []
    for tok in token:
        if len(tok) != 0:
            fd = collections.Counter(tok)
            liste.append(fd)
    return liste

def creation_dicti_terme_valeur1(token):
    # Création d'un dictionnaire clé valeur
    # La clé représente chaque mot
    # La valeur représente le
    # nombre d'occurence de ce mot
    fd = collections.Counter(token)
    return fd

def copier_terme_suivant_seuil(dico, seuil=3):
    # Création d'un dictionnaire vide
    liste = []
    for doc in dico:
        ab = {}
        # Sélectionner les clés ou mots ayant une valeur supérieure à 3
        ab = {key: value for key, value in doc.items() if value >= seuil}
        # Trier notre dictionnaire dans l'ordre décroissant de valeurs
        ab = sorted(ab.items(), key=lambda x: x[1], reverse=True)
        liste.append(ab)
    return ab

def copier_terme_suivant_seuil1(dico, seuil=3):
    # Création d'un dictionnaire vide
    ab = {}
    # Sélectionner les clés ou mots ayant une valeur supérieure à 3
    ab = {key: value for key, value in dico.items() if value >= seuil}
    # Trier notre dictionnaire dans l'ordre décroissant de valeurs
    ab = sorted(ab.items(), key=lambda x: x[1], reverse=True)
    return ab

def creer_liste_grace_dictionnaire(dico):
    gram = []
    for a in dico:
        if len(a[0]) < 15 and len(a[0]) > 2:
            gram.append(a[0])
    return gram

# Fonction ngram
def get_ngrams(text, n ):
    n_grams = ngrams(word_tokenize(text), n)
    return [' '.join(grams) for grams in n_grams]