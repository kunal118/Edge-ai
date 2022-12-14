# Importing Numpy package
import numpy as np
 
# sigma(standard deviation) and muu(mean) are the parameters of gaussian
 
 
def gaussian_filter(kernel_size, sigma=1, muu=0):
 
    # Initializing value of x,y as grid of kernel size
    # in the range of kernel size
 
    x, y = np.meshgrid(np.linspace(-1, 1, kernel_size),
                       np.linspace(-1, 1, kernel_size))
    print(x,y)
    dst = np.sqrt(x**2+y**2)
 
    # lower normal part of gaussian
    normal = 1/(2.00  * np.pi * sigma**2)
 
    # Calculating Gaussian filter
    gauss = np.exp(-((dst-muu)**2 / (2.0 * sigma**2))) * normal
    return gauss
 
 
kernel_size=5
gaussian = gaussian_filter(kernel_size)
print("gaussian filter of{} X {} :".format(kernel_size,kernel_size))
print(gaussian)