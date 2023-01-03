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

