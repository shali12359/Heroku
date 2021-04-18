import numpy as np
import pickle

class numericPrediction:

    def numDysgraphiaPredict(self, data):
        final = np.array(list(data.values()))
        print("array : ", final)

        model = pickle.load(open('NewNumericDysgraphia.pkl', 'rb'))
        prediction_y = model.predict(final)
        print(prediction_y)
        output = np.int(prediction_y)
        # return str(prediction_y)
        return output
