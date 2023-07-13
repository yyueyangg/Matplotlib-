import matplotlib.pyplot as plt 
import numpy as np

x = np.array([35, 10, 25, 30])
xlabels = ['Apples', 'Bananas', 'Watermelon', 'Blueberry']
xcolors = ['red', 'yellow', 'green', 'blue']
exp = [0.2, 0, 0, 0]
plt.pie(x, labels=xlabels, colors=xcolors, explode=exp, shadow=True)
plt.legend(title='Fruits')
plt.show()