# Import the merge_sort and bubble_sort functions from the sorting module
import time
import random
import matplotlib.pyplot as plt
import numpy as np

def merge_sort(numbers):
    # If the list has more than one element, we need to split it and merge the sorted halves
    if len(numbers) > 1:
        # Calculate the middle index of the list
        middle_index = len(numbers) // 2

        # Split the list into two halves
        left_half = numbers[:middle_index]
        right_half = numbers[middle_index:]

        # Recursively sort the two halves
        left_half = merge_sort(left_half)
        right_half = merge_sort(right_half)

        # Merge the sorted halves
        merged = []
        left_index = 0
        right_index = 0
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] < right_half[right_index]:
                merged.append(left_half[left_index])
                left_index += 1
            else:
                merged.append(right_half[right_index])
                right_index += 1
        # Add any remaining elements from the left or right halves
        merged.extend(left_half[left_index:])
        merged.extend(right_half[right_index:])

        # Return the merged list
        return merged

    # If the list has only one element, it is already sorted
    else:
        return numbers

def bubble_sort(numbers):
    # Set swap counter to a non-zero value
    swap_counter = -1

    # Keep looping until the swap counter is 0
    while swap_counter != 0:
        # Reset the swap counter to 0
        swap_counter = 0

        # Loop through the list of numbers
        for i in range(len(numbers) - 1):
            # If the current number is greater than the next number,
            # swap them and increase the swap counter by 1
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swap_counter += 1

    # Return the sorted list of numbers
    return numbers


def measure_time(func, numbers):
    # Record the starting time
    start_time = time.perf_counter()

    # Sort the list of numbers using the provided sorting function
    sorted_numbers = func(numbers)

    # Record the ending time
    end_time = time.perf_counter()

    # Return the elapsed time in seconds
    return end_time - start_time

# Generate a list of random numbers
numbers = [random.randint(1, 100) for _ in range(100)]

# Measure the time it takes for each sorting algorithm to sort the list
merge_sort_time = measure_time(merge_sort, numbers)
bubble_sort_time = measure_time(bubble_sort, numbers)

# Print the results
print(f"Merge sort took {merge_sort_time:.4f} seconds")
print(f"Bubble sort took {bubble_sort_time:.4f} seconds")


