import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt


img = ndimage.imread('galaxies.png')
plt.imshow(img, interpolation='nearest')
plt.show()
# Note the 0 sigma for the last axis, we don't wan't to blurr the color planes together!
img = ndimage.gaussian_filter(img, sigma=(5, 5, 0), order=0)
plt.imshow(img, interpolation='nearest')
plt.show()
