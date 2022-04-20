import os
# import pdf2text
import numpy as np
import spacy
import string
import pandas as pd
from gensim.models import Word2Vec
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
from nltk import sent_tokenize
from scipy.linalg import svd
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import lirePDF
import nettoyageCorpus
import math
import re
import synonymeCorpus
import implementationTFIDF
from textcleaner import *
import suppressionCaractereSpeciaux
import collections
from collections import OrderedDict
import retraitPonctuation
import comptageSelectionTermes
import spacy
import implementationTFIDFavecSeuil
import word2vectImplementation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

# Création d'un corpus appelé initié par la variable text
# Création du chemin d'accès à nos dataset

files = os.listdir("/home/ismael/Bureau/M1 IFI SIM/Echantillon_rapport_Bea/")

tablo_pdf_page = lirePDF.lire_pdf(files)
# textSansponctuation = retraitPonctuation.remove_ponctuation_sign1(tablo_pdf_page)
# print(textSansponctuation)
textMinuscule = nettoyageCorpus.mise_en_miniscule1(tablo_pdf_page)
# print(textMinuscule)
textSanslignevide = nettoyageCorpus.remove_empty_line1(textMinuscule)
nlp = spacy.load("fr_core_news_lg")
textSanslignevide = str(textSanslignevide)
nlp.max_length = 2000000
textSanslignevide = nlp(textSanslignevide)
# print("bonjour")
tokmot = suppressionCaractereSpeciaux.lemmanisation_corpus3(textSanslignevide)
# print(tokmot)
tokmot = " ".join(tokmot)
# print(textSanslignevide)
tokphrase = sent_tokenize(tokmot, 'french')
# print(tokphrase)
tokphrase1 = []
for t in tokphrase:
    c = nlp(t)
    tokphrase1.append(c)
# print(tokphrase1)
lemphrase = suppressionCaractereSpeciaux.lemmanisation_corpus2(tokphrase1)
# print(lemphrase)
phrase = suppressionCaractereSpeciaux.supprimer_stop_words(lemphrase)
# print(phrase)
phrase1 = []
for a in phrase:
    s = " ".join(a)
    phrase1.append(s)
# print(phrase1)

terme_pour_syno = []
for b in phrase:
    for c in b:
        terme_pour_syno.append(c)

print(len(terme_pour_syno))
print('\n')
vectorizer = TfidfVectorizer()
response = vectorizer.fit_transform(phrase1)
# print(response)
# C = 1 - cosine_similarity(response.T)
# ward = AgglomerativeClustering(n_clusters=50, linkage='ward').fit(C)
# label = ward.labels_
# print(label)
# print(ward)



# from sklearn.cluster import KMeans
#
# km = KMeans(n_clusters=50, init='k-means++', max_iter=100, n_init=1)
# km.fit(response)
# order_centroids = km.cluster_centers_.argsort()[:, ::-1]
# terms = vectorizer.get_feature_names()
# for i in range(50):
#     print("Cluster %d:" % i, end='')
#     for ind in order_centroids[i, :10]:
#         print(' %s' % terms[ind], end='')
#     print('\n')


newDoc = []
nbDoc = len(phrase1)
listDic = vectorizer.get_feature_names_out()

termes = []
for doc in range(nbDoc):
    dicIndex = response[doc,:].nonzero()[1]
    dicZip = zip(dicIndex, [response[doc, x] for x in dicIndex])
    temp = []
    for w, s in [(listDic[i], s) for (i, s) in dicZip]:
        if s >= 0.05:
            temp.append(w)
            # print(w, s)
            termes.append(w)
    newDoc.append(" ".join(temp))
# print(newDoc)
# print(temp)
# print(termes)

phrase2 = []
for a in newDoc:
    compt = 0
    for ter in termes:
        if ter in a:
            compt = compt + 1
    if compt >= 2:
        phrase2.append(a)
        # print(compt)

# print(phrase2)
phrase3 = []
for phra in phrase2:
    liste = comptageSelectionTermes.get_ngrams(phra, 1)
    phrase3.append(liste)
# print(phrase3)

terme = []
for ter in termes:
    compteur = 0
    for a in phrase3:
        if ter in a:
            compteur = compteur + 1
    if compteur != 0:
        terme.append(ter)

# print(terme)
# print(terme_pour_syno)
# print(len(terme))
termes_synonyme = synonymeCorpus.synonymes(termes, terme_pour_syno)
# print(len(termes_synonyme))
terme_final = list(set(terme + termes_synonyme))
# print(terme_final)

