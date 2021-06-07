import numpy as np

def roberts():
    return np.array([
        [-1, 0],
        [0, 1],
    ])

def sobel():
    return np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1],
    ])

def prewitt():
    return np.array([
        [1, 0, -1],
        [1, 0, -1],
        [1, 0, -1],
    ])

def kirch():
    return np.array([
        [5, 5, 5],
        [-3, 0, -3],
        [-3, -3, -3],
    ])

def robinson():
    return np.array([
        [1, 1, 1],
        [1, -2, 1],
        [-1, -1, -1],
    ])

def laplacien_discret():
    return np.array([
        [1, 1, 1],
        [1, -8, 1],
        [1, 1, 1],
    ])
 
def laplacien_robinson():
    return np.array([
        [1, -2, 1],
        [-2, 4, -2],
        [1, -2, 1]
    ])

def nettete():
    return np.array([
        [0, -1, 0],
        [-1, 5, 1],
        [0, -1, 0]
    ])

def augmentation_contraste():
    return np.array([
        [0, 0, 0, 0, 0],
        [0, 0,-1, 0, 0],
        [0,-1, 5, -1,0],
        [0, 0,-1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

def moyenneur():
    return (1/9) * np.ones((3, 3))
        
def gradient():
    return np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1],
    ])