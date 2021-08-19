import flask
from flask import Flask, render_template, request
from flask import jsonify
import main as m
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

    return render_template('result.html', d1=r1[0], d2=r2[0], d3=r3[0], d4=r4[0], d5=r5[0], d6=r6[0])

@app.route('/app', methods=['POST'])
def appmodel():
    if request.method == 'POST':
        json_data = request.json
        loc = json_data['loc']
        ser = json_data['ser']
        r1, r2, r3, r4, r5, r6 = m.findnow(loc, ser)

        data = {"Name": r1[0],"Contact no":r2[0],"Service":r3[0],"Location":r4[0],"Experience":r5[0],"Customer rating":r6[0]}

    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)