mon_texte = []
mon_text = []
mon_tex = []
for l_lis in phrase2:
    la_list = comptageSelectionTermes.get_ngrams(l_lis, 1)
    app = []
    for parc in la_list:
        if parc in termes_synonyme:
            app.append(parc)
    if len(app) > 0:
        mon_texte.append(" ".join(app))
        mon_text.append(app)
        for da in app:
            mon_tex.append(da)

print('\n')
print('\n')
# print(mon_texte)
# print(len(phrase2))
# print(mon_text)
print('\n')

cluster = word2vectImplementation.implementationWV(mon_texte, mon_text, mon_tex)
# print(cluster)

# doc_matrix = tfidf.fit_transform()


# tokenmot = suppressionCaractereSpeciaux.lemmanisation_corpus1(textSanslignevide)
# print(tokenmot)
# word = suppressionCaractereSpeciaux.supprimer_stop_words1(tokenmot)
# print(word)
# fd = comptageSelectionTermes.creation_dicti_terme_valeur1(word)
# print(fd)

# Afficher les termes simples ie contenant un seul mot non-vide
# triés par ordre de fréquence décroissante
# ab = comptageSelectionTermes.copier_terme_suivant_seuil1(fd, seuil=3)
# print(ab)

# Création d'une liste à partir d'un dictionnaire

# termes = comptageSelectionTermes.creer_liste_grace_dictionnaire(ab)
# print(termes)



# tablo_pdf_page = lirePDF.lire_pdf_page(files)
# print(tablo_pdf_doc)
# Retrait des signes de ponctuation dans le corpus

# text_ponct = retraitPonctuation.remove_ponctuation_sign1(text)
# print(text_ponct)

# Suppression des lignes vides dans le corpus
# Mise en miniscule d'un corpus
# list_doc_net = nettoyageCorpus.remove_empty_line(nettoyageCorpus.mise_en_miniscule(tablo_pdf_doc))
# list_doc_page_net = nettoyageCorpus.remove_empty_line(nettoyageCorpus.mise_en_miniscule(tablo_pdf_page))
# print(list_doc_net)
# Cette partie permet de sélectionner les termes d'un mot de notre corpus grace
# à la méthode d’indexation sémantique qui consiste à récupérer les mots les plus
# fréquents de notre corpus


# print(text_clear)
# Chargement de la librairie française de spacy
# nlp = spacy.load("fr_core_news_lg")
# Mise en chaine des caractères du corpus
# data = str(data)
# print(data)
#Lemmatize ou Tokenisation de mots
# tokens_doc = [nlp(str(i)) for i in list_doc_net]
# tokens_page = [nlp(str(i)) for i in list_doc_page_net]
# print(tokens_page[0])


# lem_doc = suppressionCaractereSpeciaux.lemmanisation_corpus(tokens_doc)
# lem_page = suppressionCaractereSpeciaux.lemmanisation_corpus(tokens_page)
# Suppression des stops wordds dans le corpus
# lem_ = suppressionCaractereSpeciaux.lemmanisation_corpus2(tokens_page)
# lem_1 = []
# for liste in lem_:
#     # print(liste)
#     for i in liste:
#         lem_1.append(i)
# print()
# print(lem_1)
# lem_token = suppressionCaractereSpeciaux.supprimer_stop_words1(lem_1)
# print()
# print(lem_token)

# list_lem_doc = [str(i) for i in list_lem_doc]
# list_lem_doc_page = [str(i) for i in list_lem_doc_page]
# print(list_lem_doc)

# print(list_lem_doc)
# Création d'une collection de comptage de mots sans stops words
# fd = comptageSelectionTermes.creation_dicti_terme_valeur1(lem_token)
# print(fd)


# Afficher les termes simples ie contenant un seul mot non-vide
# triés par ordre de fréquence décroissante
# ab = comptageSelectionTermes.copier_terme_suivant_seuil1(fd, seuil=5)
# print(ab)

# Création d'une liste à partir d'un dictionnaire

# termes = comptageSelectionTermes.creer_liste_grace_dictionnaire(ab)
# print(termes)


