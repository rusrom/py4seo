from nltk.stem import snowball


# Search word 'russian' in documentation
# https://www.nltk.org/api/nltk.stem.html
# Russian stemming algorithm
# http://snowball.tartarus.org/algorithms/russian/stemmer.html

stemmer = snowball.RussianStemmer()
res = stemmer.stem('берега')
print(res)
