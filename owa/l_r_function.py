import numpy as np


def lr_weights(weights, L=1, R=1):
    """ Genera pesos basados en la representación L-R """
    n = len(weights)
    adjusted_weights = np.array([(L if i < n // 2 else R) for i in range(n)])
    return adjusted_weights / np.sum(adjusted_weights)