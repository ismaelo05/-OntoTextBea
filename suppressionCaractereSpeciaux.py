import re

from nltk import word_tokenize
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop
from spacy.lang.en.stop_words import STOP_WORDS as en_stop


def supprimer_caractere_speciaux_sauf_espace(s):
    for a in s:
        text = ''.join([l for l in a if l.isalnum() or l == ' '])
    return text


def lemmanisation_corpus(text):
    # Crée une liste de mots contenant les mots racines
    output = []
    for token in text:
        tokens = []
        for tok in token:
            if tok.pos_ != 'SPACE':
                tokens.append(tok.lemma_)
        output.append(tokens)
    return output


def lemmanisation_corpus2(text):
    # Crée une liste de mots contenant les mots racines
    output = []
    for token in text:
        tokens = []
        for tok in token:
            if tok.pos_ != 'SPACE' and tok.pos_ != 'NUM' and tok.pos_ != 'PUNCT' and tok.pos_ != 'PRON' and tok.pos_ != 'DET' and tok.pos_ != 'DET' and tok.pos_ != 'DET':
                tokens.append(tok.lemma_)
        output.append(tokens)
    return output

def lemmanisation_corpus1(text):
    # Crée une liste de mots contenant les mots racines
    tokens = []
    for token in text:
        # print(token.pos_)
        if token.pos_ != 'SPACE' and token.pos_ != 'NUM' and token.pos_ != 'PUNCT' and token.pos_ != 'PRON' and token.pos_ != 'DET' and token.pos_ != 'VERB':
            tokens.append(token.lemma_)
            # print(token, token.pos_)
    return tokens

def lemmanisation_corpus3(text):
    # Crée une liste de mots contenant les mots racines
    tokens = []
    for token in text:
        # print(token.pos_)
        if token.pos_ != 'SPACE':
            tokens.append(token.lemma_)
            # print(token, token.pos_)
    return tokens