"""

# Cette partie consiste à déterminer les termes ayant plus d'un mot
# par utilisation de l'approches identification des patrons typiques qui 
# consiste à récupérer les termes les plus fréquents

# Création d'une  chaine à partir d'n token
chaine_mots = " ".join(tokens)


# Création d'une liste de tuple avec 2 mots
bigrams = comptageSelectionTermes.get_ngrams(chaine_mots, 2)
# Création d'une liste de tuple avec 3 mots
trigrams = comptageSelectionTermes.get_ngrams(chaine_mots, 3)
# Création d'une liste de tuple avec 4 mots
quagrams = comptageSelectionTermes.get_ngrams(chaine_mots, 4)

#print(bigrams)
print()
# Création des listes vides devant contenir les termes candidats
# de chacun des ngrames créés plus haut
b1 = []
b2 = []
b3 = []

# print(type(bigrams))
# Parcour de de notre liste de tuple nommé bigrams
# print(bigrams)
for liste in bigrams:
    liste1 = nlp(liste)
    if (liste1[0].pos_ == 'NOUN' and liste1[1].pos_ == 'NOUN') or (liste1[0].pos_ == 'NOUN' and liste1[1].pos_ == 'ADJ'):
        a = str(liste1[0]) + ' ' + str(liste1[1])
        b1.append(a)

# Affichage de liste contenant 2 mots selon la condition donnée
# print(b1)
print()

# Parcour de de notre liste de tuple nommé trigrams
for liste in trigrams:
    liste1 = nlp(liste)
    if (liste1[0].pos_ == 'NOUN' and liste1[1].pos_ == 'PRP' and liste1[2].pos_ == 'NOUN') or (liste1[0].pos_ == 'NOUN' and liste1[1].pos_ == 'PRP' and liste1[2].pos_ == 'VERB'):
        a = str(liste1[0])+' '+str(liste1[1]) + ' '+str(liste[2])
        b2.append(a)

# Affichage de liste contenant 3 mots selon la condition donnée
# print(b2)
print()

# Parcour de de notre liste de tuple nommé quagrams
for liste in quagrams:
    liste1 = nlp(liste)
    if liste1[0].pos_ == 'NOUN' and liste1[1].pos_ == 'PRP' and liste1[2].pos_ == 'DET' and liste1[3].pos_ == 'NOUN':
        a = str(liste1[0]) + ' ' + str(liste1[1]) + ' ' + str(liste[2]) + ' ' + str(liste[3])
        b3.append(a)


# Création d'une collection de comptage de mots sans stops words
# Création d'un dictionnaire clé valeur
# La clé représente chaque mot
# La valeur représente le nombre d'occurence de ce mot

# Création d'un dictionnaire de mots complexes avec valeur pour chaque gram
fd1 = comptageSelectionTermes.creation_dicti_terme_valeur(b1)
fd2 = comptageSelectionTermes.creation_dicti_terme_valeur(b2)
fd3 = comptageSelectionTermes.creation_dicti_terme_valeur(b3)
# Comptage des termes complexes >= 2
ab1 = comptageSelectionTermes.copier_terme_suivant_seuil(fd1, 2)
ab2 = comptageSelectionTermes.copier_terme_suivant_seuil(fd2, 2)
ab3 = comptageSelectionTermes.copier_terme_suivant_seuil(fd3, 2)
# Afficher les termes complexes ie contenant deux mots non-vides
# triés par ordre de fréquence décroissante
# print(ab1)
# print(ab2)
# print(ab3)
# print()
# Ajout des autres termes dans notre liste
termes1 = comptageSelectionTermes.creer_liste_grace_dictionnaire(ab1)
termes2 = comptageSelectionTermes.creer_liste_grace_dictionnaire(ab2)
termes3 = comptageSelectionTermes.creer_liste_grace_dictionnaire(ab3)
# print(termes0)
termes = termes0 + termes1 + termes2 + termes3
# print(termes)
#######################################################################################################
#######################################################################################################
                                        #Découverte des synonymes#
#######################################################################################################
#######################################################################################################

# termes = ['vent', 'planeur', 'heure', 'aérodrome', 'piste', 'vol', 'degré', 'accident', 'pilote', 'descendance', 'kt', 'rafale', 'branche vent', 'vent arrière', 'descendance important']
# print(wordnet.synsets('vent'))
termes_synonyme = synonymesCorpus.synonymes(termes, output)

print("les  synonymes")
print(termes_synonyme)
print("Les termes générales sont")
terme_final = list(set(termes + termes_synonyme))

print(terme_final)


#######################################################################################################
#######################################################################################################
                                        #Découverte des concepts#
#######################################################################################################
#######################################################################################################

# terme_final = ['degré', 'accident', 'vent arrière', 'aérodrome', 'pilote', 'descendance', 'souffler', 'kt', 'conséquence', 'descendance important', 'planeur', 'vent', 'heure', 'rafale', 'piste', 'vol', 'devoir']

# Implémentation de la méthode du sac à dos

data1 = nettoyageCorpus.mise_en_miniscule(text)
# print(data1)
data1 = nettoyageCorpus.remove_empty_line(data1)
data1 = str(data1)
tokens_texte1 = nlp(data1)
tokens1 = suppressionCaractereSpeciaux.lemmanisation_corpus1(tokens_texte1)
retraitMots = suppressionCaractereSpeciaux.supprimer_stop_words1(tokens1)
# print(retraitMots)

texte = ''.join(tokens1)
token_phrase = sent_tokenize(texte)
print(token_phrase)
token_word1 = comptageSelectionTermes.get_ngrams(texte, 1)
token_word2 = suppressionCaractereSpeciaux.supprimer_stop_words(token_word1)
symbole = [",", ";", "-", "(", ")", ".", "_", ":", "/", "|"]
token_word = [i for i in token_word2 if i not in symbole]
token_word = list(set(token_word))

# print(token_word)
# print(token_phrase)

# Définir le nombre de ligne de notre matrice
ligne = len(token_phrase)+1
# print(len(token_phrase))
# Dééfinir le nombre de colonne de notre matrice
colonne = len(terme_final)+1
# Définir une matrice donc la 1ère colonne représente les phrases du corpus tandis que la 1ère ligne
# représente les termes extraites précédemment et les autres cellules de la matrice représentent les
# occurences de nos termes dans le corpus
matrice = [[0]*colonne for i in range(ligne)]
matrice = implementationTFIDF.initialisation_matrice(matrice, terme_final, token_phrase)
# print(matrice)
# print()

# Appel de la fonction computeTF
tf = implementationTFIDF.computeTF(token_phrase, matrice)
# print("Voici la fréquence TF de chaque terme")
# print(tf)
# print()

# Calcul de IDF qui représente la fréquence inverse du document
# Permettant de donner un poids plus important aux termes moins fréquent
# Appel de la fonction de calcul de IDF
idfs = implementationTFIDF.computeIDF(matrice, token_phrase)
# print("Voici les statistiques IDF")
# print(idfs)
# print()

# Calcul de la mesure statistique TF-IDF de chaque terme
# Appel de la fonction qui évalue chaque TF-IDF
tfidf = implementationTFIDF.computeTFIDF(tf, idfs)
# print(tfidf)
# print()

# Création d'une nouvelle matrice par suppression de la 1ère ligne et colonne
matrice2 = [[0]*(colonne-1) for i in range(ligne-1)]
# Diminution de la 1ère ligne et 1ère colonne de
matrice2 = implementationTFIDF.matrice_valeur_tfidf(tfidf, matrice2)
# print(matrice2)
# print()

# Variable définissant le nombre de concepts donc on a besoin
# Faire la divion entière
d = len(terme_final) // 3
implementationTFIDF.implementationSVD(d, matrice2, terme_final)
"""
#################################################################################################
                    # Implémentation de TF-IDF suivie de la méthode SVD
