from flask import Flask, request, render_template
from search_engine import search
import pandas as pd
import xlrd

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def graph():
    if request.method == 'POST':
        query = request.form['query']
        src_method = request.form['word']
        questions, answers = search(query, src_method)
        df = pd.dataframe()
        df['Вопросы'] = questions
        df['Ответы'] = answers
    return render_template('result.html')

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)