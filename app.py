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
        lis = m.findnow(loc, ser)



    return render_template('result.html', value = lis)



@app.route('/app', methods=['POST'])
def appmodel():
    if request.method == 'POST':
        json_data = request.json
        loc = json_data['loc']
        ser = json_data['ser']
        listsa= m.findnow(loc, ser)
        dicts = {}

        for i in range(len(listsa)):
            r = listsa[i]
            dicts[i] = {"Name": r[0],"Contact no":r[1],"Location":r[2],"Service":r[3],"Experience":r[4],"Customer rating":r[5]}


    return jsonify(dicts)




if __name__ == '__main__':
    app.run(debug=True)
