# Simple tokenizer for BM25 application.

import re
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def tokenize(text):
    text = text.lower()
    
    # remove punctuation
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    tokens = text.split()
    
    # remove stopwords
    tokens = [t for t in tokens if t not in STOPWORDS]
    
    return tokens