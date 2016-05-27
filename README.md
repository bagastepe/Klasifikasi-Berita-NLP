# Klasifikasi-Berita-NLP

## Requirement

1. Download dan Install [Python 3.5](https://www.python.org/downloads/)
2. Install [Sastrawi](https://github.com/har07/PySastrawi)

    ```
    $ pip install Sastrawi
    ```
3. Install [TextBlob](http://textblob.readthedocs.io/)

    ```
    $ pip install -U textblob
    $ python -m textblob.download_corpora
    ```
4. Install [Tabulate](https://pypi.python.org/pypi/tabulate)

    ```
    $ pip install tabulate
    ```

## Penggunaan

Download Zip atau Clone dengan
```
$ git clone https://github.com/bagastepe/Klasifikasi-Berita-NLP.git
$ cd Klasifikasi-Berita-NLP-master
```

### Stemming

Jalankan melalui terminal dengan `$ python StemBerita.py`.

Hasil Stem akan tersimpan pada direktori dokumen *polstem.txt*, *ekostem.txt* dan *pendstem.txt*

### Hitung Akurasi Klasifikasi

Jalankan melalui terminal `$ python Classify.py`

> Hasil Running

> ![Screenshot][classify]
[classify]: https://github.com/bagastepe/Klasifikasi-Berita-NLP/classify_ss.png "Screenshot"




`