#################################################################################################
"""
data1 = nettoyageCorpus.mise_en_miniscule(text)
# print(data1)
data1 = nettoyageCorpus.remove_empty_line(data1)
data1 = str(data1)
tokens_texte1 = nlp(data1)
tokens1 = suppressionCaractereSpeciaux.lemmanisation_corpus(tokens_texte1)
retraitMots = suppressionCaractereSpeciaux.supprimer_stop_words(tokens1)
# print(retraitMots)

texte = ' '.join(tokens1)
token_phrase = sent_tokenize(texte)
token_word1 = comptageSelectionTermes.get_ngrams(texte, 1)
token_word2 = suppressionCaractereSpeciaux.supprimer_stop_words(token_word1)
symbole = [",", ";", "-", "(", ")", ".", "_", ":", "/", "|"]
token_word = [i for i in token_word2 if i not in symbole]
token_word = list(set(token_word))
# print(token_word)
# print(token_phrase)
# Définir le nombre de ligne de notre matrice
ligne = len(token_phrase)+1
# print(len(token_phrase))
# Dééfinir le nombre de colonne de notre matrice
colonne = len(token_word)+1
# Définir une matrice donc la 1ère colonne représente les phrases du corpus tandis que la 1ère ligne
# représente les termes extraites précédemment et les autres cellules de la matrice représentent les
# occurences de nos termes dans le corpus
matrice = [[0]*colonne for i in range(ligne)]
# Permet l'accès aux phrases du corpus
matrice = implementationTFIDFavecSeuil.initialisation_matrice(matrice, token_word, token_phrase)
# print(matrice)
print()

# Faire la division du nombre de mots compter sous le nombre de mots compté total par phrase
# Permet de calculer la fréquence des termes
# Appel de la fonction computeTF
tf = implementationTFIDFavecSeuil.computeTF(token_phrase, matrice)
print("Voici la fréquence TF de chaque terme")
# print(tf)
# print()


# Calcul de IDF qui représente la fréquence inverse du document
# Permettant de donner un poids plus important aux termes moins fréquent
# Appel de la fonction de calcul de IDF
idfs = implementationTFIDFavecSeuil.computeIDF(matrice, token_phrase)
print("Voici les statistiques IDF")
# print(idfs)
# print()
# print()

# Calcul de la mesure statistique TF-IDF de chaque terme
# Appel de la fonction qui évalue chaque TF-IDF
tfidf = implementationTFIDFavecSeuil.computeTFIDF(tf, idfs)
# print(tfidf)
# print()
# print()

# Calcul du score moyen pour la sélection de nos termes
# Cette valeur est appelée treshold
scoreMoyen = implementationTFIDFavecSeuil.score_moyen(token_phrase, tfidf)
# print(scoreMoyen)
# print(token_phrase)

terme_cle = implementationTFIDFavecSeuil.selection_termes(tfidf, scoreMoyen)
# print(terme_cle)
# print(wordnet.synsets('vent'))
termes_synonyme = synonymesCorpus.synonymes(terme_cle, output)
# print(output)

ligne1 = len(token_phrase)
colonne1 = len(termes_synonyme)
matrice1 = [[0]*colonne1 for i in range(ligne1)]
matrice1 = implementationTFIDFavecSeuil.new_matrice(matrice1, tfidf, termes_synonyme)
# print(matrice1)

# Variable définissant le nombre de concepts donc on a besoin
# Faire la divion entière
d = len(termes_synonyme) // 3
implementationTFIDF.implementationSVD(d, matrice1, termes_synonyme)
"""
#########################################################################################
                           # Word embedding + clustering
