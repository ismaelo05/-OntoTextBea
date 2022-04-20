import nltk
from gensim.models import Word2Vec
from nltk.cluster import KMeansClusterer
from numpy.dual import svd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from matplotlib import pyplot
# from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples, silhouette_score
# from sklearn-som.som import SOM

import PyPDF2
import spacy
from nltk.tag import StanfordPOSTagger
from nltk.tag.stanford import StanfordNERTagger
from nltk import pos_tag, ne_chunk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.cluster import KMeansClusterer
import nltk
import nltk.data
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer
from sklearn.cluster import DBSCAN
import re, os
import unicodedata
# from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
from gensim.models import Word2Vec


def implementationWV(mon_texte, mon_text, mon_tex):
    vectorizer1 = TfidfVectorizer()
    response1 = vectorizer1.fit_transform(mon_texte)
    # Check the best number of cluster
    model = Word2Vec(mon_text, vector_size=50, window=1, min_count=5)
    newTerms = []
    for word in model.wv.index_to_key:
        if word in mon_tex:
            newTerms.append(word)

    print(len(newTerms))
    # model.wv[model.wv.index_to_key]
    X = model.wv[newTerms]
    previous_silh_avg = 0.0
    for n_clusters in range(len(newTerms) // 2, len(newTerms)):
        # print(X)
        clusterer = KMeans(n_clusters=n_clusters, random_state=10)
        cluster_labels = clusterer.fit_predict(X)
        # print(cluster_labels)
        silhouette_avg = silhouette_score(X, cluster_labels)
        if silhouette_avg > previous_silh_avg:
            previous_silh_avg = silhouette_avg
            best_clusters = n_clusters
    print()
    print(best_clusters)

    km = KMeans(n_clusters=best_clusters, init='k-means++', max_iter=100, n_init=1)
    km.fit(response1)
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer1.get_feature_names()
    terme_all_cluster = []
    for i in range(best_clusters):
        print("Cluster %d:" % i, end='')
        terme_cluster = []
        for ind in order_centroids[i, :10]:
            print(' %s' % terms[ind], end='')
            terme_cluster.append(terms[i])
        terme_all_cluster.append(terme_cluster)
        print('\n')
    return terme_all_cluster
    # print("Les Tops termes par cluster sont:")
    # words = newTerms
    # clusters = dict()
    # for i, word in enumerate(words):
    #     if terms[i] in clusters:
    #         clusters[terms[i]].append(word)
    #     else:
    #         l = []
    #         l.append(word)
    #         clusters[terms[i]] = l
    #     # print (word + ":" + str(assigned_clusters[i]))
    # for cle in clusters:
    #     print(cle, ":", clusters[cle], "\n")
    #     # print(' %s' % words[ind].split(' '))


    # clusters = dict()
    # words = newTerms
    # #model.wv.index_to_key
    # for i, word in enumerate(words):
    #     if terms[i] in clusters:
    #         clusters[terms[i]].append(word)
    #     else:
    #         l = []
    #         l.append(word)
    #         clusters[terms[i]]=l
    #     #print (word + ":" + str(assigned_clusters[i]))
    # for cle in clusters:
    #     print(cle, ":", clusters[cle], "\n")