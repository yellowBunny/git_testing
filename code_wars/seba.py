
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

#print(flat_arr(a))

def fib(n):
    a,b = 0,1
    f = 1
    l = []
    for _ in range(n+1):
        f += a + b
        l.append(a + b)
        a, b = b, a+b
    print(l)
    return 4*f

def two_lineary(u):
    l = [1]
    x = lambda i: 2 * i + 1
    y = lambda i: 3 * i + 1
    for i in range(u):
        if not x(l[i]) in l:
            l += [x(l[i])]
        if not x(l[i]) in l:
            l += [y(l[i])]
    print(sorted(l))
    return sorted(l)[u]

#print(two_lineary(100))

def num_sum(n):
    n = str(n)
    return [int(n[i]) + int(n[j+1]) for i in range(len(n)) for j in range(i, len(n)) if j < len(n) - 1]

import datetime

def target_date(a0, a, p):
    day0 = datetime.date(2016, 1 , 1)
    day = p / 36000
    days = 0
    while a0 <= a:
        a0 *= (1 + day)
        days += 1
    days = datetime.timedelta(days)
    return str(day0 + days)

# f = target_date(100, 150, 2)
# print(f)

def enter_dot(n):
    dots = int((len(str(n)[1:]) - 1) / 3) if n < 0 else int((len(str(n)) - 1) / 3)
    if n >= 10**3 or n <= -10**3:
        result = dots_entry(dots, n)
    else:
        return 0, str(n)
    return dots, result

def dots_entry(dots, n):
    str_n = str(n)
    lenght = len(str_n)
    i = (lenght - 3 * dots) - 1
    head = str_n[:i + 1] + ','
    tail = str_n[len(head) - 1:]
    if len(str_n) > 6:
        s = ''.join(name + ',' if num % 3 == 0 else name for num, name in enumerate(tail, 1)).strip(',')
        return head + s
    else:
        return head + tail

#print(enter_dot(1234567))

def match_results(s):
    digits = ['nil', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    hashed_str_digits = {digits[i]: i for i in range(10)}
    return [hashed_str_digits[word] for word in s.split() if word in hashed_str_digits]

#print(match_results('two two'))

def max_prod(array):
    alt = max([array[i] * array[i + 1] for i in range(len(array)) if i < len(array) - 1])
    return alt

#print(max_prod([1,2,3]))
from functools import reduce
def product(array):
    prod = []
    arrcp = array[::]
    for i, num in enumerate(array):
        arrcp[i] = ''
        prod += [reduce(lambda x,y: x * y, [num for num in arrcp if type(num) == int])]
        arrcp = array[::]
    return prod

#print(product([1, 4, 6]))

def index_a(arr):
    for i, num in enumerate(arr):
        if i == num:
            return i
    r = [i for i, num in enumerate(arr) if i == num]
    if r:
        return r[0]

    return -1

#print(index_a([-1,1,2,9,1]))

def makde_death_fish(data):
    d = {'i' : lambda x, y: x + y, 'd' : lambda x,y: x - y, 's' : lambda x: x**2, 'o' : []}
    start_val = 0
    for instruction in data:
        if instruction == 'i' or instruction == 'd':
            start_val = d[instruction](start_val, 1)
        elif instruction == 's':
            start_val = d[instruction](start_val)
        elif instruction == 'o':
            d[instruction] += [start_val]
    return d['o']
from math import factorial
def combinatios(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k)) if n >= k else 0

#print(combinatios(2,4))

def del_ltr(s, num):
    c = 0
    new_s = s
    for ltr in sorted(set(s)):
        c += new_s.count(ltr)
        sub = num - c
        new_s = new_s.replace(ltr, '', new_s.count(ltr) + sub)
        if c >= num:
            return new_s
    return ''


#print(del_ltr('abracadabra', 8))

def reverse_number(n):
    if n < 0 :
        new_s = int(str(abs(n))[::-1]) * -1
        return new_s
    return int(str(n)[::-1])


def prime_gap(g, m, n):
    primes = [num for num in range(m, n + 1) if all(num % i for i in range(2, int(num**.5) + 1))]
    result = []
    for i in range(len(primes)):
        if i < len(primes) - 1:
            if abs(primes[i] - primes[i + 1]) == g:
                result += [primes[i], primes[i+1]]
                if result:
                    return result

#print(prime_gap(2, 3, 50))

def backward_primes(a, b):
    primes = [num for num in range(a, b + 1) if all(num % i for i in range(2, int(num ** .5) + 1))]
    print(primes)
    backward = [num for num in primes if all(int(str(num)[::-1]) % i for i in range(2, int(int(str(num)[::-1]) ** .5) + 1)) and num > 11
                and num != int(str(num)[::-1])]
    return sorted(backward)
#print(backward_primes(100,400))

def fix_array(array):
    divided_by = [num for num in array if num / 3 % 1 == 0]


