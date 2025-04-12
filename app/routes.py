from flask import Blueprint, request, jsonify
from .model import predict

routes = Blueprint('routes', __name__)

@routes.route("/predict", methods=["POST"])
def predict_route():
    data = request.json
    prediction = predict(data["features"])
    return jsonify({"prediction": prediction})
