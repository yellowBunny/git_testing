
def trickey_sorted_array(array1, array2):
    cm = set(array1) & set(array2)
    return sorted(sorted(cm), key=dr_dsddr, reverse=True)

def dr_dsddr(n):
    dr = sum(int(i) for i in str(n))
    dsddr = sum(int(j) ** 2 for j in str(sum(int(i) for i in str(n))))
    return dr + dsddr


# secont solution !!

def trickey2(array1, array2):
    cm = set(array1) & set(array2)
    return sorted(sorted(cm), key=dr_dsddr2, reverse=True)

def dr_dsddr2(n):
    dr = sum(map(int, str(n)))
    dsddr = sum(map(lambda x: int(x) ** 2, str(dr)))
    return dr + dsddr


def sum_odd_numbers(n):
    start, stop = sum(range(1, n+1)) - n, sum(range(1, n+1))
    l = list(range(1, stop * 2, 2))
    print(l)
    print(start, stop)
    print(l[start : stop])
    return sum(l[start : stop])

print(sum_odd_numbers(4))