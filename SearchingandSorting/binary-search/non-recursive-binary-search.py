def non_recursive_binary_search(array, element, start_idx, end_idx):
    
    while start_idx <= end_idx:
        mid = int((start_idx + end_idx) / 2)
        if array[mid] == element:
            return mid
        if element >= array[start_idx] and element < array[mid]:
            end_idx = mid
        elif element >= array[mid] and element <= array[end_idx]:
            start_idx = mid + 1
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
target_element = 10
result = non_recursive_binary_search(arr, target_element, 0, len(arr)-1)
if result != -1:
    print('{0} found at {1}'.format(target_element, result))
else:
    print('{0} not found'.format(target_element))