import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import dataset

file_dir = "/home/aryan/Source/Forex/EURUSD.I240.csv"
forex_data = pd.read_csv(file_dir)
forex_data.columns = ['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']
forex_data = forex_data[['Date', 'Time', 'Open', 'High', 'Low', 'Close']]

dataset.plot_data(forex_data)
