def binary_search(A, target, low, high):
    # Initialize step count
    steps = 0

    # Start the binary search loop
    while low <= high:
        # Increment step count for each comparison
        steps += 1

        # Calculate the middle index
        mid = (low + high) // 2

        # Check if the middle element is the target
        if A[mid] == target:
            return mid, steps
        # If the target is smaller, ignore the right half
        elif A[mid] > target:
            high = mid - 1
        # If the target is larger, ignore the left half
        else:
            low = mid + 1

    return -1, steps

# Input list and target value
A = [3, 7, 12, 18, 23, 27, 30, 35]
target = 4

# Call the binary search function
result, count = binary_search(A, target, 0, len(A) - 1)

# Handle the cases if target is not found or not found and print step count
if result != -1:
    print(f'Target found at index {result} after {count} steps')
else:
    print(f'Target not found after {count} steps')
