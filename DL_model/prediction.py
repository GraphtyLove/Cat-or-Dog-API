from keras.models import load_model
from keras.preprocessing import image
from .train_def import MODEL_PATH
import numpy as np


def make_prediction(input_data, model_path=MODEL_PATH):
    # TEST img
    test_image = image.load_img(input_data, target_size=(50, 50))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)

    loaded_model = load_model(model_path)
    result = loaded_model.predict(test_image)
    return result
