import numpy as np


def sigmoid_weights(weights):
    """ Genera pesos usando una función sigmoide """
    adjusted_weights = 1 / (1 + np.exp(-weights))
    return adjusted_weights / np.sum(adjusted_weights)
