from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os

MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/saved_models/model.h5'

callbacks = [
    EarlyStopping(monitor='val_loss',
                  patience=5),
    ModelCheckpoint(filepath=MODEL_PATH,
                    monitor='val_loss',
                    save_best_only=True)
]

# TRAIN SET
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=False)

train_generator = train_datagen.flow_from_directory(
    'DL_model/data/training_set',
    target_size=(50, 50),
    batch_size=32,
    class_mode='binary',
    seed=42)


# TEST SET
valid_datagen = ImageDataGenerator(rescale=1./255)
valid_generator = valid_datagen.flow_from_directory(
    'DL_model/data/test_set',
    target_size=(50, 50),
    batch_size=64,
    class_mode='binary',
    seed=42)


def train_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=(50, 50, 3), activation='relu'))
    model.add(Conv2D(32,(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())

    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])

    model.fit_generator(train_generator,
                        epochs=80,
                        validation_data=valid_generator,
                        callbacks=callbacks)

    return 'Model Trained!'

