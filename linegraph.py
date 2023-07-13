import matplotlib.pyplot as plt 
import numpy as np 

x1 = np.array([0, 1, 2, 3])
x2 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, ls=':', color='b')
plt.plot(x2, y2, 'D--b', ms=5, mfc='r', mec='r')
plt.show()