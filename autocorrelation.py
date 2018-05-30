import scipy as sp
from scipy import ndimage
from math import *
import numpy as np


def logpolar(input, silent=False):
    # This takes a numpy array and returns it in Log-Polar coordinates.

    #if not silent: print("Creating log-polar coordinates...")
    # Create a cartesian array which will be used to compute log-polar coordinates.
    coordinates = sp.mgrid[0:max(input.shape)*2,0:360]
    # Compute a normalized logarithmic gradient
    log_r = 10**(coordinates[0,:]/(input.shape[0]*2.)*log10(input.shape[1]))
    # Create a linear gradient going from 0 to 2*Pi
    angle = 2.*pi*(coordinates[1,:]/360.)

    # Using scipy's map_coordinates(), we map the input array on the log-polar
    # coordinate. Do not forget to center the coordinates!
    #if not silent: print("Interpolation...")
    lpinput = ndimage.interpolation.map_coordinates(input,
              (log_r*sp.cos(angle)+input.shape[0]/2.,
              log_r*sp.sin(angle)+input.shape[1]/2.),
              order=3, mode='constant')

    # Returning log-normal...
    return lpinput


def estimated_autocorrelation(x):
    y = x
    r = np.correlate(x, y)
    return r


def estimation_height(im1, im2, height):
    image1 = logpolar(ndimage.imread(im1, flatten=True))
    image2 = logpolar(ndimage.imread(im2, flatten=True))
    etalon_correlation = []

    for i in range(len(image1)):
        etalon_correlation.append(estimated_autocorrelation(image1[i]))
    etalon_radius = [index for index, x in enumerate(etalon_correlation) if x <= etalon_correlation[0][0] / 2]

    radius = []
    correlation = []
    for i in range(len(image2)):
        correlation.append(estimated_autocorrelation(image2[i]))
    radius = [index for index, x in enumerate(correlation) if x <= correlation[0][0] / 2]
    return 0.89*height*radius[0]/etalon_radius[0], radius[0]/etalon_radius[0]


#print(estimation_height('im/etalon.jpg', 'im/first.jpeg', 4240)[0])
