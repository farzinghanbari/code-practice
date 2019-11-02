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


def exponential_search(array, element):
    if array[0] == element:
        return 0
    if element > array[len(array) - 1]:
        return -1
    pos = 1
    while pos < len(array) and array[pos] <= element:
        pos *= 2
    pos = min(pos, len(array) - 1)
    return non_recursive_binary_search(array, element, int(pos / 2), pos)


# Test array
arr = [10, 15, 25, 45, 55, 60, 70, 80]
target_element = 10

result = exponential_search(arr, target_element)
if result != -1:
    print('{0} found at {1}'.format(target_element, result))
else:
    print('{0} not found'.format(target_element))
