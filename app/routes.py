from flask import request, jsonify
import joblib

model = joblib.load("models/model.pkl")

@app.route('/predict', methods=['POST'])
def predict_route():
    try:
        data = request.get_json() 
        input_features = data['input_features']
        prediction = model.predict([input_features]) 
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
