import numpy as np 

import enum

class Direction(enum.Enum):
    Haut = 1
    Bas = 2
    Gauche = 3
    Droite = 4

def shift_image(image: np.ndarray, direction: Direction, distance: int = 1) -> np.ndarray:

    nouvelle_image = np.zeros_like(image)

    if direction == Direction.Bas:
        nouvelle_image[distance:, :] = image[:-distance, :]

    elif direction == Direction.Haut:
        nouvelle_image[:-1, :] = image[:-1, :]

    elif direction == Direction.Gauche:
        nouvelle_image[:, :-1] = image[:, :-1]

    elif direction == Direction.Droite:
        nouvelle_image[:, 1:] = image[:, 1:]
    else:
        nouvelle_image = None
        
    return nouvelle_image


    



