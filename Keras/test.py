import pandas as pd
import matplotlib.pyplot as plt

pred = pd.read_csv('/home/aryan/Source/Forex/Keras/Forex_sample_predictions.csv')
plt.figure()
plt.plot(pred['prediction'])
plt.plot(pred['actual'])
plt.show()
