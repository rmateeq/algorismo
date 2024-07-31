def find_max(numbers):
  # Define and initialize a variable `steps` to 0
  steps = 0
  max_number = numbers[0]
  for number in numbers:
    # Increment steps here
    steps += 1
    if number > max_number:
      max_number = number
  # Print steps here
  # The len() function returns the number of items in a list
  print("It took", steps, "steps to find the maximum number from a list of", len(numbers), "numbers")
  return max_number

# Use the following lists as input (one at a time) and take a count of `steps` (implemented inside the function `find_max`) it takes to find the maximum number from the input.
# Observe the change in the count of `steps` with changing input size (i.e., list length) and try to generalize it.

# Variation 1: Small list
sample_numbers = [5, 3, 9, 1, 6]
# Step count is: `5`
# Variation 2: Larger list
# sample_numbers = [8, 2, 10, 4, 7, 1, 12, 14, 3, 6]
# Step count is: `10`
# Variation 3: Even larger list
# sample_numbers = [15, 3, 9, 8, 22, 4, 13, 2, 11, 17, 1, 19, 6, 18, 7, 20, 5, 14, 10, 21, 16, 12]
# Step count is: `22`
print("The maximum number is:", find_max(sample_numbers))

# Genrally for a list of size `n`, the number of steps to find the maximum number is `n`.


# Explanation of Steps:
# For each list, the number of steps taken by the algorithm is equal to the number of elements in the list.
# This is because the algorithm iterates through each element once to find the maximum number.
# 
# For example:
# - For the list [5, 3, 9, 1, 6], there are 5 elements, so it takes 5 steps.
# - For the list [8, 2, 10, 4, 7, 1, 12, 14, 3, 6], there are 10 elements, so it takes 10 steps.
# - For the list [15, 3, 9, 8, 22, 4, 13, 2, 11, 17, 1, 19, 6, 18, 7, 20, 5, 14, 10, 21, 16, 12], there are 22 elements, so it takes 22 steps.
#
# In general, for a list of size n, the algorithm will take n steps because it needs to examine each element once to determine the maximum.
