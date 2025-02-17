from owa import calculate_owa

values = [3, 5, 7, 8]
weights = [0.2, 0.3, 0.1, 0.4]
criteria = {'sort': True, 'operator': 'exponential'}
criteria_1 = {'sort': True, 'operator': 'gaussian'}
criteria_2 = {'sort': True, 'operator': 'sigmoid'}
owa_result_gaussian = calculate_owa(values, weights, criteria_1)
print(f"El resultado OWA es: {owa_result_gaussian}")
owa_result_sigmoid = calculate_owa(values, weights, criteria_2)
print(f"El resultado OWA es: {owa_result_sigmoid}")
owa_result = calculate_owa(values, weights, criteria)
print(f"El resultado OWA es: {owa_result}")
