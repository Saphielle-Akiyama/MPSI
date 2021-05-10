import numpy as np

x = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

import array_utils


a = array_utils.shift_image(x, direction=array_utils.Direction.Bas, distance=2)

print(a)
