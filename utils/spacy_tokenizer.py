import spacy
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
STOPWORDS = set(stopwords.words('english'))

def tokenize(text):
    doc = nlp(text.lower())
    
    tokens = [
        token.text
        for token in doc
        if token.is_alpha and token.text not in STOPWORDS
    ]
    
    return tokens


