import pandas as pd
ans_path = 'answers_base.tsv'
que_path = 'queries_base.tsv'
df_que = pd.read_csv(que_path, sep='\t')
df_ans = pd.read_csv(ans_path, sep='\t')
df_que = df_que.drop(['Unnamed: 3', 'Unnamed: 4'], axis=1)
print(df_que.head())