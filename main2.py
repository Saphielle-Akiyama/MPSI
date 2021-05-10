import numpy as np
import skimage

from matplotlib import pyplot as plt

image = skimage.data.astronaut()

for _ in range(10):
    image = skimage.util.random_noise(image, mode="gaussian", clip=True)

image = skimage.color.rgb2gray(image)

def moyennage(image: np.ndarray, taille_carre: int = 3) -> np.ndarray:
    x_size, y_size = image.shape
    
    new_img = np.zeros((x_size, y_size), dtype=float)

    new_img[1:, :] = image[:-1, :]
    new_img[0, :] = 0

    return new_img

print(moyennage(image))
