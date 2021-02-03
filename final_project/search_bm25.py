from calculate_bm25 import bm25

def topthree_bm25(query, corpus):
    bms = {}
    query = query.split()
    for document in corpus:
        bm = bm25(query, document, corpus)
        bms[document] = bm

    dict1 = bm
    sorted_values = sorted(dict1.values())  # Sort the values
    sorted_dict = {}
    results = []
    o = 0
    for i in sorted_values:
        for k in dict1.keys():
            if dict1[k] == i:
                sorted_dict[k] = dict1[k]
                break
    for d in sorted_dict:
        if o == 3:
            break
        results.append(d)
        o += 1
    return results
