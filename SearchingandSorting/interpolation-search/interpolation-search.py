def interpolation_search(array, element, start_idx, end_idx):
    while start_idx <= end_idx and element >= array[start_idx] and element <= array[end_idx]:
        if start_idx == end_idx: 
            if array[start_idx] == element:  
                return start_idx; 
            return -1; 
        # pos = start_idx + int((element-array[start_idx])*(end_idx-start_idx) / (array[end_idx]-array[start_idx]))
        pos = start_idx + int(((float(end_idx - start_idx) / ( array[end_idx] - array[start_idx])) * ( element - array[start_idx])))
        if array[pos] == element:
            return pos
        if element < array[pos]:
            end_idx = pos - 1
        else:
            start_idx = pos + 1
    return -1


# Test array
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
target_element = 18

result = interpolation_search(arr, target_element, 0, len(arr)-1)
if result != -1:
    print('{0} found at {1}'.format(target_element, result))
else:
    print('{0} not found'.format(target_element))
