from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from DL_model.prediction import make_prediction
import os
from werkzeug.utils import secure_filename
from DL_model.train_def import train_model
from keras import backend

FILE_PATH = os.path.dirname(os.path.realpath(__file__))


# Init app
app = Flask(__name__)
CORS(app)


# UPLOAD_FOLDER = '/server_files/user_img'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# ROUTE -> ROOT
@app.route('/', methods=['GET', 'POST'])
# @cross_origin(supports_credentials=True)
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
# @cross_origin(supports_creditentials=True)
def upload():
    image = request.files['image']
    filename = secure_filename(image.filename)
    image.save(FILE_PATH + '/server_files/user_img/' + filename)
    return "File uploaded at: ", FILE_PATH + '/server_files/user_img/' + filename


@app.route('/predict', methods=['POST'])
# @cross_origin(supports_credentials=True)
def predict():
    print('request file: ', request.files['image'])
    backend.clear_session()
    image = request.files['image']
    filename = secure_filename(image.filename)
    image.save(FILE_PATH + '/server_files/user_img/' + filename)
    url = 'server_files/user_img/' + filename
    y_test = make_prediction(input_data=url).round()
    # 1.0 = Dogs // Cats = 0
    print('Reponse: ', y_test)
    return jsonify(y_test.tolist())


@app.route('/train', methods=['GET'])
def train():
    train_model()
    return "Training completed"


# Run Server
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
    # app.run(host='0.0.0.0', port=os.environ['PORT'])
