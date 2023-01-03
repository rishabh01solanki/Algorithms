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

'''
# Main program
numbers = []

# Keep asking the user for numbers until they enter a blank line
while True:
    number = input("Enter a number (or press Enter to finish): ")
    if number == "":
        break
    else:
        numbers.append(int(number))

# Sort the list of numbers and print the result
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)
'''