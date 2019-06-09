import pandas as pd
import matplotlib.pyplot as plt


prediction_path =  '/home/aryan/Source/Forex/Keras/Forex_sample_predictions.csv'
pred = pd.read_csv(prediction_path)
plt.figure()
plt.plot(pred['prediction'])
plt.plot(pred['actual'])
plt.show()