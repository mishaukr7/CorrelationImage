from PIL import Image
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from test1 import logpolar
from scipy import ndimage


image1 = ndimage.imread('im/second.jpeg', flatten=True)
image2 = ndimage.imread('im/second.jpeg', flatten=True)


def estimated_autocorrelation(x):
    n = len(x)
    variance = x.var()
    y = x
    r = np.correlate(x, y)
    #result = r/(variance*n)
    return r


correlation = []
img1 = logpolar(image1)
img2 = logpolar(image2)
for i in range(len(img1)):
    correlation.append(estimated_autocorrelation(img1[i]))

x = [index for index, x in enumerate(correlation) if x <= correlation[0][0]/2]
#print(np.amax(correlation))
print(x[0])
plt.plot(correlation)
plt.show()

#9.53313e+06