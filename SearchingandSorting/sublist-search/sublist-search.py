def sublist_search(array1, array2):
    idx2 = 0
    elem2 = array2[idx2]
    for idx1 in range(0, len(array1)):
        elem1 = array1[idx1]
        if elem1 == elem2:
            flag = True
            if idx1 + len(array2) > len(array1):
                flag = False
            if flag:
                for temp_idx1, temp_idx2 in zip(range(idx1, idx1+len(array2)), range(0, len(array2))):
                    temp_elem1 = array1[temp_idx1]
                    temp_elem2 = array2[temp_idx2]
                    if temp_elem1 != temp_elem2:
                        flag = False
                        break
            if flag:
                return 1
    return -1


# Test array
arr1 = [10, 15, 25, 45, 55, 60, 70, 80]
arr2 = [60, 70, 80]

result = sublist_search(arr1, arr2)
if result == 1:
    print('subset matches')
else:
    print('subset DOES NOT matches')
