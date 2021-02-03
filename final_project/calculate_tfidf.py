import numpy as np
from sklearn.metrics.pairwise import linear_kernel

def topthree_tfidf(vec_query, X):
    vec_query = vec_query.toarray()
    cs = linear_kernel(vec_query, X).flatten()
    result = cs.argsort()[:-3:-1]
    return result



