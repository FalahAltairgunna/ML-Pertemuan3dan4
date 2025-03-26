import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

kalimat = "Agus Lapar Buk."

tokens = word_tokenize(kalimat)

print("Tokenized Words:", tokens)
