def linear_search(numbers, target):
    # Loop through the list
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i  # Return index and step count
    return -1  # Return -1 if target is not found along with step count

# Input list
sample_list = [10, 22, 35, 47, 59, 63, 77, 81, 95, 102]

# Input target value
target = int(input("Enter the number to search: "))
index = linear_search(sample_list, target)
if index == -1:
  print("The target is not found!")
else: 
	print("The target is found at location:", index)
