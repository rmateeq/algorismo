def linear_search(numbers, target):
    # Initialize step count
    steps = 0
    # Loop through the list
    for i in range(len(numbers)):
        # Increment step count for each iteration
        steps += 1
        if numbers[i] == target:
            return i, steps  # Return index and step count
    return -1, steps  # Return -1 if target is not found along with step count

# Input list
numbers = [10, 22, 35, 47, 59, 63, 77, 81, 95, 102]

# Test with three different targets
target_1 = 10  # Best case (Beginning of the list)
target_2 = 102  # Worst case (End of the list)
target_3 = 63  # Average case (Middle of the list)

# Call the function with each target and print the results
index_1, steps_1 = linear_search(numbers, target_1)
index_2, steps_2 = linear_search(numbers, target_2)
index_3, steps_3 = linear_search(numbers, target_3)

# Output with explicit messages for each case
print(f"Best case: Target {target_1} found at the beginning (index {index_1}) with {steps_1} steps.")
print(f"Worst case: Target {target_2} found at the end (index {index_2}) with {steps_2} steps.")
print(f"Average case: Target {target_3} found in the middle (index {index_3}) with {steps_3} steps.")
