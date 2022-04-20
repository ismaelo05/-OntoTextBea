import itertools
from nltk.corpus import wordnet


def synonymes(termes, output):
    termes_synonyme =[]
    for terme in termes:
        syns = [syn.lemma_names('fra') for syn in wordnet.synsets(terme, lang='fra')]
        syns = list(itertools.chain(*syns))
        # print(syns)
        inter = set(syns).intersection(set(output))
        if len(inter) > 0 and inter not in termes_synonyme:
            d = {terme: list(inter)}
            while len(inter) > 0:
                a = inter.pop()
                termes_synonyme.append(a)
    return termes_synonyme