import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def plot_data(dataset):
    plt.figure()
    plt.plot(dataset["Open"])
    # plt.plot(dataset["High"])
    # plt.plot(dataset["Low"])
    plt.plot(dataset["Close"])
    plt.ylabel('Price')
    plt.xlabel('Time')
    plt.legend(['Open', 'Close'], loc='upper left')
    plt.show()


def normalize(close_data, return_scaler=False):
    scaler = MinMaxScaler()
    close_data = close_data.values.reshape(close_data.shape[0], 1)
    close_data = scaler.fit_transform(close_data)
    if return_scaler:
        return scaler
    return close_data


def process_data(data, look_back):
    X, Y = [], []
    for i in range(len(data)-look_back-1):
        X.append(data[i:(i+look_back), 0])
        Y.append(data[(i+look_back), 0])
    return np.array(X), np.array(Y)

