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
target_1 = 10  # Best case
target_2 = 102  # Worst case
target_3 = 63  # Average case

# Call the function with each target
print("Best case:", linear_search(numbers, target_1))
print("Worst case:", linear_search(numbers, target_2))
print("Average case:", linear_search(numbers, target_3))
