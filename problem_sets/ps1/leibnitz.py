def leibnitz(n):
    """
    leibnitz(n) -> int
    
    n: The number of terms of Leibnitz's series to sum 
    """
    
    total = 0
    for i in range (n):
        # Denominator increases by two each term, starting from 1
        term = 1/(1 + 2 * i)   
        
        # Sign alternates between -1 and +1, starting at +1
        sign = (-1) ** i     
        
        total += sign * term
    
    return total

import math

def compare():
    # A list comprehension that evaluates the leibnitz function
    # at progressively higher powers of 10 (from 1 - 3)
    results = [leibnitz(10 ** n) for n in range (1, 4)]
    groundtruth   = math.pi / 4
    
    # Another list comprehension that computes the deltas between
    # the groundtruth value supplied by the math module and the 
    # values computed by the leibnitz function
    deltas = [groundtruth - r for r in results]
    
    return results, deltas

print(compare())

