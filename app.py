from flask import Flask, request, jsonify

import pickle
import pandas as pd

app = Flask(__name__)

# load the trained model
model = pickle.load(open("freight_cost_model.pkl", "rb"))
features=pickle.load(open("model_features.pkl", "rb"))

@app.route("/")
def home():
    return "ML api is running "

@app.route("/predict",methods=["POST"])
def predict():
    data = request.get_json()
    
    #convert input into df
    df= pd.DataFrame([data])
    
    #align w the training features!
    df=df.reindex(columns=features, fill_value=0)
    
    #predict
    prediction=model.predict(df)
    
    return jsonify({
        "predicted_freight_cost": float(prediction[0])
    })
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
