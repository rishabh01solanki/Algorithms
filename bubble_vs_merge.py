# Import the merge_sort and bubble_sort functions from the sorting module

from . import merge_sort as mrgsrt
from . import bubble_sort as bblsrt
import time
import random

def measure_time(func, numbers):
    # Record the starting time
    start_time = time.perf_counter()

    # Sort the list of numbers using the provided sorting function
    sorted_numbers = func(numbers)

    # Record the ending time
    end_time = time.perf_counter()

    # Return the elapsed time in seconds and the sorted list of numbers
    return end_time - start_time, sorted_numbers


# Generate a list of random numbers
numbers = [random.randint(1, 100) for _ in range(100)]
print (numbers)

# Measure the time it takes for each sorting algorithm to sort the list
merge_sort_time, sorted_numbers = measure_time(mrgsrt, numbers)
bubble_sort_time, sorted_numbers = measure_time(bblsrt, numbers)

# Print the results
print(f"Merge sort took {merge_sort_time:.4f} seconds")
print(f"Bubble sort took {bubble_sort_time:.4f} seconds")