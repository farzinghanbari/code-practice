def recursive_binary_search(array, element, start_idx, end_idx):
    if start_idx > end_idx:
        return -1
    mid = int((start_idx + end_idx) / 2)
    if array[mid] == element:
        return mid
    if element >= array[start_idx] and element < array[mid]:
        return binary_search(array, element, start_idx, mid)
    elif element >= array[mid] and element <= array[end_idx]:
        return binary_search(array, element, mid + 1, end_idx)
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
target_element = 10
result = recursive_binary_search(arr, target_element, 0, len(arr)-1)
if result != -1:
    print('{0} found at {1}'.format(target_element, result))
else:
    print('{0} not found'.format(target_element))