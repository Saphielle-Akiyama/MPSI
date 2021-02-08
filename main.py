import numpy as np
import matplotlib.image as img
from matplotlib import pyplot as plt

image = img.imread("lena.jpeg", format="RGB")

width, height, _ = image.shape

for x in range(width - 2):
    for y in range(height - 2):
        pixel = image[x:x + 3, y:y + 3]
        print(pixel)