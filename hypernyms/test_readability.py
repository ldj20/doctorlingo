import spacy
from spacy_readability import Readability

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('readability')

doc = nlp("I am some really difficult text to read because I use obnoxiously large words.")

print(doc.fk_grade)
print(doc.fk_ease)
print(doc.dale_chall)
print(doc.smog)
print(doc.coleman_liau_index)
print(doc.automated_readability_index)
print(doc.forcast)

