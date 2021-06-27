import pickle
from nltk import text
from numpy.core.fromnumeric import argmax
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
import pandas as pd
import spacy
import es_core_news_sm
import numpy as np
import codecs




def retrieve_input(texto):
  if(texto==""): return ""
  texto_procesado = str(preprocess(texto))

  loaded_tfidf = pickle.load(open("tf-idf_model.sav", 'rb'))
  transformed_text = loaded_tfidf.transform([texto_procesado])

  loaded_model = pickle.load(open("modelo_datos.sav", 'rb'))
  prediction = loaded_model.predict_proba(transformed_text)

  lista_ods = [
    "Fin de la pobreza",
    "Hambre cero",
    "Salud y bienestar",
    "Educacion de calidad",
    "Igualdad de genero",
    "Agua limpia y saneamiento",
    "Energia asequible y no contaminante",
    "Trabajo decente y crecimiento economico",
    "Industria, Innovacion e Infraestructura",
    "Reduccion de las desigualdades",
    "Ciudades y comunidades sostenibles",
    "Produccion y consumo responsables",
    "Accion por el clima",
    "Vida submarina",
    "Vida de ecosistemas terrestres",
    "Paz, Justicia e Instituciones solidas",
    "Alianzas para lograr los objetivos"
  ]

  print("----- RESULTADOS OBTENIDOS -----")
  print("")
  result = argmax(prediction)
  print(f"  El texto ha sido clasificado como ODS {result+1} -> {lista_ods[result]}")
  print("")
  print("Las probabilidades obtenidas para cada ods son las siguientes:")

  #cambiar lambda por 0 o 1 para tenerlo ordenado o no
  lista = sorted( list(enumerate(prediction[0])),  key = lambda prediction: prediction[1], reverse = True)
  
  for index, val in lista:
    value = prediction[0][index]
    print(f"  ODS {(index+1):<2} - {value:>8.2%}   ->   {lista_ods[index]:<40}")



# Función que elimina los caracteres que tienen algunos textos del csv al principio 
def clear_first_token(token):
  result = ""
  char = '\ufeff'
  for i in range(len(token)):
    if token[i] != char: result += token[i]
  return result

def preprocess(text):
  sp = es_core_news_sm.load()
  # Texto en minusculas
  text_lower = text.lower()
  # Tokenize 
  token_word = nltk.word_tokenize(text_lower, "spanish")
  # Algunos textos tienen caracteres raros al principio, por tanto hay que eliminarlos para que no influyan en el código 
  token_word[0] = clear_first_token(token_word[0])
  # Stopwords de palabras españolas
  stopword_spanish = stopwords.words("spanish")
  i = 0

  while(i < len(token_word)):
    # Se eliminan los tokens que se encuentren dentro de las stopwords 
    if token_word[i] in stopword_spanish:
      token_word.remove(token_word[i])
    #Se elimina cualquier token que sea distinto de caracteres alfanumericos
    elif not (token_word[i].isalpha()):
      token_word.remove(token_word[i])
    else:
      # Debido a que la libreria nltk no lematiza textos en español es necesario utilizar otra libreria de NLP la cual es Spacy
      word = sp(token_word[i])[0]
      token_word[i] = word.lemma_
      i = i+1
  return token_word


if __name__ =="__main__":
  f=open("texto.txt","r", encoding="utf8")
  retrieve_input(f.read())

