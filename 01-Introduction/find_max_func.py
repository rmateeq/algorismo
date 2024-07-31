def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

sample_numbers = [5, 3, 9, 1, 6]
print("The maximum number is:", find_max(sample_numbers))
