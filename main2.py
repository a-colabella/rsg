# Random Sentence Generator
# Created by Andrew Colabella
#Fix a/an
#Fix plurality

import random

def nouns(seed1, seed2): #Random noun gen
    file_name = "nouns" + seed1 + ".txt"
    fp = open(file_name)
    for i, line in enumerate(fp):
        if i == seed2:
            line = line.replace("\n","")
            return[line]

def adjectives(seed1, seed2): #Random adj gen
    file_name = "adjectives" + seed1 + ".txt"
    fp = open(file_name)
    for i, line in enumerate(fp):
        if i == seed2:
            line = line.replace("\n","")
            return[line]

def verbs(seed1, seed2): #random past-tense verb gen
    file_name = "verbs" + seed1 + ".txt"
    fp = open(file_name)
    for i, line in enumerate(fp):
        if i == seed2:
            line = line.replace("\n","")
            return[line]

def subjectpronouns(seed): #random subject prononouns gen
    fp = open("subjectpronouns.txt")
    for i, line in enumerate(fp):
        if i == seed:
            line = line.replace("\n","")
            return[line]

def objectpronouns(seed): #random object pronouns gen
    fp = open("objectpronouns.txt")
    for i, line in enumerate(fp):
        if i == seed:
            line = line.replace("\n","")
            return[line]

def adverbs(seed1, seed2): #random adverbs gen
    file_name = "adverbs" + seed1 + ".txt"
    fp = open(file_name)
    for i, line in enumerate(fp):
        if i == seed2:
            line = line.replace("\n","")
            return[line]

def prepositions(seed): #random prepositions gen
    fp = open("prepositions.txt")
    for i, line in enumerate(fp):
        if i == seed:
            line = line.replace("\n","")
            return[line]

def conjunctions(seed): #random conjunctions gen
    fp = open("conjunctions.txt")
    for i, line in enumerate(fp):
        if i == seed:
            line = line.replace("\n","")
            return[line]

def interjections(seed): #random interjections gen
    fp = open("interjections.txt")
    for i, line in enumerate(fp):
        if i == seed:
            line = line.replace("\n","")
            return[line]


user_input = input("Enter number of sentences to generate: ")

for i in range (1, int(user_input)+1):
    article_or_no = random.randrange(1,3) #Use article?
    noun_or_pro = random.randrange(1,5) #Use noun or pronoun?
    adj_or_no = random.randrange(1,3) #Use adjective?
    adv_or_no = random.randrange(1,3) #Use adverb?
    prep_or_no = random.randrange(1,3) #Use preposition?
    interj_or_no = random.randrange(1,41) #Use interjection?
    conj_or_no = random.randrange(1,3) #Use conjunction?
    obj_or_no = random.randrange(1,3) #Use object?

    verb_seed1 = str(random.randrange(1,6))
    verb_seed2 = random.randrange(1,201)
    verb = str(verbs(verb_seed1,verb_seed2)).strip("[]").strip("'") + " " #Get random verb
    #ARTICLE
    if article_or_no == 1 and noun_or_pro == 1: #Article
        the_or_a = random.randrange(1,3)
        if the_or_a == 1:
            article = "the "
        else:
            article = "a/an "
    else:
        article = ""
    #INTERJECTION
    if interj_or_no == 1: #Interjection
        interjection_seed = random.randrange(1,28)
        interjection = str(interjections(interjection_seed)).strip("[]").strip("'") + " "
    else:
        interjection = ""
    #NOUN
    if noun_or_pro == 1: #Pronoun
        sub_pronoun_seed = random.randrange(1, 31)
        noun = str(subjectpronouns(sub_pronoun_seed)).strip("[]").strip("'") + " "
    else:#Noun
        noun_seed1 = str(random.randrange(1, 17))
        noun_seed2 = random.randrange(1, 277)
        noun = str(nouns(noun_seed1, noun_seed2)).strip("[]").strip("'") + " "
    #ADJECTIVE
    if adj_or_no == 1 and noun_or_pro ==1:
        adj_seed1 = str(random.randrange(1,11))
        adj_seed2 = random.randrange(1,136)
        adjective = str(adjectives(adj_seed1,adj_seed2)).strip("[]").strip("'") + " "
    else:
        adjective = ""
    #ADVERB
    if adv_or_no == 1:
        adv_seed1 = str(random.randrange(1,3))
        adv_seed2 = random.randrange(1,201)
        adverb = str(adverbs(adv_seed1,adv_seed2)).strip("[]").strip("'") + " "
    else:
        adverb = ""
    #OBJECT
    if obj_or_no == 1 or prep_or_no ==1: #yes, add object
        obj_seed1 = str(random.randrange(1,17))
        obj_seed2 = random.randrange(1,277)
        obj_pro_or_no = random.randrange(1,3) #object pronoun?
        obj_article_or_no = random.randrange(1,3) #object article?
        obj_adjective_or_no = random.randrange(1,3) #object adjective?

        if obj_article_or_no == 1 and obj_pro_or_no == 1:  # yes article (no pronoun)
            the_or_a = random.randrange(1, 3)
            if the_or_a == 1:
                obj_article = "the "
            else:
                obj_article = "a/an "
        else:
            obj_article = ""

        if obj_adjective_or_no == 1 and obj_pro_or_no == 1: #yes adjective (no pronoun)
            adj_seed1 = str(random.randrange(1, 11))
            adj_seed2 = random.randrange(1, 136)
            obj_adjective = str(adjectives(adj_seed1, adj_seed2)).strip("[]").strip("'") + " "
        else:
            obj_adjective = ""

        if obj_pro_or_no == 1:  # Object Noun
            noun_seed1 = str(random.randrange(1, 17))
            noun_seed2 = random.randrange(1, 277)
            obj_noun = str(nouns(noun_seed1, noun_seed2)).strip("[]").strip("'")
        else:  # Object Pronoun
            ob_pronoun_seed = random.randrange(1, 42)
            obj_noun = str(objectpronouns(ob_pronoun_seed)).strip("[]").strip("'")

        object = obj_article + obj_adjective + obj_noun
    else: #no object
        object = ""
    #PREPOSITION
    if prep_or_no == 1:
        prep_seed = random.randrange(1,98)
        preposition = str(prepositions(prep_seed)).strip("[]").strip("'") + " "
    else:
        preposition = ""


    sentence = interjection + article + adjective + noun + adverb + verb + preposition + object + "."
    print(sentence.capitalize())