import numpy as np
import pandas as pd


import pickle
from PIL import Image
import re

from bs4 import BeautifulSoup
from tqdm import tqdm
import nltk
import re
from nltk.corpus import stopwords
from flask import Flask, render_template, request, url_for
from flask import jsonify
# initiate flask
app = Flask(__name__)

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)

    return phrase

words = []
path1 = "bad-words.csv"
df1 = pd.read_csv(path1,header = None)
a = df1[0].values
words.extend(a)
path2 = "Hindi.csv"
df2 = pd.read_csv(path2,header = None)
b = df2[0].values
words.extend(b)

@app.route('/word',methods = ['POST'])
def word() :

    if request.method == 'POST':


        data = request.get_json()

        print(data)

        s = data["data"]
        y = str(s)


        word = "GOOD_WORD"

        for x in words :

            if ( x == y ) or (y.lower() == x) :

                word = "BAD_WORD"

                break

        print(word)

        d = {"output" : word}
        return jsonify(d)

@app.route('/sentence',methods = ['POST'])
def sentence() :

    if request.method == 'POST':


        data = request.get_json()

        print(data)

        a = data["data"]



        strr = str(a)
        print(strr)

        s = strr.split(" ")
        print(s)

        l = len(s)

        for x in range(l) :
            if ord("A") <= ord(s[x][-1])<=ord("z"):
                print(s)
            else :
                s[x] = s[x][0:-1]
                print(s[x])

        for x in words :
            i = 0
            for y in s :

                if x == y or y.lower()==x:
                    s[i] = "$#*/%"
                    print(s[i])
                i = i+1

        s = " ".join(s)



        d = {"sentence":s}

    return jsonify(d)



if __name__ == '__main__':
    app.run(debug = True)