######################################################################################

# list_doc_net = nettoyageCorpus.mise_en_miniscule(list_doc)
# list_doc_page_net = nettoyageCorpus.mise_en_miniscule(list_doc_page)
# print(list_doc_page_net)



# terme_final1 = ['accident',  'aérodrome', 'pilote', 'descendance', 'souffler', 'conséquence', 'planeur', 'vent', 'rafale', 'piste', 'vol']
# words = list(model.wv[model.vocab])
# terme_final1 = ['pilote', 'enquête', 'avion', 'dernier', 'sol', 'épave', 'hélicoptère', 'numéro', 'virage', 'rotor', 'aérodrome', 'fevrier', 'immatricule', 'degré', 'fort', 'hauteur', 'condition', 'mettre', 'poutre', 'série', 'vitesse', 'droite', 'panne', 'opération', 'observation', 'béquille', 'faire', 'vue', 'décolle', 'indique', 'partie', 'côte', 'indiquer', 'centrage', 'réduire', 'passager', 'limite', 'voir', 'altitude', 'utilisation', 'observer', 'position', 'témoin', 'décrochage', 'décide']
# print()
# word2vectImplementation.implementationWV(lem_doc, termes)
# print()
# word2vectImplementation.implementationWV(lem_page, termes)


# print(termes_synonyme)
# print()
# print()
# term_synonyme = []
# for term in termes_synonyme:
#     term = term.replace('_', ' ')
#     term_synonyme.append(term)
#
# print(term_synonyme)
# print()
# print()
# # Rechercher les synonymes qui sont dans le texte en un mots
# terme_finale = []
# for a in gram:
#     count = 0
#     for b in term_synonyme:
#         if a == b:
#             count = count + 1
#     if count > 0:
#         terme_finale.append(a)
#
# # Rechercher les synonymes qui sont dans le texte en deux mots
# for a in bigrams_liste:
#     count = 0
#     for b in term_synonyme:
#         if a == b:
#             count = count + 1
#     if count > 0:
#         terme_finale.append(a)
#
# # Rechercher les synonymes qui sont dans le texte en trois mots
# for a in trigrams_liste:
#     count = 0
#     for b in term_synonyme:
#         if a == b:
#             count = count + 1
#     if count > 0:
#         terme_finale.append(a)
#
#
# # Rechercher les synonymes qui sont dans le texte en trois mots
# for a in quagrams_liste:
#     count = 0
#     for b in term_synonyme:
#         if a == b:
#             count = count + 1
#     if count > 0:
#         terme_finale.append(a)
#
# print(terme_finale)
# print()
# print()
# terme_finale = terme_finale + termes
# print(terme_finale)
# print()
# print()
# terme_finale = list(set(terme_finale))
# print(terme_finale)

