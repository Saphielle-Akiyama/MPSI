import enum
from scipy import signal

import skimage
from skimage import color

from matplotlib import pyplot as plt

import masques

fig = plt.figure()

image = skimage.data.chelsea()
image = color.rgb2gray(image)

for _ in range(2):
    image = skimage.util.random_noise(image, mode='gaussian', seed=None, clip=True)


# Application de nos filtres maisons
last = 0 
for index, filtre in enumerate(masques.__dict__.values(), 1):
    if not callable(filtre):
        continue
    print(filtre.__name__)

    sub = fig.add_subplot(5, 5, index)
    sub.axis('off')

    sub.imshow(
        signal.correlate(
            image.copy(),
            filtre()
        ),
        cmap=plt.cm.gray,
    )
    sub.set_title(filtre.__name__)

    last = index

# Filtres vanant de skimage
from skimage import restoration

for index, filtre in enumerate(restoration.__dict__.values(), last):
    if not callable(filtre):
        continue

    if not filtre.__name__.startswith("denoise"):
        continue

    print(filtre.__name__)

    sub = fig.add_subplot(5, 5, index)
    sub.axis('off')

    sub.imshow(
        filtre(image.copy()),
        cmap=plt.cm.gray,
    )
    sub.set_title(filtre.__name__)

plt.show()
 