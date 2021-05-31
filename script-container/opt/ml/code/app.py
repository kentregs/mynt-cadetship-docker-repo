import numpy as np
import joblib
import json
import sys
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
# route which will accept POST requests and return model prediction/s
@app.route('/invocations', methods=['POST'])
def prediction():
    # deserialize pickled LinearRegression model
    lr_model = joblib.load('/opt/ml/model/lr_model.pkl')
    
    # prepare JSON Request data
    content = request.json
    payload = np.array(content.get("floor")).reshape(-1, 1)
    
    # perform predictions
    lr_predict = lr_model.predict(payload)
    prediction = str(lr_predict[0])
    
    return dict({'prediction': prediction})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
