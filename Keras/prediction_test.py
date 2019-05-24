import pandas as pd
import matplotlib.pyplot as plt


prediction_path =  ''
pred = pd.read_csv(prediction_path)
plt.figure()
plt.plot(pred['prediction'])
plt.plot(pred['actual'])
plt.show()
