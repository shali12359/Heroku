import numpy as np
import pickle


class Prediction:
    def helo(self):
        return {'about': 'Hello'}

    def dyscalculiaPredict(self, data):
        # data = request.get_json(force=True)
        # final=[np.array(list(data.values()))]
        final = np.array(list(data.values()))
        print("array : ", final)

        model = pickle.load(open('Dyscalculiar-Predict.pkl', 'rb'))
        prediction_y = model.predict(final)
        print(prediction_y)
        output = np.int(prediction_y)
        # return str(prediction_y)
        return output
