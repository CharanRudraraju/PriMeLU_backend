from flask import Flask, request,jsonify
from flask_cors import CORS

import numpy as np
import ast


# from flask import current_app
# current_app.config['SERVER_NAME'] = 'localhost'   
# with current_app.test_request_context():
#      url = url_for('index', _external=True)

app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/': {'origins': ''}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/predict", methods=["POST","GET"])
def submitData():
    form_data = request.data
    data =  form_data.decode("UTF-8")
    data_dict = ast.literal_eval(data)
    return 'hi'


if __name__ =='__main__':
    app.run(debug=True)