import matplotlib.pyplot as plt
import numpy as np 

x = np.array([5, 7, 8, 1, 2, 4, 1, 11, 0, 10])
y = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
colours = np.array(['red', 'blue', 'green', 'yellow', 'pink', 'orange', 'purple', 'brown', 'grey', 'black'])
sizes = np.array([100, 200, 300, 100, 500, 200, 300, 700, 1000, 200])
plt.scatter(x, y, c=colours, s=sizes, alpha=0.7)
plt.colorbar()
plt.show()