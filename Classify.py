from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob as tb
from StemProcess import stem_words
import traintes
from tabulate import tabulate


# feature yang dipilih
def feature_extractor(text):
    if not isinstance(text, tb):
        text = tb(text.lower())

    return {
        'has_harga': 'harga' in text.words,
        'has_persen': 'persen' in text.words,
        'has_saham': 'saham' in text.words,
        'has_ihsg': 'ihsg' in text.words,
        'has_pasar': 'pasar' in text.words,
        'has_ketua': 'pemasaran' in text.words,
        'has_hukum': 'saham' in text.words,
        'has_partai': 'partai' in text.words,
        'has_konvensi': 'konvensi' in text.words,
        'has_menteri': 'menteri' in text.words,
        'has_buku': 'buku' in text.words,
        'has_ui': 'ui' in text.words,
        'has_didik': 'didik' in text.words,
        'has_mahasiswa': 'mahasiswa' in text.words,
        'has_universitas': 'universitas' in text.words,
        'starts_with_[': text[0] == '['
    }

cl = NaiveBayesClassifier(traintes.train,feature_extractor=feature_extractor)

# print("Accuracy: {0}".format(round(cl.accuracy(traintes.test),9)))

pp=0
pe=0
pd=0
ee=0
ep=0
ed=0
dd=0
dp=0
de=0
for i in traintes.test1:
    if (cl.classify(i[0])=="politik"):
        pp+=1
    elif (cl.classify(i[0])=="ekonomi"):
        pe+=1
    elif (cl.classify(i[0])=="pendidikan"):
        pd+=1
for i in traintes.test2:
    if (cl.classify(i[0]) == "politik"):
        ep += 1
    elif (cl.classify(i[0]) == "ekonomi"):
        ee += 1
    elif (cl.classify(i[0]) == "pendidikan"):
        ed += 1
for i in traintes.test3:

    if (cl.classify(i[0]) == "politik"):
        dp += 1
    elif (cl.classify(i[0]) == "ekonomi"):
        de += 1
    elif (cl.classify(i[0]) == "pendidikan"):
        dd += 1

acp = cl.accuracy(traintes.test1)
ace = cl.accuracy(traintes.test2)
acd = cl.accuracy(traintes.test3)

table=[["politik",pp,pe,pd,acp],["ekonomi",ep,ee,ed,ace],["pendidikan",dp,de,dd,acd]]
header =["KATEGORI","politik","ekonomi","pendidikan","akurasi"]
print(tabulate(table,header,tablefmt="grid"))
print("akurasi adalah %f" %cl.accuracy(traintes.test))
print("\n\n")
print(cl.show_informative_features(10))