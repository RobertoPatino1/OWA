import numpy as np

def weighted_average_weights(weights, custom_weights=None):
    """Genera pesos basados en un promedio ponderado"""
    if custom_weights is None:
        custom_weights = np.ones_like(weights)
    weighted_values = weights * custom_weights
    adjusted_weights = weighted_values / np.sum(weighted_values)
    return adjusted_weights