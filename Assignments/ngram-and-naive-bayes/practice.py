import nltk
from nltk.util import ngrams
from nltk.corpus import reuters, movie_reviews
from collections import Counter, defaultdict
import math, random, numpy as np
from sklearn.model_selection import train_test_split

# Download corpora (only the first time)
# nltk.download('reuters')
# nltk.download('movie_reviews')
# nltk.download('punkt')
from nltk import sent_tokenize, word_tokenize

# Load manually if punkt_tab missing
text = " ".join(reuters.words(categories='acq')[:5000])
docs = [word_tokenize(sent) for sent in sent_tokenize(text)]


# Load sentences from Reuters (acq category)
# docs = reuters.sents(categories='acq')[:2000]
# Flatten tokens and add sentence boundary tokens
tokens = ['<s>'] + [w.lower() for sent in docs for w in sent] + ['</s>']

# Helper to build n-gram counts
def build_ngram_counts(tokens, n):
    return Counter(ngrams(tokens, n))

unigram_counts = build_ngram_counts(tokens, 1)
bigram_counts = build_ngram_counts(tokens, 2)
trigram_counts = build_ngram_counts(tokens, 3)

V = len(set(tokens))  # vocabulary size

print('Vocabulary size V =', V)
print('Sample unigram counts (top 10):', unigram_counts.most_common(10))
print('Sample bigram counts (top 10):', bigram_counts.most_common(10))
