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
    # print(data)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(data)
    return result[0]
@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        #to_predict_list = list(to_predict_list.values())
        #to_predict_list = list(map(int, to_predict_list))
        # result = predictor(to_predict_list)
        #print(list(to_predict_list.values()))
        # df3 = pd.Series(to_predict_list)
        # df3 = pd.DataFrame(df3)
        # df3.swapaxes("columns","index")
        # print(df3)
        # TODO Refactor this
        print(to_predict_list)
        # create a list
        values = list(to_predict_list.values())
        #create a dataframe
        df2 = pd.DataFrame(np.array([values]),columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
        #print(df2)
        #error handlng
        if df2 is None:
            result = -1
        else:
            result=predictor(df2)
    #return render_template('results.html', prediction=result)
    return jsonify(prediction=int(result))
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)