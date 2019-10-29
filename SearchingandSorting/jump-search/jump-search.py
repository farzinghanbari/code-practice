def linear_search(array, element, offset):
    for index in range(0, len(array)):
        if array[index] == element:
            return index + offset
    return -1


def jump_search(array, element, start_idx, end_idx, step_size):
    interval_start = start_idx
    interval_end = interval_start + step_size
    offset = 0
    
    while interval_start <= end_idx:
        if element >= array[interval_start] and element <= array[interval_end]:
            return linear_search(array[interval_start:interval_end+1], element, offset)
        interval_start += step_size
        if interval_end + step_size >= end_idx:
            interval_end = end_idx
        else:
            interval_end += step_size
        offset += step_size
    return -1


# Test array
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
target_element = 55
step_size = 4

result = jump_search(arr, target_element, 0, len(arr)-1, step_size)
if result != -1:
    print('{0} found at {1}'.format(target_element, result))
else:
    print('{0} not found'.format(target_element))