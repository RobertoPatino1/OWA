import numpy as np

def validate_input(values, weights):
    """
    Validates the input values and weights.
    
    Parameters:
        values (list or numpy array): The values to be aggregated.
        weights (list or numpy array): The weights for each value.
        
    Returns:
        bool: True if inputs are valid, otherwise raises an error.
    """
    if len(values) != len(weights):
        raise ValueError("The number of values must be equal to the number of weights.")
    
    if not all(isinstance(i, (int, float)) for i in values):
        raise TypeError("All values must be numeric.")
    if not all(isinstance(i, (int, float)) for i in weights):
        raise TypeError("All weights must be numeric.")
    
    if not np.isclose(np.sum(weights), 1.0):
        raise ValueError("The sum of weights must be equal to 1.")
    
    return True

def normalize_values(values):
    """
    Normalizes the input values to the range [0, 1].
    
    Parameters:
        values (list or numpy array): The values to normalize.
        
    Returns:
        numpy array: The normalized values.
    """
    values = np.array(values)
    min_val = np.min(values)
    max_val = np.max(values)
    
    if max_val - min_val == 0:
        return np.zeros_like(values)
    
    return (values - min_val) / (max_val - min_val)
