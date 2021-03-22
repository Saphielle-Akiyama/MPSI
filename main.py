import numpy as np
from numpy import random

import skimage

from matplotlib import pyplot as plt

N = 10

image = skimage.data.astronaut()

image = skimage.util.random_noise(image, mode='gaussian', seed=None, clip=True)
image = skimage.color.rgb2grey(image)

print(image.shape)

fft_image = np.fft.fft2(image)

print(fft_image.shape)

fft_image[N:512-N, :] = 0
fft_image[:, N:512-N] = 0

ifft_image = np.fft.ifft2(fft_image)

plt.imshow(image, cmap="gray")
plt.show()


plt.imshow((ifft_image.real), cmap="gray")
plt.show()