def entry(n):

    return n / 3 * 2

#print(fix_array([9,12,3,4,6,8])) # 9 / 3 * 2 = 6 in array T
def bubble_sort(arr):
    result = arr[::]
    for i in range(len(result) - 1):
        if result[i] > result[i + 1]:
            result[i], result[i + 1] = result[i + 1], result[i]
    return result

# arr = [2,5,3,1,6]
# print(bubble_sort(arr))

def prime_word(array):
    result = []
    f = lambda x, y: set([ele + y for ele in list(map(ord, list(x)))])
    prime = lambda x: all(x % i for i in range(2, int(x**.5) + 1))
    for arr in array:
        word, num = arr
        print(f(word, num))
        result += [any(1 for i in f(word, num) if prime(i))]
    return result

# sample = [['Emma', 30], ['Liam', 30]]
# print(prime_word(sample))

def substring(array1, array2):
    result = sorted(set([word for word in array1 for word2 in array2 if word in word2]))
    return result
# a1 = ["live", "arp", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# print(substring(a1, a2))

def weast(array):
    r = []
    l = ["NORTH", "SOUTH", "EAST", "WEST"]
    pass

#a1 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
#print(weast(a1))

def numerical_str(s):
    new_s = ''
    d = {ltr : 0 for ltr in set(s)}
    for ltr in s:
        d[ltr] += 1
        new_s += str(d[ltr])
    return new_s

#print(numerical_str('Hello, World'))

def hastags(s):
    result = '#' + ''.join([word.capitalize() for word in s.split()]) if s else False
    if not result: return False
    return result if len(result) < 140 else False

s = " Hello there thanks for trying my Kata"
#print(hastags(s))
import re
def morse_code(s):
    CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
            'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',

            '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', 'SOS': '...---...', '!': '-.-.--',

            }
    CODE2 = {val : key for key, val in CODE.items()}
    s = [ele for ele in re.findall(r'[.-]+|\s+',s) if ele != ' ']
    print(s)
    return ''.join(CODE2.get(code, ' ') for code in s)


#print(morse_code('...---...'))

def rectangle(array):
    team1, team2 = array
    if sum(team1) == sum(team2):
        for i in range(len(team1)-1):
            if team1[i] > team2[-i]:
                return 'Team 1 win!'
            elif team1[i] < team2[-i]:
                return 'Team 2 win!'
    return 'Team {} win!'.format(1 if sum(team1) > sum(team2) else 2)


def wind_rose(array):
    d = {'NORTH' : -1, 'SOUTH' : 1, 'EAST' : -2, 'WEST' : 2 }
    rev_d = {val : key for key, val in d.items()}
    new_arr = [d[direction] for direction in array]
    for _ in range(len(new_arr)):
        for i in range(len(new_arr) - 1):
            if i < len(new_arr) - 1:
                # print(abs(new_arr[i]) == abs(new_arr[i+1]), abs(new_arr[i]), abs(new_arr[i + 1]))
                if new_arr[i] + new_arr[i + 1] == 0:
                    new_arr[i: i + 2] = []
                    break
            #print([rev_d[num] for num in new_arr])
    return [rev_d[num] for num in new_arr]

# print(wind_rose(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

def rev_palidrome(s):
    c = 0
    for j in range(len(s)):
        for i in range(len(s)):
            r = check(s[i:j+1])
            r_rev = check(s[::-1][i:j+1])
            if r > c: c = r
            if r_rev > c: c = r_rev
    return c

def check(pal):
    print(pal == pal[::-1], '---->', pal, pal[::-1])
    if pal == pal[::-1]:
        return len(pal)
    else: return 0

#print(rev_palidrome('baablkj12345432133d'))

def sum_of_intervals(arrays):
    cp = arrays[::]
    result = []
    while cp:
        to_pop, r = com(cp)
        print(to_pop, r)
        result += [r]
        for i in to_pop:
            cp.remove(i)
    return sum(result)

def com(arr):
    arr = sorted(arr, key=lambda tup: tup[0])
    to_pop = [arr[0]]
    minimum = arr[0][0]
    maximum = arr[0][1]
    common = [minimum, maximum]
    for arr in arr[1:]:
        n1, n2 = arr
        if n1 < common[1]:
            to_pop += [arr]
            if n2 > common[1]:
                common[1] = n2
    n1, n2 = common
    return to_pop, n2 - n1

#print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))
# return len(set([n for (a, b) in intervals for n in [i for i in range(a, b)]]))

def common_2(array):
    s = set()
    for a, b in array:
        for n in [i for i in range(a,b)]: # 1,2,3| 7,8,9 | 4 |
            s.add(n)
    return len(s)

#print(common_2([(1, 4), (7, 10), (3, 5)]))
from time import sleep

