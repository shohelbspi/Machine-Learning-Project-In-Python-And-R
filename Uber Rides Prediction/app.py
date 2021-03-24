import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('taxi.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_feauters = [int(x) for x in request.form.values()]
    final_feauters = [np.array(int_feauters)]
    prediction = model.predict(final_feauters)
    output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="Number of Weekly Rides Should be {}".format(math.floor(output)))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)