def bubblesort(array):
    """
    bubblesort(array) -> list
    
    array -> [list]: A list of elements to be sorted using bubblesort 
    """

    steps = 0
    
    while True:
        swapped = False

        # Iterate through the array from 0 to len(array) - 2
        # The -2 is because we also check the element after,
        # so we'd get an outOfBoundsError if we went to
        # len(array) - 1. This means the for loop's bounds
        # are from 0 to len(array) - 1
        for i in range (len(array) - 1):
            if (array[i] > array[i + 1]):
                # Swap!
                array[i + 1], array[i] = array[i], array[i + 1]
                swapped = True
            
            steps += 1
        
        # Terminate if no swaps were performed (array
        # is perfectly sorted)
        if not swapped:
            break;
    
    return array, steps

print(bubblesort([5, 0, 9, 8, 7, 1, 4, 3, 2, 6]))

def combsort(array, scaling_factor):
    """
    combsort(array, scaling_factor) -> list
    
    array -> [list]: A list of elements to be sorted using combsort 
    scaling_factor -> [float]: A scalar that reduces the size of the
    gap every sweep (>1)
    """

    steps = 0    
    gap = len(array)
    
    while True:
        swapped = False
        
        # Reduce the gap
        # We can safely cast gap to int after every divide
        # because int() floors the float result of 
        # the division, ensuring that gap is always
        # smaller every sweep
        gap = int(gap / scaling_factor)

        for i in range (len(array) - gap):
            if (array[i] > array[i + gap]):
                # Swap!
                array[i + gap], array[i] = array[i], array[i + gap]
                swapped = True
            
            steps += 1
            
        if not swapped and gap == 0:
            break;
    
    return array, steps

print(combsort([5, 0, 9, 8, 7, 1, 4, 3, 2, 6], 1.3))

import time
import random

def evaluate(trials = 1000, n = 100):
    random_array = [i for i in range (n)]
    bubblesort_total = 0
    combsort_total = 0
    
    for i in range (trials):
        # In-place shuffles the random_array
        random.shuffle(random_array)
        
        # Start a timer for bubblesort
        bubblesort_timer = time.time()
        bubblesort(random_array)
        bubblesort_total += time.time() - bubblesort_timer
        
        # Start a timer for combsort
        combsort_timer = time.time()
        combsort(random_array, 1.3)
        combsort_total += time.time() - combsort_timer
    
    bubblesort_avg = bubblesort_total / trials
    combsort_avg = combsort_total / trials

    return bubblesort_avg, combsort_avg, bubblesort_avg / combsort_avg

print(evaluate())