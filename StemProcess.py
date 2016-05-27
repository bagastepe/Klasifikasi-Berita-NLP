from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from textblob import TextBlob as tb
from StopWords import get_stop
import sys

stop_words = set(get_stop())

# create stemmer Sastrawi
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def get_berita(url):
    teks = """

    """
    fo = open(url)

    teks = fo.read()

    fo.close()

    return teks

def stem_words(url,type="text"):

    if type != "text":
        output = get_berita(url)
    else:
        output = url

    sentence2 = tb(output.lower())
    word_token = sentence2.words
    # print(word_token)

    filtered_sentence = []

    for w in word_token:
        if w == "perbankan":
            w = "bank"
        w = stemmer.stem(w)
        if w not in stop_words:

            filtered_sentence.append(w)

    #print(" ".join(filtered_sentence),"\n")
    return " ".join(filtered_sentence)
