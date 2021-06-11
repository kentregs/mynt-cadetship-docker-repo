import numpy as np
import tensorflow
import PIL.Image
import os.path
import shutil
import keras
import json
import glob
import sys
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from flask import Flask, request, jsonify
from keras.preprocessing import image
from flask import Flask

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)

main_dir = '/home/train/opt'

def remove_thing(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)

def empty_directory(path):
    for i in glob.glob(os.path.join(path, '*')):
        remove_thing(i)

def preprocess(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img = image.img_to_array(img)/255.0
    img = img.reshape(1, 150, 150, 3)
	
    return img

def predict_labels(img_paths):
    # init empty lists for storing preprocessed images and predictions
    imgs = []
    pred_lst = []
    predictions = []
    
    # preprocess image/s 
    for path in img_paths:
        img = preprocess(path)
        imgs.append(img)
    
    # load binary classifier model
    model = keras.models.load_model(main_dir + '/model/bees_wasps_model.h5')
    
    # perform prediction/s
    for img in imgs:
        pred = model.predict(img)
        predictions.append(pred)
    
    # convert probability/ies to prediction/s and store in list
    for probability in predictions:
        pred = "wasp" if probability * 100 > 50 else "bee"
        pred_lst.append(f'prediction: {pred}')
    
    return dict({'prediction/s': pred_lst})

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
# route which will accept POST requests and return our model predictions
@app.route('/invocations', methods=['POST'])
def prediction():
    # init empty lists for storing image filenames and paths
    img_paths = []
    imgs = []
    
    # parse input data
    for i in range(1, len(request.files)+1):
        img = request.files[f'img_{i}']
        imgs.append(img)
    
    for img in imgs:
        path = main_dir + "/data/static/" + img.filename
        img.save(path)
        img_paths.append(path)
        
    # perform prediction/s
    response = predict_labels(img_paths)
    
    # delete saved images
    empty_directory('/home/train/opt/data/static/')
    
    return response
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')