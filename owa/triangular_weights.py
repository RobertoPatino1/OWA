import numpy as np


def triangular_weights(weights):
    """asignacion de pesos basados en su distribucion triangular"""
    n = len(weights)
    midpoint = n//2
    adjusted_weights = np.zeros(n)
    for i in range(n):
        if i <= midpoint:
            adjusted_weights[i] = (i + 1) / (midpoint + 1)
        else:
            adjusted_weights[i] = (n - i) / (n - midpoint)
    return adjusted_weights / np.sum(adjusted_weights)
