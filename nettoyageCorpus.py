import textcleaner as tc #or

def mise_en_miniscule(text):
    # Crée un objet nommé data de la classe document tout en mettant
    # les caractères du corpus en minuscule
    liste = []
    for doc in text:
        data = tc.document(doc.lower())
        liste.append(data)
    # print(liste[0])
    return liste


def mise_en_miniscule1(text):
    # Crée un objet nommé data de la classe document tout en mettant
    # les caractères du corpus en minuscule
    data = tc.document(text.lower())
    return data

def remove_empty_line(text):
    # Supprime les lignes vides de l'objet data
    liste = []
    for doc in text:
        data = doc.clear_blank_lines()
        liste.append(data)
    # print(liste[0])
    return liste

def remove_empty_line1(text):
    # Supprime les lignes vides de l'objet data
    data = text.clear_blank_lines()
    return data