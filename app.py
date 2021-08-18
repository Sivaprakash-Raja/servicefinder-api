from flask import Flask, render_template, request
import main as m
import sorting as s
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def models():
    if request.method =='POST':
        loc = request.form['loc']
        ser = request.form['ser']

        r1,r2,r3,r4,r5,r6 = m.findnow(loc, ser)




    return render_template('result.html',d1=r1[0],d2=r2[0],d3=r3[0],d4=r4[0],d5=r5[0],d6=r6[0])



if __name__ == '__main__':
    app.run(debug=True)