def spread_to_prime_numbers(number):
    is_prime = lambda n: all(n % i for i in range(2,int(n**.5) + 1))
    divisiors = []
    c = 0
    while c < 2:
        for i in range(2, int(number ** .5) + 1):
            if is_prime(i):
                if number % i == 0:
                    number = int(number / i)
                    divisiors += [i]
                    c = 0
                    break
        c += 1
    divisiors += [number]
    return make_str(divisiors)

def make_str(array):
    my_set = []
    for num in array:
        if num not in my_set:
            my_set += [num]
    my_set = sorted(my_set)
    return ''.join('({}**{})'.format(num, array.count(num)) if array.count(num) > 1 else '({})'.format(num)
                  for num in my_set)




#print(spread_to_prime_numbers(86240))
#print(make_str([2,2,2,3,2,3,5,7,2,1231241,51,100]))
import re
def sentence(length, s):
    alt = sum(len(i) <= length for i in re.findall('\w+', s))
    print(alt)
    # return sum([1 for word in re.findall(r'[a-zA-Z]+', s) if len(word) <= length])

# print(sentence(4, "The Fox asked the stork, 'How is the soup?'"))

def legs(n=6):
    result = []
    max_cat = n//4
    max_human = n//2
    c = 0
    for i in range(max_cat):
        c += 4
        result += [(n-c)//2]
    # alt = [num for num in range(n//2) if num % 2 == 0]
    return sorted(result + [max_human])

# print(legs(8))

def encript(string):
    return ''.join(chr(ord(ltr) + i) for i, ltr in enumerate(string))

def decrypt(string):
    return ''.join(chr(ord(ltr) - i) for i, ltr in enumerate(string))


def longest_consec(strarr, k):
    if not strarr or len(strarr) < k or k <= 0: return ''
    result = ''
    for i in range(len(strarr)):
        if i + k <= len(strarr):
            new_arr = ''.join(strarr[j] for j in range(i, i+k))
            if len(new_arr) > len(result):
                result = new_arr
    return result
# print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3))

import functools



#print(reduce_func(som, [1,2,3], 0))

def gcd(a, b):
    '''ggrate common divisior - największy współny dzilnik'''
    while True:
        l = sorted([a, b, max(a, b) - min(a, b)])[::-1][1:]
        print(l)
        a, b= l[0],l[1]
        if l[-1] <=0:
            return l[0]

def gcd_modulo(a,b):
    a, b = max(a,b), min(a,b)
    while a%b:
        a, b = b, a%b
    return b

def gcd_simple(a,b):
    while True:
        a, b = min(a,b), abs(a - b) # a
        if b <= 0:
            return a

def lcm(a, b):
    '''lower common multilple'''
    return (a * b) // gcd(a, b)

def som(a, b):
    return a+b

def reduce_func(f, array, init):
    result = [init]
    for i in range(len(array)):
        tmp = f(result[-1], array[i])
        result += [tmp]
    return result[1:]
# [0,1,3,6,10][1:]

# sample = [2, 4, 6, 8, 10, 20]
#
# print(reduce_func(som, sample, 0))
import numpy as np
def theater(nCol, nRow, col, row):
    matrix = np.array([[nCol, nRow], [col - 1, row]])
    r = matrix[0] - matrix[1]
    return r[0] * r[1]


def sol(nRow, nCol, row, col):
    return (nRow - row + 1) * (nCol - col)

# print(theater(16, 11, 5, 3))

def occurent(list1, list2):
    new_list = ''.join(str(abs(num)) for num in list1)
    result = [(num, new_list.count(str(num))) for num in list2]
    return result


import functools
def geometri_sum(arr):
    new_arr = []
    invalid = []
    for num in arr:
        if num >= 0:
            new_arr += [num]
        if type(num) not in (int, float):
            invalid += [num]
        if len(invalid) > 1 : return 0
    return round(functools.reduce(lambda x,y: x * y, new_arr) ** (1/len(new_arr)), 11)

#print(geometri_sum( [-1, -1, 38, 23, 46, 49, 30, 50, 50, 18, 20, 8, 22, 30, 48, 8, 13, 29, 3, 28]))

def pillars(num, distance, width):
    if num <= 1: return 0
    if num >= 2:
        return (num - 1) * (distance * 100) + (num - 2) * width

class MyErrors(Exception):
    pass
class ArgumentNullException(MyErrors):
    pass
class InvalidOperatorException(MyErrors):
    pass
def array_prod(arr):
    if not arr:
        raise ArgumentNullException('input arg is empty')
    if 0 in arr:
        raise InvalidOperatorException('zero detected in array')
    return reduce(lambda x, y: x * y, arr)

#print(array_prod([]))

def signs_counter(arr):
    if not arr: return 0
    c = 0
    state = 0 if arr[0] < 0 else 1
    for num in arr:
        if num < 0:
            if not state == 0:
                c += 1
                state = 0
        else:
            if not state == 1:
                c += 1
                state = 1
    return c



