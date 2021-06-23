import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import joblib
app = Flask(__name__)
 
pred = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[float(x) for x in request.form.values()]]
    print(x_test)
    
    model = pickle.load(open('future wheather predection.pkl', 'rb'))
    scaler = joblib.load("future wheather predection.save") 
    print("test1")
    prediction = model.predict(scaler.transform(x_test))
    print(prediction)
    
    if(prediction == [0]):
        pred = "No Rainfall"
    elif(prediction == [1]):
        pred = " There is a chance of Fog!..."
    elif(prediction == [2]):
        pred = " There is a chance of Fog & Rain!..."
    elif(prediction == [3]):
        pred = " There is a chance of Fog & Rain & Thunderstorm!..."
    elif(prediction == [5]):
        pred = " There is a chance of Rain!..."
    elif(prediction == [6]):
        pred = " There is a chance of Rain & Snow!..." 
    elif(prediction == [7]):
        pred = " There is a chance of Rain And Thunderstorm!..."  
    else:
        pred = " There is a chance of Thunderstorm!..."   
    
    return render_template('index.html', prediction_text="Prediction: "+pred)



if __name__ == "__main__":
    app.run(debug=True)
