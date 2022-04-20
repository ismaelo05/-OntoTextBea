import math

from sklearn.decomposition import TruncatedSVD

from comptageSelectionTermes import get_ngrams


def initialisation_matrice(matrice, terme_final, token_phrase):
    # Permet l'accès aux phrases du corpus
    compt2 = -1
    # Parcours de la matrice par ligne
    for i in range(len(matrice)):
        # Permet d'accéder aux différentes valeurs des termes
        compt1 = 0
        # Parcours de la matrice en colonne
        for j in range(len(matrice[0])):
            # Mets les valeur de la 1ère ligne de la matrice par les termes
            if i == 0 and j > 0:
                matrice[i][j] = terme_final[compt1]
                compt1 = compt1 + 1
            # Mets les valeur de la 1ère colonne de la matrice par les phrase
            elif i > 0 and j == 0:
                matrice[i][j] = "Phrase " + str(compt2 + 1)
            # compte les occurences de chaque terme dans le corpus
            elif i > 0 and j > 0:
                # Donne le nombre de mots que contient le terme dans une phrase
                nbMotChaine = len(terme_final[compt1].split())
                if nbMotChaine == 1:  # Cas d'un terme simple
                    a = token_phrase[compt2].split()  # Fais du 1-gram
                    matrice[i][j] = a.count(terme_final[compt1])
                elif nbMotChaine == 2:  # Cas d'un terme de deux mots
                    bigrams1 = get_ngrams(token_phrase[compt2], 2)
                    matrice[i][j] = bigrams1.count(terme_final[compt1])
                elif nbMotChaine == 3:  # Cas d'un terme de trois mots
                    trigrams1 = get_ngrams(token_phrase[compt2], 3)
                    matrice[i][j] = trigrams1.count(terme_final[compt1])
                else:  # Cas d'un terme de quatre mots
                    quagrams1 = get_ngrams(token_phrase[compt2], 4)
                    matrice[i][j] = quagrams1.count(terme_final[compt1])
                compt1 = compt1 + 1
            else:
                matrice[i][j] = "  "
        compt2 = compt2 + 1

    return matrice

# Faire la division du nombre de mots compter sous le nombre de mots compté total par phrase
# Permet de calculer la fréquence des termes
def computeTF(wordDict, bagOfWords):
    for i in range(len(bagOfWords)):
        # Permet d'accéder aux différentes valeurs des termes
        # Parcours de la matrice en colonne
        for j in range(len(bagOfWords[0])):
            if i > 0 and j > 0:
                # Donne le nombre de mots que contient le terme
                nbMotChaine = len(bagOfWords[0][j].split())
                # Si le terme choisi est un terme simple
                if nbMotChaine == 1:
                    # Donne la longueur de chaque phrase par Mots unique
                    nbMotPhrase = len(wordDict[i-1].split())
                    # Evalue la fréquende du terme d'un mots
                    bagOfWords[i][j] = bagOfWords[i][j]/nbMotPhrase
                # Si le terme contient 2 mots
                elif nbMotChaine == 2:
                    # Donne la longueur de chaque phrase par 2 Mots unique
                    nbMotPhrase = len(get_ngrams(wordDict[i-1], 2))
                    # Evalue la fréquende du terme de 2 mots
                    bagOfWords[i][j] = bagOfWords[i][j] / nbMotPhrase
                # Si le terme contient 3 mots
                elif nbMotChaine == 3:
                    # Donne la longueur de chaque phrase par 3 Mots unique
                    nbMotPhrase = len(get_ngrams(wordDict[i - 1], 3))
                    # Evalue la fréquende du terme de 3 mots
                    bagOfWords[i][j] = bagOfWords[i][j] / nbMotPhrase
                # Si le terme contient 4 mots
                else:
                    # Donne la longueur de chaque phrase par 4 Mots unique
                    nbMotPhrase = len(get_ngrams(wordDict[i - 1], 4))
                    # Evalue la fréquende du terme de 4 mots
                    bagOfWords[i][j] = bagOfWords[i][j] / nbMotPhrase
    return bagOfWords

# Implémentation de IDF
def computeIDF(bagOfWords, documents):
    # Donne la taille du document en comptant uniquement les phrases
    N = len(documents)
    for i in range(len(bagOfWords)):
        # Parcours de la matrice en colonne
        for j in range(len(bagOfWords[0])):
            if i > 0 and j > 0:
                try:
                    bagOfWords[i][j] = math.log(1/bagOfWords[i][j])
                except:
                    bagOfWords[i][j] = 0
    return bagOfWords

# Implémentation de TFIDF
def computeTFIDF(tfBagOfWords, idfs):
    for i in range(len(tfBagOfWords)):
        # Permet d'accéder aux différentes valeurs des termes
        # Parcours de la matrice en colonne
        for j in range(len(tfBagOfWords[0])):
            if i > 0 and j > 0:
                tfBagOfWords[i][j] = tfBagOfWords[i][j] * idfs[i][j]
    return tfBagOfWords


def matrice_valeur_tfidf(tfidf, matrice2):
    for i in range(len(tfidf)):
        # Parcours de la matrice en colonne
        for j in range(len(tfidf[0])):
            if i > 0 and j > 0:
                matrice2[i - 1][j - 1] = tfidf[i][j]
    return matrice2

def supprimerPhrase(matrice1, tokenPhrase):
    for i in range(len(matrice1)):
        compt = 0
        for j in range(matrice1[0]):
            if i > 0 and j > 0:
                if matrice1[i][j] != 0:
                    compt = compt + 1
        if compt >= 2:
            del tokenPhrase[i-1]
    return tokenPhrase

def implementationSVD(d, matrice2, terme_final):
    svd = TruncatedSVD(n_components=d)
    lsa = svd.fit_transform(matrice2)
    v_trans = svd.components_
    # print(lsa)
    print("\n")
    # print(v_trans)

    # print(len(terme_final))
    # print()
    # print()
    for index, component in enumerate(v_trans):
        zipped = zip(terme_final, component)
        top_terms_key = sorted(zipped, key=lambda t: t[1], reverse=True)[:3]
        top_terms_list = list(dict(top_terms_key).keys())
        print("Topic " + str(index) + ": ", top_terms_list)