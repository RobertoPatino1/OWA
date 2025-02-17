import numpy as np

def harmonic_weights(weights):
    """Genera pesos basados en la media armónica"""
    adjusted_weights = 1 / (1 / (weights + 1e-6))  # Se agrega un pequeño valor para evitar divisiones por cero
    return adjusted_weights / np.sum(adjusted_weights)
