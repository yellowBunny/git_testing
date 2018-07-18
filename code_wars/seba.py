def trickey_sorted_array(array1 ,array2):
    common_elements = [i for i in array1 if i in array2]
    return sorted(common_elements, key = dr_dsddr, reverse=True)

def dr_dsddr(n):
    dr = sum(int(i) for i in str(n))
    dsddr = sum(int(j) ** 2 for j in str(sum(int(i) for i in str(n))))
    return dr + dsddr


arr1 = [5, 56, 28, 35, 12, 27, 64, 99, 18, 31, 14, 6]
arr2 = [28, 17, 31, 63, 64, 5, 18, 17, 95, 56, 37, 5, 28, 16]
l1 = [11 , 538, 919, 119]
l2 = [23, 45, 538, 119]
print(trickey_sorted_array(arr1, arr2))
#
# print(dr_dsddr(999))