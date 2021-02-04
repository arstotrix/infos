import pandas as pd
from pre_processing import presets, preprocess

def getdata():
    presets()
    ans_path = 'answers_base.tsv'
    que_path = 'queries_base.tsv'
    df_que = pd.read_csv(que_path, sep='\t')
    df_ans = pd.read_csv(ans_path, sep='\t')
    df_que = df_que.drop(['Unnamed: 3', 'Unnamed: 4'], axis=1)
    df_que = df_que.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    df_ans = df_ans.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    questions = df_que['Текст вопроса'].values.tolist()
    link_numbers_q = df_que['Номер связки'].values.tolist()
    link_numbers_a = df_ans['Номер связки'].values.tolist()
    answers = df_ans['Текст ответа'].values.tolist()
    questions_answers = []
    for i, question in enumerate(questions):
        linked_number = link_numbers_q[i]
        ind_answer = link_numbers_a.index(linked_number)
        answer = answers[ind_answer]
        questions_answers.append(answer)
    corpus = []
    for question in questions:
        entry = preprocess(question)
        corpus.append(entry)
        print("Обработка данных: ", len(corpus), " из", len(questions))
    global df_final
    df_final = pd.DataFrame()
    df_final['questions'] = questions
    df_final['answers'] = answers
    df_final['lemmas'] = corpus
    df_final.to_csv("dffinal.tsv", sep = '\t')
    X = vectorizer.fit_transform(corpus)
    print("Корпус успешно векторизован")
    return X