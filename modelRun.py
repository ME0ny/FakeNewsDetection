
import re
import pandas as pd
from keras.models import load_model

def preprocess_text(sentence):
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    return sentence.lower()

def vectorize(text,item_to_index):
    return_list = []
    for word in text.split(' '):
        try:
            return_list.append(item_to_index[word])
        except:
            pass
    return return_list

def main(text):
    text = ['WASHINGTON (Reuters) - The head of a conservat']
    text = preprocess_text(text)
    list1 = ''.join(text.tolist()).split(' ')
    list1.extend(''.join(text.tolist()).split(' '))
    unique = pd.Series(''.join(text.tolist()).split(' ')).unique()
    item_to_index = {}
    index_to_item = {}
    for index,item in enumerate(unique):
        item_to_index[item] = index
        index_to_item[index] = item
    text = vectorize(text,item_to_index)
    model = load_model('path_to_my_model.h5')
    return model.predict(text)
