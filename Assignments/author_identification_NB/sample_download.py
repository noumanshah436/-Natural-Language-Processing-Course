# import nltk
# nltk.download('gutenberg')

# from nltk.corpus import gutenberg

# print(gutenberg.fileids())

from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
import pandas as pd

author_map = {
    "Jane Austen": ["austen-emma.txt", "austen-persuasion.txt", "austen-sense.txt"],
    "Herman Melville": ["melville-moby_dick.txt"],
    "Shakespeare": [
        "shakespeare-caesar.txt",
        "shakespeare-hamlet.txt",
        "shakespeare-macbeth.txt",
    ],
    "Lewis Carroll": ["carroll-alice.txt"],
    "William Blake": ["blake-poems.txt"],
    "G. K. Chesterton": [
        "chesterton-ball.txt",
        "chesterton-brown.txt",
        "chesterton-thursday.txt",
    ],
    "John Milton": ["milton-paradise.txt"],
    "Walt Whitman": ["whitman-leaves.txt"],
    "Maria Edgeworth": ["edgeworth-parents.txt"],
    "Thomas Bryant": ["bryant-stories.txt"],
    "Thornton Burgess": ["burgess-busterbrown.txt"],
}

data = {"text": [], "author": []}

for author, files in author_map.items():
    for f in files:
        text = gutenberg.raw(f)
        sentences = sent_tokenize(text)

        for s in sentences:
            if len(s.split()) > 5:
                data["text"].append(s)
                data["author"].append(author)

df = pd.DataFrame(data)

df.to_csv("gutenberg_authors_dataset_extended.csv", index=False)

print("Saved CSV with", len(df), "samples.")
print("Authors included:", df["author"].unique())
print(df["author"].value_counts())
