def find_max(numbers):
  # Define and initialize a variable `steps` to 0
  # 
  max_number = numbers[0]
  for number in numbers:
    # Increment steps here
    # 
    if number > max_number:
      max_number = number
  # Print steps here
  # 
  return max_number

# Use the following lists as input (one at a time) and take a count of `steps` (implemented inside the function `find_max`) it takes to find the maximum number from the input.
# Try to observe the change in the count of `steps` with changing input size (i.e., length of the list) and generalize it.

# Variation 1: Small list
sample_numbers1 = [5, 3, 9, 1, 6]
print("The maximum number is:", find_max(sample_numbers1))
# Step count is: ____

# Variation 2: Larger list
sample_numbers2 = [8, 2, 10, 4, 7, 1, 12, 14, 3, 6]
print("The maximum number is:", find_max(sample_numbers2))
# Step count is: ____

# Variation 3: Even larger list
sample_numbers3 = [15, 3, 9, 8, 22, 4, 13, 2, 11, 17, 1, 19, 6, 18, 7, 20, 5, 14, 10, 21, 16, 12]
print("The maximum number is:", find_max(sample_numbers3))
# Step count is: ____

# Genrally for a list of size `n`, the number of steps to find the maximum number is ____.
