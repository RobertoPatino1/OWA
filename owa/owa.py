import numpy as np

# TODO: Agregar nuevos operadores OWA, por ejemplo lineal, exponencial, etc.
def calculate_owa(values, weights, criteria):
    """
    Calculates the Ordered Weighted Averaging (OWA) of a set of values.
    
    Parameters:
        values (list or numpy array): The values to aggregate.
        weights (list or numpy array): The weights for each value. Should sum to 1.
        criteria (dict): A dictionary containing the criteria like sorting order.
        
    Returns:
        float: The aggregated OWA result.
    """
    
    values = np.array(values)
    weights = np.array(weights)
    
    if not np.isclose(np.sum(weights), 1.0):
        raise ValueError("The sum of weights must be equal to 1.")
    
    
    if criteria.get('sort', True):
        values = np.sort(values)[::-1]
    
    
    owa_result = np.dot(values, weights)
    
    return owa_result
