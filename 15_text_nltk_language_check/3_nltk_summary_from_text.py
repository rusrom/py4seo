from collections import defaultdict, OrderedDict
from heapq import nlargest

from nltk import sent_tokenize, word_tokenize
from nltk.stem import snowball


__stopwords = ['и', 'а', 'или']


def words_frequercy(text, n=20):
    sents = sent_tokenize(text)
    freq = defaultdict(int)
    stemmer = snowball.SnowballStemmer("russian")
    for sent in sents:
        words = word_tokenize(sent.lower())
        for word in words:
            word = str(stemmer.stem(word))
            if len(word) <= 3:
                continue
            if word in __stopwords:
                continue
            freq[word] += 1
    m = float(sum(freq.values()))
    for w in list(freq.keys()):
        freq[w] = round(freq[w]*100/m, 2)
    return OrderedDict(nlargest(n, freq.items(), key=lambda x: x[1]))


def text_summary(text, n):
    '''Returns n summary sentences from text
    Parameters:
        text (str): String which text.
        n (int): Number of summary sentences.
    '''
    sents = sent_tokenize(text)
    if n >= len(sents):
        return text
    _freq = words_frequercy(text, n=100)
    ranking = defaultdict(float)
    for sent in sents:
        if len(sent) > 300:
    	    continue
        words = word_tokenize(sent.lower())
        for w in words:
            if w in _freq:
                ranking[sent] += _freq[w]
    summary_sents = nlargest(n, ranking.items(), key=lambda x: x[1])
    _summary = [s[0] for s in summary_sents]
    return ' '.join(_summary)


with open('some_text.txt') as f:
    some_text = f.read()

# Описание некоторого текста в 2 предложениях
summary = text_summary(some_text, 5)

print(summary)
