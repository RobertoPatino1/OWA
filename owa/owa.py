import numpy as np

# TODO: Agregar nuevos operadores OWA, por ejemplo lineal, exponencial, etc.
def calculate_owa(values, weights, criteria):
    """
    Calculates the Ordered Weighted Averaging (OWA) of a set of values, with custom operators like linear and exponential.

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
    else:
        adjusted_weights = weights


    owa_result = np.dot(values, adjusted_weights)
    
    return owa_result
