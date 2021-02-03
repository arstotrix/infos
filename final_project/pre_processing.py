import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
import pymorphy2
import string
from sklearn.feature_extraction.text import TfidfVectorizer

def presets():
  global vectorizer
  vectorizer = TfidfVectorizer()
  global morph
  morph = pymorphy2.MorphAnalyzer()
  global sting
  sting = string.punctuation + '1234567890'
  global stop_words
  stop_words = set(stopwords.words("russian"))

def preprocess(text):
  text = str(text)
  text = text.lower()
  for s in sting:
    text = text.replace(s,'')
  pretext = nltk.word_tokenize(text)
  for i, element in enumerate(pretext):
      element = morph.parse(element)[0].normal_form
      if element not in stop_words:
        pretext.append(element)
  line = ' '.join(pretext)
  return line

