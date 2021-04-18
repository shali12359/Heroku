import flask
from flask import jsonify, request
from test import sayHello
from test import sayAge
from OperationDyscalculiaController import Prediction
from NumericDysgraphiaController import numericPrediction

app = flask.Flask(__name__)

diseasePrediction = Prediction()
numericDysgraphiaPrediction = numericPrediction()


@app.route('/', methods = ['GET', 'POST'])
def predict():
  greet = sayHello('Shalitha')
  return greet

@app.route('/predict', methods = ['GET', 'POST'])
def predictNew():
  greet = sayAge("26")
  return jsonify({ 'msg': "Hello, " + greet})

@app.route("/numeric",methods=['GET', 'POST'])
def scrrenNumericDysgraphia():
   data = request.get_json(force=True)
   numberDysgraphiaResult = numericDysgraphiaPrediction.numDysgraphiaPredict(data)
   return jsonify({"data":numberDysgraphiaResult})

@app.route("/api",methods=['GET', 'POST'])
def scrrenDyscalculia():
    data = request.get_json(force=True)
    dyscalculiaResult = diseasePrediction.dyscalculiaPredict(data)
    return jsonify({"data":dyscalculiaResult})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9696, debug=True)
