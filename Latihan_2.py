#eksperiment menggunakan variabel berbeda-beda
import nltk
from nltk.tokenize import sent_tokenize

paragraf1 = "Siang Siang enak mokel nih"
paragraf2 = "Bentar lagi Lebaran. Mohon maaf lahir Batin"
kalimat = "Baju baru Alhamdulillah."

sentences1 = sent_tokenize(kalimat)
sentences2 = sent_tokenize(paragraf1)
sentences3 = sent_tokenize(paragraf2)


print("Tokenized Sentences 1:", sentences1)
print("Tokenized Sentences 2:", sentences2)
print("Tokenized Sentences 3:", sentences3)

