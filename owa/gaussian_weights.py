import numpy as np


def gaussian_weights(weights):
    """genera pesos basados en la distribucion gaussiana"""
    mean = np.mean(weights)
    std = np.std(weights) if np.std(weights) != 0 else 1   # no division para 0
    adjusted_weights = np.exp(-0.5 * ((weights - mean) / std)**2)
    return adjusted_weights / np.sum(adjusted_weights)