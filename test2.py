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


def autocorrelation(x):
    """
    Compute the autocorrelation of the signal, based on the properties of the
    power spectral density of the signal.
    """
    xp = x-np.mean(x)
    f = np.fft.fft(xp)
    p = np.array([np.real(v)**2+np.imag(v)**2 for v in f])
    pi = np.fft.ifft(p)
    return np.real(pi)[:x.size/2]/np.sum(xp**2)


im1 = ndimage.imread('images/1_1.jpeg', flatten=True)
im2 = ndimage.imread('images/2_1.jpeg', flatten=True)

correlation = []
lpimage = logpolar(im2)
print(lpimage)

for i in range(len(lpimage)):
    correlation.append(autocorrelation(lpimage[i]))
print(correlation)