from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from autocorrelation import logpolar, estimation_height, estimated_autocorrelation
from scipy import ndimage


etalon = logpolar(ndimage.imread('images/etalon.jpg', flatten=True))
#im = logpolar(ndimage.imread('images/third.jpg', flatten=True))


image_list = ['im/first.jpeg']
#image_list = ['images/1_1.jpg']

#image_list = ['im/second.jpeg']
etalon_correlation = []
for i in range(len(etalon)):
    etalon_correlation.append(estimated_autocorrelation(etalon[i]))
etalon_radius = [index for index, x in enumerate(etalon_correlation) if x <= etalon_correlation[0][0] / 2]

radius = []
for x in image_list:
    correlation = []
    img = logpolar(ndimage.imread(x, flatten=True))
    for i in range(len(img)):
        correlation.append(estimated_autocorrelation(img[i]))
    radius.append([index for index, x in enumerate(correlation) if x <= correlation[0][0] / 2][0])

sum = sum(radius)
height = 4240*0.89*sum/(len(image_list)*etalon_radius[0])

print('Висота польоту дрона = ', height, 'метрів')
print('Похибка вимірювань = ', 100 - 100*height/1360, '%')

