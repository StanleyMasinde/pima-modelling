import os
import numpy as np
import pickle
import pandas as pd
from flask import Flask, render_template, request,jsonify

# create the instance
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# the predictor function
def predictor(data):
    # load the serializzed model
    loaded_model = pickle.load(open("model.pkl","rb"))
    # make the prediction
    result = loaded_model.predict(data)
    return result[0]
@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
      
        # TODO Refactor this
        print(to_predict_list)
        # create a list
        values = list(to_predict_list.values())
        #create a dataframe
        df2 = pd.DataFrame(np.array([values]),columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
        
        # basic error handling
        if df2 is None:
            result = -1
        else:
            result=predictor(df2)
        
        #return render_template('results.html', prediction=result)
        return jsonify(prediction=int(result))
    else:
        return {"error": "POST is only allowed"}
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)