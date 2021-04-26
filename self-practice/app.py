from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import json, codecs
import pandas as pd

app = Flask(__name__)
api = Api(app)

file_path = "/lib/path.json"

# Trained Model file
model_path = 'lib/model/model.pkl'

# Load trained classification model to environment
model = pickle.load(open(model_path, 'rb'))

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('data_path')


class Prediction(Resource):
    def get(self):
        # get parser argument and find data for prediction
        args = parser.parse_args()
        data_path = args['data_path']

        # Load data
        data = pd.read_csv(data_path)

        # Get prediction
        prediction = model.predict(data.drop('item_id',axis=1))

        # create JSON object
        output = {}

        # Load item_id and preidiction for each item_id
        for item_id, prediction in zip(data.item_id,prediction):
            output[item_id] = prediction

        return output

api.add_resource(Prediction, '/')

if __name__ == '__main__':
    app.run(debug=True)
