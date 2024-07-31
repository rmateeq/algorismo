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
# Try to observe the change in the count of `steps` with changing input size (i.e., length of the list) and generalize it

# Variation 1: Small list
sample_numbers = [5, 3, 9, 1, 6]
# Variation 2: Larger list
# sample_numbers = [8, 2, 10, 4, 7, 1, 12, 14, 3, 6]
# Variation 3: Even larger list
# sample_numbers = [15, 3, 9, 8, 22, 4, 13, 2, 11, 17, 1, 19, 6, 18, 7, 20, 5, 14, 10, 21, 16, 12]

print("The maximum number is:", find_max(sample_numbers))
