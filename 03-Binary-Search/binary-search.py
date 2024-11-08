def binary_search(A, target, low, high):

    while low <= high:
        mid = (low + high) // 2

        if A[mid] == target:
            return mid
        elif A[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1 
A = [3, 7, 12, 18, 23, 27, 30, 35] 
target = 36
result = binary_search(A, target, 0, len(A)-1) 
if result != -1: 
    print(f'Target found at index {result}') 
else: 
    print('Target not found')
