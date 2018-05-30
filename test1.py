import scipy as sp
from scipy import ndimage
from math import *
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def logpolar(input, silent=False):
    # This takes a numpy array and returns it in Log-Polar coordinates.

    if not silent: print("Creating log-polar coordinates...")
    # Create a cartesian array which will be used to compute log-polar coordinates.
    coordinates = sp.mgrid[0:max(input.shape)*2,0:360]
    # Compute a normalized logarithmic gradient
    log_r = 10**(coordinates[0,:]/(input.shape[0]*2.)*log10(input.shape[1]))
    # Create a linear gradient going from 0 to 2*Pi
    angle = 2.*pi*(coordinates[1,:]/360.)

    # Using scipy's map_coordinates(), we map the input array on the log-polar
    # coordinate. Do not forget to center the coordinates!
    if not silent: print("Interpolation...")
    lpinput = ndimage.interpolation.map_coordinates(input,
              (log_r*sp.cos(angle)+input.shape[0]/2.,
              log_r*sp.sin(angle)+input.shape[1]/2.),
              order=3, mode='constant')

    # Returning log-normal...
    return lpinput





im1 = ndimage.imread('images/third.jpg', flatten=True)
im2 = ndimage.imread('images/third.jpg', flatten=True)
#im1 = np.asarray(Image.open('images/1_1.jpeg').convert('L'))
#im2 = np.asarray(Image.open('images/1.jpg').convert('L'))

# Conversion to log-polar coordinates
lpimage = logpolar(im1)
lptarget = logpolar(im2)

#correlation = []
# for i in range(len(lpimage)):
#     correlation.append(np.correlate(lpimage[i], lptarget[i], mode='same'))
# print(len(correlation))
# print(4.24*984*np.amax(correlation)/4.21316e+06)

#i = [(index, x) for index, x in enumerate(correlation) if x == np.amax(correlation)]
#print(i)
#x = [x for index, x in enumerate(correlation) if index >= i[0][0]]
#print('X=', x)

# correlation = []
# for i in range(len(lpimage)):
#     correlation.append(np.correlate(lpimage[i], lptarget[i], mode='valid'))
# print(np.amax(correlation))
# plt.acorr(lpimage)
# plt.show()



#475