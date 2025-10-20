import pickle
import numpy as np
import pandas as pd
from flask import Flask, request,app,jsonify,url_for,render_template

app = Flask(__name__)
linear_regression_model = pickle.load(open("linear_regression_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=linear_regression_model.predict(final_input)[0]
    return render_template("home.html", prediction_text = "The House  price prediction is {}".format(output))

if __name__ =="__main__":
    app.run(debug = True)