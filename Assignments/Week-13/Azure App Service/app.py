from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
model = pickle.load(open("Crop_Recommendation.pkl", 'rb'))

app = Flask(__name__)


@app.route('/',methods=['POST', 'GET'])
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    prediction = ""
    if request.method == "POST":
        N = int(request.form['Nitrogen'])
        P = int(request.form['Phosphorous'])  
        K = int(request.form['Potassium'])
        temperature = float(request.form['Temperature'])  
        humidity = float(request.form['Humidity']) 
        ph = float(request.form['Soil PH']) 
        rainfall = float(request.form['Rainfall']) 

        input_features = np.array([[N, P, K, temperature, humidity, ph, rainfall]]) 

        prediction = model.predict(input_features)[0]

        if prediction == 0:
            prediction = "Apple"
        elif prediction == 1:
            prediction = "Banana"
        elif prediction == 2:
            prediction = "Blackgram"
        elif prediction == 3:
            prediction = "Chickpea"
        elif prediction == 4:
            prediction = "Coconut"
        elif prediction == 5:
            prediction = "Coffee"
        elif prediction == 6:
            prediction = "Cotton"
        elif prediction == 7:
            prediction = "Grapes"
        elif prediction == 8:
            prediction = "Jute"
        elif prediction == 9:
            prediction = "Kidneybean"
        elif prediction == 10:
            prediction = "Lentil"
        elif prediction == 11:
            prediction = "Maize"
        elif prediction == 12:
            prediction = "Mango"
        elif prediction == 13:
            prediction = "Mothbean"
        elif prediction == 14:
            prediction = "Mungbean"
        elif prediction == 15:
            prediction = "Muskmelon"
        elif prediction == 16:
            prediction = "Orange"
        elif prediction == 17:
            prediction = "Papaya"
        elif prediction == 18:
            prediction = "Pigeonpea"
        elif prediction == 19:
            prediction = "Pomegranate"
        elif prediction == 20:
            prediction = "Rice"
        elif prediction == 21:
            prediction = "Watermemlon"

        return render_template("predict.html", prediction=prediction)

   
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)