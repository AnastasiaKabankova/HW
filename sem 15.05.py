import re

with open('news.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()
    
punct = '[.,?!:;"\'—@–...«»#()$%&*—-]' #[a-z0-9]
tabs = '[\t\n]'

def preprocessing(text):
    text = text.strip().lower()
    text = re.sub(punct, '', text)
    text = re.sub(tabs, ' ', text)
    words = text.split()
    return words
words = preprocessing(text)
# print(words[:1000])

def make_freq(arr):
    d = {}
    for el in arr:
        try:
            d[el] += 1
        except KeyError:
            d[el] = 1
    return d
word_freq = make_freq(words)

def make_bigrams(arr):
    bigrams = []
    for i in range(len(words)):
        bigr = arr[i] + ' ' + arr[i + 1]
        bigrams.append(bigr)
    return bigrams
bigrams = make_bigrams(words)
# print(bigrams[:100])
bigrams_freq = make_freq(bigrams)

from math import log

def count_pmi(x, y):
    bigr = x + ' ' + y
    try:
        p_x = word_freq[x]/len(words)
    except KeyError:
        p_x = 0
    try:
        p_y = word_freq[y]/len(words)
    except KeyError:
        p_y = 0
    try:
        p_xy = bigrams_freq[bigr]/len(bigrams)
    except KeyError:
        p_xy = 0
    try:
        pmi = log(p_xy/(p_x*p_y))
    except ZeroDivisionError:
        pmi = 0
    return pmi

def calculate_pmi():
    pmis ={}
    for bigr in bigrams:
        x, y = bigr.split()
        pmi = count_pmi(x, y)
        pmis[bigr] = pmi
    return pmis

pmi = calculate_pmi()
i = 0
for el in sorted(pmi, key = lambda m: -pmi[m]):
    if i > 100:
        break
    print(el, pmi[el])
    i += 1
    
import os

corpus_anek = ''
corpus_izvest = ''
corpus_teh = ''

for root, dirs, files in os. walk('texts'):
    if 'anekdots' in root:
        for f in files:
            with open(os.path.join(root,f), 'r', encoding = 'utf-8') as f1:
                text = f1.read()
                corpus_anek += text
    if 'teh_mol' in root:
        for f in files:
            with open(os.path.join(root,f), 'r', encoding = 'utf-8') as f1:
                text = f1.read()
                corpus_teh += text
    if 'izvest' in root:
        for f in files:
            with open(os.path.join(root,f), 'r', encoding = 'utf-8') as f1:
                text = f1.read()
                corpus_izvest += text

print(corpus_teh[:100])

words_anek = preprocessing(corpus_anek)
words_teh = preprocessing(corpus_teh)
words_izvest = preprocessing(corpus_izvest)
words_all = words_anek + words_teh + words_izvest

freq_anek = make_freq(words_anek)
freq_teh = make_freq(words_teh)
freq_izvest = make_freq(words_izvest)
freq_all = make_freq(words_all)

def count_pmi_cats(word, category):
    p_word = freq_all[word]/len(words_all)
    p_cat = 1/3
    if category == 'anek':
        d = freq_anek
        w = len(words_anek)
    elif category == 'izvest':
        d = freq_izvest
        w = len(words_izvest)
    elif category == 'teh':
        d = freq_teh
        w = len(words_teh)
    p_word_cat = d[word]/w
    pmi = log(p_word_cat/(p_word*p_cat))
    return pmi

for w in words:
    if i > 100:
        break
    try:
        pmi_anek = count_pmi_cats(w, 'anek')
        pmi_izvest = count_pmi_cats(w, 'izvest')
        pmi_teh = count_pmi_cats(w, 'teh')
        max_pmi = max(pmi_anek, pmi_izvest, pmi_teh)
        if max_pmi == pmi_anek:
            print(w, 'anek')
        elif max_pmi == pmi_izvest:
            print(w, 'izvest')
        elif max_pmi == pmi_teh:
            print(w, 'teh')
    except KeyError:
        pass
    i += 1
