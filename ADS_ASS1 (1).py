

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

#Loading the dataset
durham_data=pd.read_csv(r"/content/Durham_Weather_Dataset.csv", low_memory=False)

#Dataset info
durham_data.info()

#Line Plot for Maximum and Minimum Temperature - Durham based on months
axs = plt.gca()
durham_data.plot(kind='line',x='MM',y='Min_Temp', color='green', ax=axs)
durham_data.plot(kind='line',x='MM',y='Max_Temp',ax=axs,color='violet')
x_ticks = [1,2,3, 4,5, 6,7, 8,9, 10,11,12]

plt.ylabel("Temperature")
#Adding X-axis labels
x_labels = [1,2,3, 4,5, 6,7, 8,9, 10,11,12]

#Adding X-axis values to the plot
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.xlabel("Months")
plt.show()


#Scatter plot for Sun Duration based on months
durham_data.plot(kind='scatter',x='Mon',y='Sun_Dur_Days',color='green')
plt.show()

#Box Plot for Air Frost Days based on months
durham_data.boxplot(column='Air_Frost_Days',by='Mon')
plt.xlabel("Air Frost Days")
plt.xlabel("Months")
plt.show()