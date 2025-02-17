import numpy as np
from trapezoidal_weights import trapezoidal_weights
from triangular_weights import triangular_weights
from alpha_cuts import alpha_cut_weights
from l_r_function import lr_weights
from harmonic_weights import harmonic_weights
from softmax_weights import softmax_weights
from weighted_average_weights import weighted_average_weights


# TODO: Agregar nuevos operadores OWA, por ejemplo lineal, exponencial, etc.


def calculate_owa(values, weights, criteria):
    """
    Calculates the Ordered Weighted Averaging (OWA) of a set of values,
    with custom operators like linear and exponential.

    Parameters:
        values (list or numpy array): The values to aggregate.
        weights (list or numpy array): The weights for each value. Should sum to 1.
        criteria (dict): A dictionary containing the criteria like sorting order and operator type.
            - 'sort': Boolean indicating whether to sort the values.
            - 'operator': A string specifying the operator ('linear', 'exponential', 'logarithmic', 'sigmoid','gaussian','uniform','tanh'.)

    Returns:
        float: The aggregated OWA result.
    """
    values = np.array(values)
    weights = np.array(weights)
    if not np.isclose(np.sum(weights), 1.0):
        raise ValueError("The sum of weights must be equal to 1.")
    if criteria.get('sort', True):
        values = np.sort(values)[::-1]
    operator = criteria.get('operator', 'linear')

    if operator == 'linear':
        adjusted_weights = weights
    elif operator == 'exponential':
        adjusted_weights = np.exp(weights) / np.sum(np.exp(weights))
    elif operator == 'logarithmic':
        adjusted_weights = np.log(weights + 1) / np.sum(np.log(weights + 1))
    elif operator == 'sigmoid':
        adjusted_weights = 1 / (1 + np.exp(-weights))
        adjusted_weights /= np.sum(adjusted_weights)
    elif operator == 'power':
        p = criteria.get('p', 2)
        adjusted_weights = np.power(weights, p) / np.sum(np.power(weights, p))
    elif operator == 'gaussian':
        mean = np.mean(weights)
        std = np.std(weights)
        adjusted_weights = np.exp(-0.5 * ((weights - mean) / std) ** 2)
        adjusted_weights /= np.sum(adjusted_weights)
    elif operator == 'uniform':
        adjusted_weights = np.ones_like(weights) / len(weights)
    elif operator == 'tanh':
        adjusted_weights = np.tanh(weights)
        adjusted_weights /= np.sum(np.tanh(weights))
    elif operator == 'triangular':
        adjusted_weights = triangular_weights(weights)
    elif operator == 'trapezoidal':
        adjusted_weights = trapezoidal_weights(weights)
    elif operator == 'alpha_cut':
        adjusted_weights = alpha_cut_weights(weights,
                                             criteria.get('alpha', 0.5))
    elif operator == 'lr':
        adjusted_weights = lr_weights(weights, criteria.get('L', 1),
                                      criteria.get('R', 1))
    elif operator == 'harmonic':
        return harmonic_weights(weights)
    elif operator == 'softmax':
        return softmax_weights(weights)
    elif operator == 'weighted_average':
        custom_weights = criteria.get('custom_weights', None)
        return weighted_average_weights(weights, custom_weights)
    else:
        adjusted_weights = weights

    owa_result = np.dot(values, adjusted_weights)
    return owa_result
