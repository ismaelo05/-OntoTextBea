import math

from comptageSelectionTermes import get_ngrams


def initialisation_matrice(matrice, token_word, token_phrase):
    compt2 = -1
    # Parcours de la matrice par ligne
    for i in range(len(matrice)):
        # Permet d'accéder aux différentes valeurs des termes
        compt1 = 0
        # Parcours de la matrice en colonne
        for j in range(len(matrice[0])):
            # Mets les valeur de la 1ère ligne de la matrice par les termes
            if i == 0 and j > 0:
                matrice[i][j] = token_word[compt1]
                compt1 = compt1 + 1
            # Mets les valeur de la 1ère colonne de la matrice par les phrase
            elif i > 0 and j == 0:
                matrice[i][j] = "Phrase " + str(compt2 + 1)
            # compte les occurences de chaque terme dans le corpus
            elif i > 0 and j > 0:
                # Donne le nombre de mots que contient le terme dans une phrase
                a = get_ngrams(token_phrase[compt2], 1)
                matrice[i][j] = a.count(token_word[compt1])
                compt1 = compt1 + 1
            else:
                matrice[i][j] = "  "
        compt2 = compt2 + 1
    return matrice


def computeTF(wordDict, bagOfWords):
    for i in range(len(bagOfWords)):
        # Permet d'accéder aux différentes valeurs des termes
        # Parcours de la matrice en colonne
        for j in range(len(bagOfWords[0])):
            if i > 0 and j > 0:
                # Donne la longueur de chaque phrase par 4 Mots unique
                nbMotPhrase = len(get_ngrams(wordDict[i - 1], 1))
                # Evalue la fréquende du terme de 4 mots
                bagOfWords[i][j] = bagOfWords[i][j] / nbMotPhrase
    return bagOfWords



def computeIDF(bagOfWords, documents):
    # Donne la taille du document en comptant uniquement les phrases
    N = len(documents)
    for i in range(len(bagOfWords)):
        # Parcours de la matrice en colonne
        for j in range(len(bagOfWords[0])):
            if i > 0 and j > 0:
                try:
                    bagOfWords[i][j] = math.log(N/bagOfWords[i][j])
                except:
                    bagOfWords[i][j] = 0
    return bagOfWords


def computeTFIDF(tfBagOfWords, idfs):
    for i in range(len(tfBagOfWords)):
        # Permet d'accéder aux différentes valeurs des termes
        # Parcours de la matrice en colonne
        for j in range(len(tfBagOfWords[0])):
            if i > 0 and j > 0:
                tfBagOfWords[i][j] = tfBagOfWords[i][j] * idfs[i][j]
    return tfBagOfWords



def score_moyen(liste_phrase, bagOfWords):
    # Donne la taille du document en comptant uniquement les phrases
    moyen = 0
    for i in range(1, len(bagOfWords)):
        somme = 0
        # Parcours de la matrice en colonne
        for j in range(len(bagOfWords[0])):
            if i > 0 and j > 0:
                somme = somme + bagOfWords[i][j]
        # motPhrase = len(get_ngrams(liste_phrase[i-1], 1))
        # print(motPhrase)
        # print(somme)
        somme1 = somme / (len(bagOfWords[0])-1)
        # print(somme1)
        moyen = moyen + somme1
        # print(moyen)
    # print(len(bagOfWords)-1)
    moyenne = moyen / (len(bagOfWords) - 1)
    return moyenne

def selection_termes(bagOfWords, score):
    liste_terme = []
    for j in range(1, len(bagOfWords[0])):
        somme = 0
        # Parcours de la matrice en colonne
        for i in range(len(bagOfWords)):
            if i > 0 and j > 0:
                somme = somme + bagOfWords[i][j]
        # print(len(bagOfWords) - 1)
        somme = somme / (len(bagOfWords) - 1)
        if somme <= score and somme > 0:
            liste_terme.append(bagOfWords[0][j])
    return liste_terme


# Nouvelle Matrice TFIDF
def new_matrice(matrice1, tfidf, termes_synonyme):
    indice = 0
    for i in range(1, len(tfidf[0])):
        if tfidf[0][i] in termes_synonyme:
            for j in range(1, len(tfidf)):
                matrice1[j - 1][indice] = tfidf[j][i]
            indice = indice + 1

    return matrice1