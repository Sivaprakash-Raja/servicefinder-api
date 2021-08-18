from flask import Flask, render_template, request
import models as models
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def models():
    if request.method =='POST':
        day = request.form['d']
        hour = request.form['h']
        min = request.form['m']
        result=day+"/"+hour+"/"+min
        #result= models.powerPrediction(day,hour,min)

    return render_template('index.html',d=result)



if __name__ == '__main__':
    app.run(debug=True)