def supprimer_stop_words(text):
    # Création d'une liste de l'alphabet et de différents types d'espace
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', '-', '\xa0', '\xa0 ', '\x88', '\x88 ', '\n', ')', '(', ',', '.',"'",'--', ':', '!','...', '/'
        , '[', ']', '%', '<', '>', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', '’', '*', '+', '' ,';', '?', '-',
         '\uf0a7', '=', '�', '//www.bea.aero', '//leafletjs.com', '|', '', 'www.bea.aero', 'www.bea.ci', '‘', 'tx_news_pi1',
         '5d', '/les', 'https', '/le', 'rapport', 'non', '5d=1761', 'c3', 'min', '5d=1288', '5d=77', '5d=1533', '5d=2007', '20bea',
         'stateareaofocc_string', '20et', 'injurylevel_string', 'highestdamage_strings', 'occurrenceclass_strings', 'a0',
         '20fix', 'operator_string' 'operationtype_strings', '20non', 'ii', 'qu', 'pal', 'manufacturermodel_string', '313b',
         'civ', '00', 'pp', 'scf', 'ag', 'http', 'ée', 'ulm', 'htt', '02', '20-', '5d=288', '5baction', 'non' , 'https://www.bea.aero/les-enquetes/evenements-notifies',
         'chash=52d556168ae6cc55531098f2e309a06a', 'cea%20-%20dr315&tx_news_pi1%5bnews%5d=1533', 'tx_news_pi1%5bfacetvalue%5d',
         'http://leafletjs.com', 'france%20-%20bea', 'stateareaofocc_strings', 'europe%20et%20atlantique%20nord%20-%20france%20-%2003%20allier'
         'tx_news_pi1%5bnews%5d=1288&chash', 'cf528c5958f220405c35fa9f338a028d', 'notifies/?tx_news_pi1%5baction%5d', '/?tx_news_pi1%5baction%5d', 'tx_news_pi1%5bnews%5d=1533&chash=485b49883c29d21d7866b22b0e8a9c44',
         'tx_news_pi1%5bcontroller%5d', 'tx_news_pi1%5bnews%5d=1533&chash=5f3c0d92ad952789604e337c0467e7e2', 'https://www.bea.aero/les-enquetes/evenements-notiﬁes',
         'europe%20et%20atlantique%20nord%20-%20france%20-%2051%20marne', 'tx_news_pi1%5bfacetaction%5d add&tx_news_pi1%5bfacettitle%5d', 'tx_news_pi1%5bnews%5d=1533&chash=6d3fbc90394853cbbce783bb7520bfb0',
         'tx_news_pi1%5bnews%5d=1533&chash=4d8b0c0d516b0a23921e68131505c57e', 'occurrenceclass_strings&tx_news_pi1%5bfacetvalue%5d', 'occurrence tx_news_pi1%5bfacettitle%5d',
         'news&tx_news_pi1%5bfacetaction%5d', 'tx_news_pi1%5bnews%5d=1533&chash=846b9475c81344d38fc157e42190a242', 'tx_news_pi1%5bfacettitle%5d',
         'exploitations%20non%20commerciales%20-%20loisir', 'tx_news_pi1%5bfacetaction%5d', 'operationtype_strings', 'tx_news_pi1%5bnews%5d=1533&chash=9a9093f38f0c25ad19cbb27daff7bee6',
         'searchresult&tx_news_pi1%5bcontroller%5d', 'year_ints&tx_news_pi1%5bfacetvalue%5d=2007', 'c369eb3d674800b1ddb7a3e4fe2831fa',
         'tx_news_pi1%5bnews%5d=1288&chash=04b12e2be71661229a082cb96f2a4096', 'responsibleentity_strings&tx_news_pi1%5bfacetvalue%5d', 'europe%20et%20atlantique%20nord%20-%20france%20-%2003%20allier',
         'tx_news_pi1%5bnews%5d=1288&chash', 'injurylevel_strings&tx_news_pi1%5bfacetvalue%5d', 'tx_news_pi1%5bnews%5d=1288&chash=52959d444ef18ed235e6a36f5a46e92f',
         'tx_news_pi1%5bnews%5d=1288&chash=58b6a5a49285db03b51d31fa7e7265ca', 'd%c3%a9truit', 'add&tx_news_pi1%5bfacettitle%5d', 'aircraftcategory_strings',
         'a%c3%a9ronef%20%c3%a0%20voilure%20fixe%20-%20avion', 'bccdd18887ed35ddefdb2ce4cc070b0f', 'bc97cfe86626430b13a88742b84f8e5c',  'bef16e13b321c21a26bd110d1bd66515', 'bd0d71125aa74f5b073379bd99a47e43',
         'bee3b4a0cc07221eae043bd36f99434e', 'tx_news_pi1%5bnews%5d=1761&chash=7aa79036d285b21cc53da035e27666da', 'europe%20et%20atlantique%20nord%20-%20france%20-%2060%20oise&tx_news_pi1%5bnews%5d=1761',
          'chash=4f23e85e7b8cd134e40f3eeb1aab3bac', 'tx_news_pi1%5bnews%5d=1761&chash=24257af226bfa608fbe4e37f6596d879', 'tx_news_pi1%5bnews%5d=1761&chash', 'da2b6ff4ce394e9abf611448e1116e27',
         'tx_news_pi1%5bnews%5d=1761&chash=0f24e71864277924ea8dda0530fc46d9', 'aircraftcategory_strings&tx_news_pi1%5bfacetvalue%5d', 'a%c3%a9ronef%20%c3', 'a0%20voilure%20fixe%20-%20ulm&tx_news_pi1%5bnews%5d=1761&chas',
         'tx_news_pi1%5bnews%5d=1761&chash=1379c18bbce1496bac8ee659cee99ff1', 'b0b979620e70c59661a79d03f443fbe0', 'manufacturermodel_strings&tx_news_pi1%5bfacetvalue%5d', 'a97c737eee567ecd320bdd2a70c39598',
         'a7fa9db9a65a9fe18b4e10a316be7425', 'a5045d259b6825e016b1c34c005d18a7', 'a46584b3de45918f5cd54f239fb0823e', 'a3647b849911bff36d76fc747aab4170', 'c369eb3d674800b1ddb7a3e4fe2831fer',
         'dd1a2ffac8358d8e84699c7fd8a6ea7b', 'e392eb633c174a45bb4074d915ae67ber', 'e77ba4c2736315a3849174c0732802bf']
    # Ajout de cette liste dans la liste de nos stops words
    stop_word = list(fr_stop) + a
    # Elimination des stops words dans le corpus de listes de mots
    output = []
    for token in text:
        doc = []
        for tok in token:
            # tok = word_tokenize(re.sub(r"[^a-zA-Z- ]", "", "".join(tok)))
            # tok = str(" ".join(tok))
            if tok not in stop_word:
                if ('.' not in tok) and ('-' not in tok) and ('=' not in tok) and (':' not in tok) and (
                        '_' not in tok) and ('%' not in tok):
                    doc.append(tok)
        output.append(doc)
    return output

