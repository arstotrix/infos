from math import log

def textfreq(word, document):
  tf = 0
  for item in document:
    if item == word:
      tf += 1
  return tf

def invdocfreq(word, corpus):
  n = 0
  N_big = len(corpus)
  for document in corpus:
    document = document.split()
    if word in document:
      n+=1
  if n == 0:
    n = 0.00000001
  idf = log(N_big - n + 0.5 / n + 0.5 )
  return idf

def bm25(query, document, corpus) -> float:
  document = document.split()
  #print(document)
  k = 2.0
  b = 0.75
  okbm = 0
  big_number = 0
  l = len(document)
  avgdl = 0
  for entry in corpus:
    avgdl += len(entry.split())
  avgdl = avgdl/len(corpus)
  #print('avgdl =', avgdl)
  for word in query:
    #print(word)
    tf = textfreq(word, document)
    idf = invdocfreq(word, corpus)
    big_number = tf * (k + 1) / (tf + k * (1 - b + b * (l/avgdl)))
    okbm += idf * big_number
  return okbm