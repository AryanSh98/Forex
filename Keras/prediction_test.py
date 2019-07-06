import pandas as pd
import matplotlib.pyplot as plt


prediction_path =  'C:\\Users\\Jack\\Documents\\Forex\\Forex\\Keras\\prediction_sample_test.csv'
pred = pd.read_csv(prediction_path)
plt.figure()
plt.plot(pred['prediction'])
plt.plot(pred['Ground_truth'])
plt.show()


