from getdata import getdata
import pandas as pd
from search_bm25 import topthree_bm25
from calculate_tfidf import topthree_tfidf
from pre_processing import preprocess, presets

X = getdata()
presets()
df_final = pd.read_excel("dffinal.xlsx")
questions = df_final['questions'].values.tolist()
answers = df_final['answers'].values.tolist()

def search(query, search_method):
    answer_result = []
    corpus = df_final['lemmas'].values.tolist()
    query = preprocess(query)
    search_result = []
    if search_method == 'tf-idf':
        f_q = []
        f_q.append(query)
        vect_query = vectorizer.transform(f_q)
        search_result = topthree_tfidf(vect_query, X)
    elif search_method == 'bm25':
        search_result = topthree_bm25(query, corpus)
    else:
        raise TypeError('unsupported search method')
    if len(search_result) > 0:
        for result in search_result:
            answer = answers[questions.index(result)]
            answer_result.append(answer)

    return search_result, answer_result

