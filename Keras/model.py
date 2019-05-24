from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_model():
    model = Sequential()
    model.add(LSTM(256,input_shape=(20,1)))
    model.add(Dense(1))
    model.compile(optimizer='adam',loss='mse')
    return model

