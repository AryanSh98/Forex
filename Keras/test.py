import pandas as pd
import matplotlib.pyplot as plt

pred = pd.read_csv('Forex_sample_prediction.csv')
plt.figure()
plt.plot(pred['prediction'])
plt.plot(pred['actual'])
plt.show()