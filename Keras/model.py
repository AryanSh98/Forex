# pylint: disable=import-error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
# pylint: enable=import-error

def build_keras_model():
    model = Sequential()
    model.add(LSTM(256,input_shape=(20,1)))
    model.add(Dense(1))
    return model

