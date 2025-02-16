from owa.owa import calculate_owa

def main():
    ##################################
    ## OWA FOR SAMPLE 1
    ##################################
    values_1 = [0.8, 0.6, 0.9, 0.7, 0.5]
    weights_1 = [0.2, 0.3, 0.1, 0.25, 0.15]
    
    
    criteria_1 = {
        'sort': True,
    }
    
    
    result_1 = calculate_owa(values_1, weights_1, criteria_1)
    print(f"OWA Result 1: {result_1}")
    
    ##################################
    ## OWA FOR SAMPLE 2
    ##################################
    values_2 = [0.5, 0.9, 0.6, 0.4, 0.7]
    weights_2 = [0.25, 0.25, 0.2, 0.15, 0.15]
    
    criteria_2 = {
        'sort': True,
    }
    
    result_2 = calculate_owa(values_2, weights_2, criteria_2)
    print(f"OWA Result 2: {result_2}")
    
    ##################################
    ## OWA FOR SAMPLE 3
    ##################################
    values_3 = [0.6, 0.4, 0.8, 0.7, 0.9]
    weights_3 = [0.1, 0.3, 0.2, 0.25, 0.15]
    
    
    criteria_3 = {
        'sort': True,
    }
    
    result_3 = calculate_owa(values_3, weights_3, criteria_3)
    print(f"OWA Result 3: {result_3}")
    
if __name__ == "__main__":
    main()
