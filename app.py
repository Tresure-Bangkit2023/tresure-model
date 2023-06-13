import numpy as np
from flask import Flask, request
from tensorflow import keras


model = keras.models.load_model('model/saved_model')

def do_predict(user_id, places_not_visited):
    
    places_not_visited = np.expand_dims(places_not_visited, 1)
    user_places_array = np.hstack(
        ([[user_id % 299]] * len(places_not_visited), places_not_visited)
    )

    predictions = model.predict(user_places_array).flatten()
    top_ratings_indices = predictions.argsort()[-15:][::-1]
    recommended_place_ids = np.array([places_not_visited[i] for i in top_ratings_indices]).flatten().tolist()
    
    result_dict = {
        "data": recommended_place_ids
    }
    return result_dict


app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Halo</p>"


@app.route('/predict', methods=['POST'])
def predict():
    user_id = request.form.get('user_id')
    places_not_visited = request.form.get('places_not_visited')

    empty_request = [None, '']

    if user_id in empty_request:
        return '<p>Please input user id.</p>'
    
    try:
        user_id = int(user_id, 10)
    except:
        return '<p>Please input a valid user id (Integer).</p>'

    if places_not_visited in empty_request:
        return '<p>Please input places not visited.</p>'
    
    try:
        places_not_visited = convert_number(places_not_visited)
    except:
        return '<p>Please input valid places not visited, e.g., "123, 321, 333".</p>'

    print(places_not_visited)
    result = do_predict(user_id, places_not_visited)
    return result


def convert_number(string_data):
    if ',' in string_data:
        numbers = string_data.split(",")
        result = [int(num.strip()) for num in numbers]
    else:
        result = [int(string_data)]

    return result