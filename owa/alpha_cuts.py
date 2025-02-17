import numpy as np


def alpha_cut_weights(weights, alpha=0.5):

    adjusted_weights = np.where(weights >= alpha, weights, 0)
    return adjusted_weights / np.sum(adjusted_weights)
