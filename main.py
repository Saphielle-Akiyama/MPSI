import numpy as np
import PIL
import matplotlib.image as img
from matplotlib import pyplot as plt

image_data = PIL.Image.open("carré.png")
image = np.array(image_data)


width, height, _ = image.shape

for x in range(width - 2):
    for y in range(height - 2):
        pixel = image[x:x + 3, y:y + 3, 0]
        print(pixel)