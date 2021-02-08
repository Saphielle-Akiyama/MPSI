import numpy as np

arr = np.zeros((4, 4), dtype=int)

g, d = arr.shape

for i in range(g):
    for j in range(d):
        arr[i, j] = i + j

print(arr)

print("-" * 50)

for x in range(g - 2):
    for y in range(d - 2):
        print(arr[x:x + 3, y:y + 3])