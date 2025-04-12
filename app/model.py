import joblib

model = joblib.load("models/model.pkl")

def predict(input_features):
    prediction = model.predict([input_features])
    return int(prediction[0])  