def supprimer_stop_words1(text):
    # Création d'une liste de l'alphabet et de différents types d'espace
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', '', '\xa0', '\xa0 ', '\x88', '\x88 ', '\n', ' ', ')', '(', ',', '.',"'",'--', ':', '!','...', '/'
        , '[', ']', '%', '<', '>', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', '’', '*', '+', '' ,';', '?', '-',
         '\uf0a7', '=', '�', '//www.bea.aero', '//leafletjs.com', '|', '', 'www.bea.aero', 'www.bea.ci', '‘', 'tx_news_pi1'
         , '5d', '/les', 'https', '/le', 'rapport' 'non', '5d=1761', 'c3', 'min', '5d=1288', '5d=77', '5d=1533', '5d=2007', '20bea',
         'stateareaofocc_string', '20et', 'injurylevel_string', 'highestdamage_strings', 'occurrenceclass_strings', 'a0',
         '20fix', 'operator_string' 'operationtype_strings', '20non', 'ii', 'qu', 'pal', 'manufacturermodel_string', '313b',
         'civ', '00', 'pp', 'scf', 'ag', 'http', 'ée', 'ulm', 'htt', '02', '20-', '5d=288', '5baction', 'non', 'https://www.bea.aero/les-enquetes/evenements-notifies',
         'chash=52d556168ae6cc55531098f2e309a06a', 'cea%20-%20dr315&tx_news_pi1%5bnews%5d=1533', 'tx_news_pi1%5bfacetvalue%5d',
         'http://leafletjs.com', 'france%20-%20bea', 'stateareaofocc_strings', 'europe%20et%20atlantique%20nord%20-%20france%20-%2003%20allier'
         'tx_news_pi1%5bnews%5d=1288&chash', 'cf528c5958f220405c35fa9f338a028d', 'notifies/?tx_news_pi1%5baction%5d', '/?tx_news_pi1%5baction%5d', 'tx_news_pi1%5bnews%5d=1533&chash=485b49883c29d21d7866b22b0e8a9c44',
         'tx_news_pi1%5bcontroller%5d', 'tx_news_pi1%5bnews%5d=1533&chash=5f3c0d92ad952789604e337c0467e7e2', 'https://www.bea.aero/les-enquetes/evenements-notiﬁes',
         'europe%20et%20atlantique%20nord%20-%20france%20-%2051%20marne', 'tx_news_pi1%5bfacetaction%5d add&tx_news_pi1%5bfacettitle%5d', 'tx_news_pi1%5bnews%5d=1533&chash=6d3fbc90394853cbbce783bb7520bfb0',
         'tx_news_pi1%5bnews%5d=1533&chash=4d8b0c0d516b0a23921e68131505c57e', 'occurrenceclass_strings&tx_news_pi1%5bfacetvalue%5d', 'occurrence tx_news_pi1%5bfacettitle%5d',
         'news&tx_news_pi1%5bfacetaction%5d', 'tx_news_pi1%5bnews%5d=1533&chash=846b9475c81344d38fc157e42190a242', 'tx_news_pi1%5bfacettitle%5d',
         'exploitations%20non%20commerciales%20-%20loisir', 'tx_news_pi1%5bfacetaction%5d', 'operationtype_strings', 'tx_news_pi1%5bnews%5d=1533&chash=9a9093f38f0c25ad19cbb27daff7bee6',
         'searchresult&tx_news_pi1%5bcontroller%5d', 'year_ints&tx_news_pi1%5bfacetvalue%5d=2007', 'c369eb3d674800b1ddb7a3e4fe2831fa',
         'tx_news_pi1%5bnews%5d=1288&chash=04b12e2be71661229a082cb96f2a4096', 'responsibleentity_strings&tx_news_pi1%5bfacetvalue%5d', 'europe%20et%20atlantique%20nord%20-%20france%20-%2003%20allier',
         'tx_news_pi1%5bnews%5d=1288&chash', 'injurylevel_strings&tx_news_pi1%5bfacetvalue%5d', 'tx_news_pi1%5bnews%5d=1288&chash=52959d444ef18ed235e6a36f5a46e92f',
         'tx_news_pi1%5bnews%5d=1288&chash=58b6a5a49285db03b51d31fa7e7265ca', 'd%c3%a9truit', 'add&tx_news_pi1%5bfacettitle%5d', 'aircraftcategory_strings',
         'a%c3%a9ronef%20%c3%a0%20voilure%20fixe%20-%20avion', 'bccdd18887ed35ddefdb2ce4cc070b0f', 'bc97cfe86626430b13a88742b84f8e5c',  'bef16e13b321c21a26bd110d1bd66515', 'bd0d71125aa74f5b073379bd99a47e43',
         'bee3b4a0cc07221eae043bd36f99434e', 'tx_news_pi1%5bnews%5d=1761&chash=7aa79036d285b21cc53da035e27666da', 'europe%20et%20atlantique%20nord%20-%20france%20-%2060%20oise&tx_news_pi1%5bnews%5d=1761',
          'chash=4f23e85e7b8cd134e40f3eeb1aab3bac', 'tx_news_pi1%5bnews%5d=1761&chash=24257af226bfa608fbe4e37f6596d879', 'tx_news_pi1%5bnews%5d=1761&chash', 'da2b6ff4ce394e9abf611448e1116e27',
         'tx_news_pi1%5bnews%5d=1761&chash=0f24e71864277924ea8dda0530fc46d9', 'aircraftcategory_strings&tx_news_pi1%5bfacetvalue%5d', 'a%c3%a9ronef%20%c3', 'a0%20voilure%20fixe%20-%20ulm&tx_news_pi1%5bnews%5d=1761&chas',
         'tx_news_pi1%5bnews%5d=1761&chash=1379c18bbce1496bac8ee659cee99ff1', 'b0b979620e70c59661a79d03f443fbe0', 'manufacturermodel_strings&tx_news_pi1%5bfacetvalue%5d', 'a97c737eee567ecd320bdd2a70c39598',
         'a7fa9db9a65a9fe18b4e10a316be7425', 'a5045d259b6825e016b1c34c005d18a7', 'a46584b3de45918f5cd54f239fb0823e', 'a3647b849911bff36d76fc747aab4170', 'c369eb3d674800b1ddb7a3e4fe2831fer',
         'dd1a2ffac8358d8e84699c7fd8a6ea7b', 'e392eb633c174a45bb4074d915ae67ber', 'e77ba4c2736315a3849174c0732802bf']
    # Ajout de cette liste dans la liste de nos stops words
    stop_word = list(fr_stop) + a
    # Elimination des stops words dans le corpus de listes de mots
    output = []
    for token in text:
        # token = word_tokenize(re.sub(r"[^a-zA-Z- ]", "", "".join(token)))
        # token = str(" ".join(token))
        if token not in stop_word:
            if ('.' not in token) and ('-' not in token) and ('=' not in token) and (':' not in token)and ('_' not in token) and ('%' not in token):
                output.append(token)
    return output