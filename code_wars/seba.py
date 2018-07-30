
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



def string_packet(input_string):
    input_string = '-'.join(input_string[i:i+4] for i in range(len(input_string)) if i%4 == 0)
    header, instruction, data1, data2, footer = input_string.split('-')
    operators = {'0F12' : lambda x, y: x + y,
                'B7A2' : lambda x, y: x - y,
                'C3D9': lambda x, y: x * y}
    instead_operatos = 'FFFF'
    for oper in operators:
        if oper in input_string:
            compute_data1 = str(operators[oper](int(data1), int(data2))).zfill(4)
            if int(compute_data1) < 0:
                compute_data1 = '0000'
            elif int(compute_data1) > 9999:
                compute_data1 = '9999'
            output_string = header + instead_operatos + compute_data1 + '0000' + footer
            return output_string

# s = "H1H10F1200120008F4F4"
# print(string_packet(s))

def queue(arr, pos):
    c = 0
    cp_arr = arr[:]
    while cp_arr:
        for i in range(len(cp_arr)):
            if cp_arr[i] > 0:
                c += 1
            cp_arr[i] -= 1
            if cp_arr[pos] == 0:
                return c

def squareup(n):
    return [j if j - 1 <= i else 0 for i in range(n) for j in range(n, 0, -1)] # j = 4 - 1, 3-1, 2 - 1, i = 0


def roman_calendar(n):
    d = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L',
         100 : 'C', 500 : 'D', 1000 : 'M'}
    nums = [10**n for n in range(len(str(n)))]

    return nums

#print(roman_calendar(1234))
import string
def birthday(candles,debris):
    str_result = sum(ord(debris[i]) if i % 2 ==0 else string.ascii_lowercase.index(debris[i]) + 1
                     for i in range(len(debris)))
    print(str_result, candles * 1.7 - candles)
    if str_result > int(candles * 1.7 - candles):
        return 'Fire'
    else:
        return 'It was close'

# print(birthday(900, 'abcdef'))

import itertools
def trangle(array):
    comb = itertools.combinations(array, 2)
    return max(((ele[0][0] - ele[1][0])**2 + (ele[0][1] - ele[1][1]) ** 2) **.5 for ele in comb)


def flat_arr(array):
    return sorted(num for arr in array for num in arr)

a = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]

print(flat_arr(a))

