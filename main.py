import numpy as np
import tensorflow as tf
import string
import re
import pandas as pd
from fastapi import FastAPI, Form
from starlette.responses import HTMLResponse
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def preprocess_data(text):#preprocessingdata
    #Lower the text
    text = text.lower()
    #Removes non-alphabetic characters
    new_text = re.sub(r'[^a-zA-Z]', ' ', text)
    #Removes punctuation
    remove = string.punctuation
    new_text = new_text.translate(str.maketrans('', '', remove))
    #Removes ASCII dan UNICODE
    new_text = new_text.encode('ascii', 'ignore').decode('utf-8')
    new_text = re.sub(r'[^\x00-\x7F]+', '', new_text)
    #Removes newline
    new_text = new_text.replace('\n', ' ')

    return new_text

app = FastAPI()

data = pd.read_csv('depresi.csv')
tokenizer = Tokenizer(num_words=3000, split=' ')
tokenizer.fit_on_texts(data['text'].values)

def my_pipeline(text):
    text_new = preprocess_data(text)
    value = tokenizer.texts_to_sequences(pd.Series(text_new).values)
    value = pad_sequences(value, maxlen=100)
    return value

@app.get('/') #basic get view
def basic_view():
    return {"use /docs route, or /post or send post request to /predict "}

@app.post('/predict') #prediction on data
def predict(text:str = Form(...)):
    text_clear = my_pipeline(text)
    load = tf.keras.models.load_model('serenepath_model.h5')
    # print("Processed Input Text:", text_clear)  # Add this line for debugging
    predict = load.predict(text_clear)
    # print("Raw Predictions:", predict)  # Add this line for debugging
    
    prob = max(predict.tolist()[0])

    threshold = 0.5
    if prob<threshold: #assigning appropriate name to prediction
        label = 'Tidak depresi'
    elif prob>=threshold:
        label='Depresi'

    return {
        "Text": text,
        "Label": label,
        "Probability": prob
    }