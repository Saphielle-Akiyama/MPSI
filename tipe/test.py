from __future__ import annotations
from collections.abc import Callable
from math import factorial, isnan

import numpy as np
from matplotlib import pyplot as plt
from scipy.misc import derivative

def f(x: float) -> float:
    return np.sin(x)

def dl_n(f: Callable[[float], float], x0: float, n: int) -> list[float]:
    """
    Coefficients du DL à l'ordre N de la fonction donnée
    """
    L = []
    fact = 1

    for k in range(n + 1):
        fact *= k or 1
        x = derivative(f, x0, dx=k, order=5) / fact

        if isnan(x):
            L.append(0)
        else:
            L.append(x)

    return L

def dl_vers_fn(dl: list[float]) -> Callable[[float], float]:
    """
    Donne la fonction polynomiale associée à la liste donnée
    """
    def f(x: float) -> float:
        S = 0
        for k, coeff in enumerate(dl):
            S += coeff * pow(x, k)
        return S

    return f


lin = np.linspace(-10, 10, 10_000)
dl = dl_n(f, 0, 10)

lins = []

for i, _ in enumerate(dl):
    fn = dl_vers_fn(dl[:i])

    try:
        plt.plot(lin, fn(lin))
    except ValueError:
        print("N'a pas pu afficher le dl à l'ordre", i)

plt.show()