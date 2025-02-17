import numpy as np

def softmax_weights(weights):
    """Genera pesos basados en la transformación softmax"""
    exp_weights = np.exp(weights - np.max(weights))  # Se resta el valor máximo para estabilidad numérica
    adjusted_weights = exp_weights / np.sum(exp_weights)
    return adjusted_weights
