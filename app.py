import numpy as np
import pandas as pd

import pickle

from flask import Flask, render_template, request, url_for
from flask import jsonify
from flask_cors import CORS
# initiate flask

app = Flask(__name__)


CORS(app)

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
