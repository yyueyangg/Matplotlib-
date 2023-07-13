import matplotlib.pyplot as plt 
import numpy as np 

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([1, 3, 5, 7])

plt.bar(x, y, width=0.3, color='red')
plt.show()

plt.barh(x, y, height=0.3, color='blue')
plt.show()