# import language_check

from pprint import pprint

from nltk import sent_tokenize, word_tokenize, ngrams
from nltk.stem import snowball


text = '''
Юрий Гагарин – советский летчик, биографию которого каждый 
знает еще со школы. Гагарин -  человек, совершивший первый 
полет в космос. Летчик-космонавт стал образцом и легендой не 
только для жителей СССР, он почетный гражданин заграничных 
городов и международный общественный деятель. Юрий Алексеевич 
открыл новую страницу в исследовании космоса и стал символом 
развития советской науки и авиации.

Юрий Алексеевич Гагарин родился 9 марта 1934 года в деревушке 
Клушино, в Западной области СССР, в семье зажиточных крестьян. 
Мальчик был третьим из четверых детей. Детство Юры проходило 
спокойно и радостно, отец и мать уделяли ему много внимания. 
Алексей Иванович, глава семейства, много занимался поделками 
из дерева и с удовольствием приобщал к этому детей.
'''

# Get all sentences
sentences = sent_tokenize(text)
pprint(sentences)

# Find sentences containing word 'деятель'
sentences_with_world = [sent for sent in sentences if 'деятель' in sent]
pprint(sentences_with_world)

# Get words from sentence
words = word_tokenize(sentences_with_world[0])
pprint(words)

# Split on ngrams (2 words) words from sentence containing 'деятель'
grams = ngrams(words, 2)
print(list(grams))

# ngrams (3 words) for all text
words = word_tokenize(text)
grams = ngrams(words, 3)
print('-' * 50)
# pprint(list(grams))

# Keywords from ngrams
for gram in grams:
    keyword = ' '.join(gram)
    print(keyword)