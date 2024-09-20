import numpy as np

array = np.array([1,2,3,4,5])

print(np.mean(array))

import matplotlib.pyplot as plt
import math as m
y=[m.sin(i*0.01) for i in range(1000)]
x=[i*0.01 for i in range(1000)]

plt.plot(x,y)
plt.show()