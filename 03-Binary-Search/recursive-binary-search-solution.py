def recursive_binary_search(A, target, low, high):

    if low > high:
        return -1

    mid = (low + high) // 2

    if A[mid] == target:
        return mid
    elif A[mid] > target:
        return recursive_binary_search(A, target, low, mid - 1)  
    else:
        return recursive_binary_search(A, target, mid + 1, high) 

A = [3, 7, 12, 18, 23, 27, 30, 35] 
target = 7
result = recursive_binary_search(A, target, 0, len(A)-1) 
if result != -1: 
    print(f'Target found at index {result}') 
else: 
    print('Target not found')
