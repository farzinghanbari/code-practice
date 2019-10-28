def linear_search(array, element):
	for index in range(0, len(array)):
		if array[index] == element:
			return index
	return -1
input_array = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
target_element = 110
print('input:', input_array)
print('target:', target_element)
print()
result = linear_search(input_array, target_element)
if result != -1:
	print('{0} found at {1}'.format(target_element, result))
else:
	print('{0} not found'.format(target_element))