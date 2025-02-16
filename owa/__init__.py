from owa import calculate_owa

values = [3, 5, 7, 8]
weights = [0.2, 0.3, 0.1, 0.4]
criteria = {'sort': True, 'operator': 'exponential'}

owa_result = calculate_owa(values, weights, criteria)
print(f"El resultado OWA es: {owa_result}")
