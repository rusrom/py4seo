# import language_check
from collections import defaultdict, OrderedDict
from pprint import pprint
from nltk import sent_tokenize, word_tokenize, ngrams
from nltk.stem import snowball
from heapq import nlargest
from googletrans import Translator


# text = '''
# Юрий Гагарин – советский летчик, биографию которого каждый 
# знает еще со школы. Гагарин -  человек, совершивший первый 
# полет в космос. Летчик-космонавт стал образцом и легендой не 
# только для жителей СССР, он почетный гражданин заграничных 
# городов и международный общественный деятель. Юрий Алексеевич 
# открыл новую страницу в исследовании космоса и стал символом 
# развития советской науки и авиации.

# Юрий Алексеевич Гагарин родился 9 марта 1934 года в деревушке 
# Клушино, в Западной области СССР, в семье зажиточных крестьян. 
# Мальчик был третьим из четверых детей. Детство Юры проходило 
# спокойно и радостно, отец и мать уделяли ему много внимания. 
# Алексей Иванович, глава семейства, много занимался поделками 
# из дерева и с удовольствием приобщал к этому детей.
# '''


# translator = Translator()
# result = translator.translate(text, src='ru', dest='uk')

# print(result.text)

# sentences = sent_tokenize(text)


# for sent in sentences:
# 	if 'космонавт' in sent:
# 		sent_kos = sent
# 		break

# # print(sentences)

# words = word_tokenize(text)
# grams2 = ngrams(words, 2)
# grams3 = ngrams(words, 3)

# for gr in grams2:
# 	kw = ' '.join(gr)
# 	print(kw)


# for gr in grams3:
# 	kw = ' '.join(gr)
# 	print(kw)





# stemmer = snowball.SnowballStemmer("russian")
# res = stemmer.stem('четверых')

# print(res)

# quit()

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


with open('ga.txt', 'r') as f:
	gagarin_text = f.read()

# summary = text_summary(gagarin_text, 2)

fw = words_frequercy(gagarin_text, n=20)

pprint(fw)

# print(summary)


def distance(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n+1) # Keep current and previous row, not entire matrix
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1,n+1):
            add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]



result = distance('Гагарин', 'Юрий')

print(result)