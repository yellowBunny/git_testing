
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