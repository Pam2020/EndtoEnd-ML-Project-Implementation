import pickle
#from django.shortcuts import render
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np 
import pandas as pd
#import sklearn 

app = Flask(__name__)

# Load the model
log_reg = pickle.load(open('log_reg.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    data = pd.DataFrame(np.array(list(data.values())).reshape(1,-1), columns = data.keys())
    output = log_reg.predict(data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods = ['POST'])
def predict():
    data = [float(x) for x in request.form.values()]

if __name__=="__main__":
    app.run(debug = True)

