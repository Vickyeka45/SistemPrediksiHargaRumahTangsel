import os
import numpy as np
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def predict():
    if request.method == 'POST':
        int_features = [int(x) for x in request.form.values()]
        model = pickle.load(open("model.pkl","rb"))
        feature = [np.array(int_features)]
        prediction = model.predict(feature)
        # Format the prediction as a string with commas
        prediction_text = "Estimasi harga rumah Anda yaitu Rp{:,}".format(round(prediction[0], 2))
        return render_template("index.html", prediction_text = prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
