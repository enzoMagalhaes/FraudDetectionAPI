from flask import Blueprint ,request, jsonify

prediction_app = Blueprint("prediction_app",__name__)

@prediction_app.route("/",methods=["GET"])
def health():
	if request.method == "GET":
		return jsonify({"status":"OK"})


@prediction_app.route("/predict",methods=["POST"])
def predict():
	if request.method == "POST":
		json_data = request.get_json()

		from classification_model.predict import make_prediction
		result = make_prediction(json_data)

		predictions = None
		if result.get("prediction") is not None:
			predictions = result.get("prediction").tolist()

		return jsonify({"predictions": predictions,"version":result.get("version")
						,"errors": result.get("errors")})



@prediction_app.route("/version",methods=["GET"])
def version():
	if request.method == "GET":
		from classification_model import __version__

		return jsonify({"model_version": __version__})