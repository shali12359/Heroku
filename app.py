import flask
from flask import jsonify
from test import sayHello
from test import sayAge

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def predict():
  greet = sayHello('Shalitha')
  return greet

@app.route('/predict', methods = ['GET', 'POST'])
def predictNew():
  greet = sayAge("26")
  return jsonify({ 'msg': "Hello, " + greet})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9696, debug=True)
