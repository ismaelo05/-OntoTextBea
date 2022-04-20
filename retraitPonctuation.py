import string

def remove_ponctuation_sign(text):
    # Chargement des charactères de ponctuaction dans une liste
    liste = []
    translate_table = dict((ord(char), None) for char in string.punctuation)
    for doc in text:
        doc = str(doc)
        # Soustraire les caractères de ponctuations dans le corpus
        text1 = doc.translate(translate_table)
        liste.append(text1)
    return liste

def remove_ponctuation_sign1(text):
    # Chargement des charactères de ponctuaction dans une liste
    translate_table = dict((ord(char), None) for char in string.punctuation)
    # Soustraire les caractères de ponctuations dans le corpus
    text = str(text)
    text1 = text.translate(translate_table)
    return text1