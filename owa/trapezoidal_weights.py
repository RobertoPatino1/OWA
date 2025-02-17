import numpy as np


def trapezoidal_weights(weights):
    """genera pesos para una funcion trapezoidal"""
    n = len(weights)
    adjusted_weights = np.ones(n)
    # reducir pesos en los extremos
    adjusted_weights[0] = adjusted_weights[-1] = 0.5
    adjusted_weights /= np.sum(adjusted_weights)
    return adjusted_weights