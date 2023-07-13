import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 2, 1)
plt.title('Day 1 sales')
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([2, 7, 2, 9])
plt.subplot(2, 2, 2)
plt.title('Day 1 income')
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([5, 2, 7, 3])
plt.subplot(2, 2, 3)
plt.title('Day 2 sales')
plt.plot(x, y)

x = np.array([0, 1, 2, 3])
y = np.array([4, 1, 6, 4])
plt.subplot(2, 2, 4)
plt.title('Day 2 income')
plt.plot(x, y)

plt.suptitle('My Shop')
plt.show()