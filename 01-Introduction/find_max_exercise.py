def find_max(numbers):
  # define and initialize a variable `steps` to 0
  max_number = numbers[0]
  for number in numbers:
    # increment steps here
    if number > max_number:
      max_number = number
  # print steps here
  return max_number

# use the lists as input and take a count of `steps` (implemented inside the function `find_max`) it takes to find the maximum number from the input
sample_numbers = [5, 3, 9, 1, 6]
print("The maximum number is:", find_max(sample_numbers))
