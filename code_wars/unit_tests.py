import unittest
import seba
import parse_data_from_site
import random, re, math, sys, os
from string import ascii_uppercase, digits, ascii_lowercase, ascii_letters

class CodeWars_tests(unittest.TestCase):

    pass

    # def test_signs_counter_basic_test(self):
    #     samples = [[1,2,3,4], [-1,1,2,3,4], [1, 2, -3, 3], [1,-1, 1, -1, 1]]
    #     answers = [0, 1, 2, 4]
    #     for sample, ans in zip(samples, answers):
    #         f = seba.signs_counter(sample)
    #         self.assertEqual(f, ans)

    # def test_sings_counter_random_test(self):
    #     samples = [[random.randint(-20,20) for _ in range(random.randint(5,20))] for _ in range(20)]
    #     def answers(arr):
    #         pass


    # def test_pillars_basic_test(self):
    #     num_col, distance, width = 1, 20, 40
    #     ans = 0
    #     f = seba.pillars(num_col, distance, width)
    #     self.assertEqual(f, ans)
    #
    # def test_pillars_basic_test_2(self):
    #     num_col, distance, width = 2, 30, 20
    #     ans = 3000
    #     f = seba.pillars(num_col, distance, width)
    #     self.assertEqual(f, ans)
    #
    # def test_pillars_basic_test_3(self):
    #     samples = [(3, 30, 50), (2, 20, 25), (11, 15, 30)]
    #     answers = [6050, 2000, 15270]
    #     for i , sample in enumerate(samples):
    #         num_col, distance, width = sample
    #         f = seba.pillars(num_col, distance, width)
    #         self.assertEqual(f, answers[i], 'should be {} is {}'.format(answers[i], f))


    # def test_geometri_sum_basic_test(self):
    #     sample = [2, 3, 4, 6]
    #     ans = 3.46410161514
    #     f = seba.geometri_sum(sample)
    #     self.assertEqual(f, ans)
    #
    # def test_geometric_sum1(self):
    #     sample = [2, 3, 4, 6, -5, '5']
    #     ans = 0
    #     f = seba.geometri_sum(sample)
    #     self.assertEqual(f, ans)
    #
    # def test_geometric_sum2(self):
    #     sample = [-1, -1, 38, 23, 46, 49, 30, 50, 50, 18, 20, 8, 22, 30, 48, 8, 13, 29, 3, 28]
    #     ans = 0
    #     f = seba.geometri_sum(sample)
    #     self.assertEqual(f, ans)



        # def test_occure_basic_test(self):
    #     l1, l2 = [1, 2, 5, 10, 12, 5, 1], [1, 2, 5]
    #     ans = [(1, 4), (2, 2), (5, 2)]
    #     f = seba.occurent(l1, l2)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))


    # def test_theter_basic_test(self):
    #     a,b,c,d = 16, 11, 5, 3
    #     ans = 96
    #     f = seba.theater(a,b,c,d)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_theater_rand_test(self):
    #     nRow, nCol = random.randint(3,200), random.randint(3,200)
    #     while True:
    #         row, col = random.randint(3,200), random.randint(3,200)
    #         if 1 < row <= nRow and 1 < col <= nCol:
    #             break
    #     print(nRow, nCol)
    #     print(row, col)
    #     def sol(nRow, nCol, row, col):
    #         return (nRow - row + 1) * (nCol - col)
    #
    #     for _ in range(2000):
    #         nRow, nCol = random.randint(3, 200), random.randint(3, 200)
    #         while True:
    #             row, col = random.randint(3, 200), random.randint(3, 200)
    #             if 1 < row <= nRow and 1 < col <= nCol:
    #                 break
    #         print(nRow, nCol)
    #         print(row, col)
    #         ans = sol(nRow, nCol, row, col)
    #         f = seba.theater(nRow, nCol, row, col)
    #
    #         self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))






    # def test_reduce_list_basic_test(self):
    #     a, b = [1, 1, 2, 3, 1, 2, 3, 4], [1, 3]
    #     ans = [2, 2, 4]
    #     f = seba.reduce_list(a, b)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_reduce_random(self):
    #     # a, b = [random.randint(0,100) for _ in range(10)], [random.randint(0,100) for _ in range(4)]
    #     ans = lambda arr1,arr2: [num for num in arr1 if num not in arr2]
    #     for _ in range(200):
    #         a, b = [random.randint(0, 100) for _ in range(10)], [random.randint(0, 100) for _ in range(4)]
    #         print(a, b)
    #         answer = ans(a, b)
    #         f = seba.reduce_list(a, b)
    #         self.assertEqual(f, answer, 'should be {} is {}'.format(answer, f))


    # def test_reduce_func_basic_test(self):
    #      init, arr = 0, [2, 4, 6, 8, 10, 20]
    #      ans = [2, 6, 12, 20, 30, 50]
    #      som = seba.som
    #      f = seba.reduce_func(som, arr, init)
    #      self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))

    # def test_gcd_basic_test(self):
    #     a, b = 6, 8
    #     ans = 2
    #     f = seba.gcd(a, b)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))

    # def test_gcd1(self):
    #     samples = [(6, 8), (24, 68), (125, 110)]
    #     ans = [2, 4, 5]
    #     for i, sample in enumerate(samples):
    #         print(sample)
    #         a, b = sample
    #         f = seba.gcd_simple(a, b)
    #         self.assertEqual(f, ans[i], 'should be {} is {}'.format(ans[i], f))

    # def test_gcd_random_test(self):
    #     samples = [(random.randint(1,2000), random.randint(1,2000)) for _ in range(100)]
    #     ans = [math.gcd(a, b) for a, b in samples]
    #     for i, sample in enumerate(samples):
    #         a, b = sample
    #         f = seba.gcd_simple(a, b)
    #         self.assertEqual(f, ans[i], 'should be {} is {}'.format(ans[i], ans[i]))

    # def test_lcm_basic_test(self):
    #     a, b = 6, 8
    #     ans = 24
    #     f = seba.lcm(a, b)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_lcm_random_tests(self):
    #     samples = [(random.randint(1, 2000), random.randint(1, 2000)) for _ in range(10)]
    #     sol = lambda x, y: (x * y) // math.gcd(x, y)
    #     ans = [sol(a, b) for a, b in samples]
    #     for i, sample in enumerate(samples):
    #         a, b = sample
    #         f = seba.lcm(a, b)
    #         self.assertEqual(f, ans[i])






    # def test_longest_consec_basic_test(self):
    #     arr, num = ['ab', 'xxx', 'y', 'xzaaw', 'pua'], 2
    #     ans = 'xzaawpua'
    #     f = seba.longest_consec(arr, num)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_longest_consec1(self):
    #     arr, num = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2
    #     ans =  "abigailtheta"
    #     f = seba.longest_consec(arr, num)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_longest_consec2(self):
    #     arr, num = ["zone", "abigail"], 3
    #     ans = ''
    #     f = seba.longest_consec(arr, num)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_longest_consec3(self):
    #     arr, num = [], 0
    #     ans = ''
    #     f = seba.longest_consec(arr, num)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_longest_consec4(self):
    #     arr, num = ['a','b','c'], 0
    #     ans = ''
    #     f = seba.longest_consec(arr, num)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))






    # def test_encript_decript_basic_test(self):
    #     e, d = 'aa', 'ab'
    #     f1, f2 = seba.encript(e), seba.decrypt(d)
    #     self.assertEqual(f1, d, 'should be {} {}'.format(d, f1))
    #     self.assertEqual(f2, e, 'should be {} {}'.format(e, f2))




    # def test_legs(self):
    #     samples = [6, 8, 10, 12, 14]
    #     ans = [[1, 3], [0, 2, 4], [1, 3, 5], [0, 2, 4, 6], [1, 3, 5, 7]]
    #     for i, sample in enumerate(samples):
    #         f = seba.legs(sample)
    #         self.assertEqual(f, ans[i], 'should be {} is {}'.format(ans[i], f))
    #
    # def test_legs_random_test(self):
    #
    #     def solution(n):
    #         return [num for num in range(0, n // 2 + 1, 2)] if n % 4 == 0 else [num for num in range(1, n // 2 + 1, 2)]
    #
    #
    #     samples = [random.choice(range(2,100,2))for _ in range(10)]
    #     ans = [solution(n) for n in samples]
    #     for i, sample in enumerate(samples):
    #         f = seba.legs(sample)
    #         self.assertEqual(f, ans[i], 'should be {} is {}'.format(ans[i], f))
    #



    # def test_word_length(self):
    #     length, sentence = 4, "The Fox asked the stork, 'How is the soup?'"
    #     ans = 7
    #     f = seba.sentence(length, sentence)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_word_lenght_random_test(self):
    #
    #     def solution(num, s):
    #         if not s: return 0
    #         c = 0
    #         for word in re.findall(r'[a-zA-Z]+', s):
    #             if len(word) <= num:
    #                 c += 1
    #         return c
    #     for _ in range(100):
    #         sentence = ' '.join([''.join(random.choice(ascii_letters) for i in range(random.randint(0,10))) for _ in range(random.randint(0,10))])
    #         number = random.randint(1,10)
    #         print(sentence, '---->', number)
    #         ans = solution(number, sentence)
    #         print('ANSWER')
    #         print(ans)
    #         f = seba.sentence(number, sentence)
    #         self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))





    # def test_make_arr(self):
    #     sample = [2,2,2,2,3,5,7,7]
    #     ans = '(2**4)(3)(5)(7**2)'
    #     f = seba.make_str(sample)
    #     self.assertEqual(f, ans, 'sohuld be {} is {}'.format(ans, f))
    #
    # def test_spread(self):
    #     sample = 7775460
    #     ans = "(2**2)(3**3)(5)(7)(11**2)(17)"
    #     f = seba.spread_to_prime_numbers(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))

    # def test_common_basic_test(self):
    #     sample = [(1,5), (3,6), (5,10)]
    #     ans = ([(1,5), (3,6), (5,10)], 9)
    #     f = seba.com(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_common1(self):
    #     samples = [[(0,3),(1,5),(4,20)], [(10, 80), (30, 50), (12, 93), (92,200)]]
    #     ans = [([(0,3),(1,5),(4,20)], 20), ([(10, 80), (30, 50), (12, 93), (92, 200)], 190)]
    #
    #     for i, sample in enumerate(samples):
    #         f = seba.com(sample)
    #         for tup in f[0]:
    #             self.assertIn(tup, ans[i][0])
    #
    # def test_common2(self):
    #     samples = [(2,8), (10, 20), (6,8)]
    #     ans = ([(2, 8), (6, 8)], 6)
    #     f = seba.com(samples)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_common3(self):
    #     samples = [(10, 20), (1, 8), (11, 29)]
    #     ans = ([(1,8)], 7)
    #     f = seba.com(samples)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_sum_of_itervals_basic_test(self):
    #     print('sum interval basic test')
    #     sample = [(1, 5), (3, 6), (5, 10)]
    #     ans = 9
    #     f = seba.sum_of_intervals(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_sum_of_itervals1(self):
    #     samples = [[(0, 3), (1, 5), (4, 20)], [(10, 80), (30, 50), (12, 93), (92, 200)]]
    #     ans = [20, 190]
    #     for i, sample in enumerate(samples):
    #         f = seba.sum_of_intervals(sample)
    #         self.assertEqual(f, ans[i], 'should be {} is {}'.format(ans, f))
    #
    # def test_sum_of_intervals_rand_test(self):
    #     samples = []
    #     while len(samples) <= 5 :
    #         tup = (random.randrange(1,200), random.randrange(1,200))
    #         minimum, maximum = tup
    #         if minimum < maximum:
    #             samples += [tup]
    #     print('SAMPLES')
    #     samples = sorted(samples, key=lambda tup: tup[0])
    #     print(samples)


    # def test_children(self):
    #     samples = [(10, 0), (0,0), (1, -10), (-100, -100)]
    #     ans = []
    #     for candy, ch_num in samples:
    #         f = seba.children(candy, ch_num)
    #         self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_children1(self):
    #     samples = [(7, 5), (10, 6), (11, 3)]
    #     ans = [[2, 2, 1, 1, 1], [2, 2, 2, 2, 1, 1], [4, 4, 3]]
    #     c = 0
    #     for candy, num in samples:
    #         f = seba.children(candy, num)
    #         self.assertEqual(f, ans[c], 'should be {} is {}'.format(ans[c], f))
    #         c += 1



    # def test_swap(self):
    #     d1, arr1 = [{'a' : 1, 'b' : 2, 'c' : 3}, ['y', 'x', 'z']]
    #     ans = {'y': 1, 'x' : 2, 'z' : 3}
    #     f = seba.swap(d1, arr1)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_swap2(self):
    #     d2, arr2 = [{'x' : 1, 'c' : 2, 'w' : 1 }, ['i', 'k', 'w']]
    #     ans = {'i' : 2, 'k' : 1, 'w' : 1}
    #     f = seba.swap(d2, arr2)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_rand1(self):
    #     alpha = ascii_lowercase
    #     r = random.choices(alpha, k=3)
    #     d1 = {r[i]: i for i in range(len(r))}
    #     l = random.choices(alpha, k=3)
    #
    #     def sol(d, arr):
    #         n_d = {}
    #         c = 0
    #         for key in sorted(d.keys()):
    #             n_d[arr[c]] = d[key]
    #             c += 1
    #         return n_d
    #
    #     for i in range(3,10):
    #         r = random.choices(alpha, k=i)
    #         d1 = {r[i]: i for i in range(len(r))}
    #         l = random.choices(alpha, k=i)
    #         ans = sol(d1, l)
    #         f = seba.swap(d1, l)
    #         self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))




    # def test_palindrom(self):
    #     sample = 'racecar'
    #     ans = 7
    #     f = seba.rev_palidrome(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_palidrome2(self):
    #     sample = 'aab'
    #     ans = 2
    #     f = seba.rev_palidrome(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_palindrome3(self):
    #     sample = 'baablkj12345432133d'
    #     ans = 9
    #     f = seba.rev_palidrome(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))





    # def test_wind_rose(self):
    #     sample = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    #     ans = [ "WEST"]
    #     f = seba.wind_rose(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_widn_rose_1(self):
    #     sample = ['NORTH'] * 10
    #     ans = sample
    #     f = seba.wind_rose(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_wind_rose_2(self):
    #     sample = ["NORTH", "WEST", "SOUTH", "EAST"]
    #     ans = sample
    #     f = seba.wind_rose(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_wind_rose3(self):
    #     sample = ['NORTH', 'NORTH', 'WEST', 'EAST', 'SOUTH']
    #     ans = ['NORTH']
    #     f = seba.wind_rose(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_wind_rose_random1(self):
    #     directions = ["NORTH", "WEST", "SOUTH", "EAST"]
    #     samples = [[random.choice(directions) for _ in range(10)]for _ in range(100)]
    #
    #     def solution(sample):
    #         result = sample
    #         d = {'NORTH' : 'SOUTH', 'WEST' : 'EAST', 'EAST': 'WEST', 'SOUTH': 'NORTH'}
    #         for _ in range(len(result)):
    #             for i in range(len(result) - 1):
    #                 if i < len(result) - 1:
    #                     if d[result[i]] == result[i + 1]:
    #                         result[i: i + 2] = []
    #         return result
    #
    #     for i, samp in enumerate(samples):
    #         print(i)
    #         ans = solution(samp)
    #         f = seba.wind_rose(samp)
    #         self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))





    # def test_morese(self):
    #     sample = '.... . -.--   .--- ..- -.. .'
    #     ans = 'HEY JUDE'
    #     f = seba.morse_code(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_morese_sos(self):
    #     sample = '...---...'
    #     ans = 'SOS'
    #     f = seba.morse_code(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))


    # def test_hastags(self):
    #     sample = " Hello there thanks for trying my Kata"
    #     ans = '#HelloThereThanksForTryingMyKata'
    #     f = seba.hastags(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    # def test_hastag_abowe_140char(self):
    #     sample = ' '.join([''.join(random.choice(ascii_lowercase) for _ in range(40)) for _ in range(10)])
    #     print(sample)
    #     f = seba.hastags(sample)
    #     self.assertFalse(f, 'should be FALSE is TRUE')
    #
    # def test_hastah_empty_str(self):
    #     sample = ''
    #     f = seba.hastags(sample)
    #     self.assertFalse(f, 'should be FALSE is TRUE')
    #
    # def test_hastag_radom_test(self):
    #     sample = [''.join(random.choice(ascii_lowercase) for _ in range(10)) for _ in range(10)]
    #     ans = '#' + ''.join(word.capitalize() for word in sample)
    #     f = seba.hastags(' '.join(sample))
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))


    # def test_numerical(self):
    #     samples = ['Hello, World!', 'aaaaaaaaaaa']
    #     ans = ['1112111121311','1234567891011']
    #     for i, sample in enumerate(samples):
    #         f = seba.numerical_str(sample)
    #         self.assertEqual(f, ans[i], 'should be {} is {}'.format(ans[i], f))


    # def test_prime_word(self):
    #     sample = [['Emma', 30], ['Liam', 30]]
    #     ans = [1,1]
    #     f = seba.prime_word(sample)
    #     self.assertEqual(f, ans, 'sholud be {} is {}'.format(ans, f))

    # def test_bubble_sort(self):
    #     sample = [2,5,3,1,6]
    #     ans = [2,3,1,5,6]
    #     f = seba.bubble_sort(sample)
    #     self.assertEqual(f, ans, 'should be {} is {}'.format(ans, f))
    #
    #
    #
    # def test_simple(self):
    #     samples = [123, 555, 112, -432, 1000, -10]
    #     ans = [321, 555, 211, -234, 1, -1]
    #     for i, sampel in enumerate(samples):
    #         f = seba.reverse_number(sampel)
    #         self.assertEqual(f, ans[i], 'should be {} is {}'.format(ans[i], f))
    #
    # def test_rand(self):
    #     sampels = [random.randrange(-100000, 100000)for _ in range(100)]
    #     conv = lambda x: -int(str(abs(x))[::-1]) if x < 0 else int(str(x)[::-1])
    #     ans = [conv(num) for num in sampels]
    #     for i, sampel in enumerate(sampels):
    #         print(sampel, '--->' ,ans[i])
    #         f = seba.reverse_number(sampel)
    #         self.assertEqual(f, ans[i], 'should be {} is {}'.format(ans[i], f))

    # def test_simple(self):
    #     samples = ['iiso', 'sisisdosddso']
    #     answers = [[4], [3, 49]]
    #     for i, sample in enumerate(samples):
    #         f = seba.makde_death_fish(sample)
    #         self.assertEqual(f, answers[i], 'should be {} is {}'.format(answers[i], f))

    # def test_simple(self):
    #     samples = ["The score is four nil", "new score: two three",
    #                "Arsenal just conceded another goal, two nil"]
    #     ans = [[4, 0], [2, 3], [2, 0]]
    #     for i in range(len(samples)):
    #         print(samples[i], '--->', ans[i])
    #         f = seba.match_results(samples[i])
    #         self.assertEqual(f, ans[i],
    #                          'shuld be {} is {}'.format(ans[i], f))
    #
    # def test_rand_test(self):
    #     print('RANDOM TEST STARTED')
    #     simpley_words = ['yes','club', 'Arsenal', 'Barcelona', 'win', 'lose', 'good', 'game',
    #                      'will', 'try', 'shot', 'goal', 'few', 'last', 'minute']
    #     digits = ['nil', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    #     hashed_str_digits = {digits[i]: i for i in range(10)}
    #     ran_sentense = []
    #     s = ''
    #     r = []
    #     for sentence in range(100):
    #         for _ in range(20):
    #             s += random.choices(simpley_words)[-1] + ' '
    #         else:
    #             tmp_r = []
    #             for _ in range(2):
    #                 rand = random.choices(digits)[-1]
    #                 s += rand + ' '
    #                 tmp_r += [hashed_str_digits[rand]]
    #             r += [tmp_r]
    #             tmp_r = []
    #             ran_sentense += [s.strip()]
    #             s = ''
    #     print(ran_sentense)
    #     print(r)
    #     for i in range(len(ran_sentense)):
    #         print(ran_sentense[i], '--->', r[i])
    #         f = seba.match_results(ran_sentense[i])
    #         self.assertEqual(f, r[i], 'should be {} is {}'.format(r[i], f))




    # def test_simpy_test(self):
    #     d = {1000000 : [2, '1,000,000'], 456789 : [1, '456,789'], 12 : [0, '12'], 100 : [0, '100'], 99999999 : [2, '99,999,999'],
    #          1091 : [1, '1,091'], -100 : [0, '-100'], -8888 : [1, '-8,888'], -9876543 : [2, '-9,876,543']}
    #     for inp, outp in d.items():
    #         print(inp, outp)
    #         f = seba.enter_dot(inp)
    #         self.assertEqual(f, tuple(outp), 'sould be {} is {}'.format(tuple(outp), f))
    #
    # def rev(self, number):
    #     n = str(abs(number))
    #     result = ''
    #     c = 0
    #     for i in range(1, len(n) + 1):
    #         result += n[-i]
    #         c += 1
    #         if c == 3:
    #             result += ','
    #             c = 0
    #     return '-' + result[::-1].strip(',') if number < 0 else result[::-1].strip(',')
    #
    # def test_random_tests(self):
    #     l = [random.randint(-10000000000, 10000000000) for _ in range(100)]
    #     for ele in l:
    #         f1, f2 = seba.enter_dot(ele)[1], self.rev(ele)
    #         print(f1, '---->', f2)
    #         self.assertEqual(f1, f2, 'should be {} is {}'.format(f1, f2))
    #




    # def test_bank_app_checking_days(self):
    #     dates = [366, 7299]
    #     args = [[100, 101, 0.98], [100, 150, 2]]
    #     for i in range(len(dates)):
    #         a0, a, p = args[i]
    #         func = seba.target_date(a0, a, p)
    #         self.assertEqual(func, dates[i], msg='should be {} si {}'.format(dates[i], func))

    # def test_corett_date(self):
    #     dates = ["2017-01-01", '2035-12-26', "2018-03-13"]
    #     args = [[100, 101, 0.98], [100, 150, 2], [9999, 11427, 6]]
    #     for i in range(len(dates)):
    #         a0, a, p = args[i]
    #         func = seba.target_date(a0, a, p)
    #         self.assertEqual(func, dates[i], msg='should be {} si {}'.format(dates[i], func))







    # def test_square_up_simple_test(self):
    #     sampels = (n for n in range(1,4))
    #     ans = [[1],[0, 1, 2, 1], [0, 0, 1, 0, 2, 1, 3, 2, 1], [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]]
    #     for i in range(3):
    #         self.assertEqual(seba.squareup(next(sampels)), ans[i])



    # def test_simple_equeue(self):
    #     l = [2, 5, 3, 6, 4]
    #     ans = [6, 18, 12, 20, 17]
    #     for i in range(len(l)):
    #         l = [2, 5, 3, 6, 4]
    #         self.assertEqual(seba.queue(l, i), ans[i],
    #                          'should be {} is {}'.format(ans[i], seba.queue(l, i)))


    # def test_simply_test(self):
    #     samples = ["H1H10F1200120008F4F4", 'H1H10F1201000100F4F4']
    #     answ = ["H1H1FFFF00200000F4F4", "H1H1FFFF02000000F4F4" ]
    #     for i in range(len(samples)):
    #         self.assertEqual(seba.string_packet(samples[i]), answ[i], 'should be {} are {}'.format(answ[i], seba.string_packet(samples[i])))
    #
    # def test_grate_than_9999(self):
    #     s = "H1H10F1200109999F4F4"
    #     answ = "H1H1FFFF99990000F4F4"
    #     self.assertEqual(seba.string_packet(s), answ)
    #
    # def test_bleow_0(self):
    #     s = "H1H1B7A200010010F4F4"
    #     answ = "H1H1FFFF00000000F4F4"
    #     self.assertEqual(seba.string_packet(s), answ)
    #
    # def test_rand_test(self):
    #     def answer(head, op, n1, n2, foth):
    #         d = {'0F12': lambda x, y: x + y,
    #              'B7A2': lambda x, y: x - y,
    #              'C3D9': lambda x, y: x * y}
    #         d1_d2 = d[op](int(n1), int(n2))
    #         if d1_d2 <= 0:
    #             d1_d2 = '0000'
    #         elif d1_d2 >= 9999:
    #             d1_d2 = '9999'
    #         else:
    #             d1_d2 = str(d1_d2).zfill(4)
    #         a = head + 'FFFF' + d1_d2 + '0000' + foth
    #         return a
    #
    #     for c in range(10):
    #         header = ''.join(random.choice(ascii_uppercase + digits) for _ in range(4))
    #         foother = ''.join(random.choice(ascii_uppercase + digits) for _ in range(4))
    #         operators = random.choice(['0F12', 'B7A2', 'C3D9'])
    #         num1, num2 = str(random.randint(1000,9999)), str(random.randint(1000,9999))
    #         created_string = header + operators + num1 + num2 + foother
    #         ans = answer(header, operators, num1, num2, foother)
    #         testing_function = seba.string_packet(created_string)
    #         self.assertEqual(testing_function, ans, msg='should be {} are {}'
    #                          .format(ans, testing_function))
    #         print('TEST {}\n {}\n {}\n --> PASSED <--'.format(c, created_string, testing_function))



   # def test_simple_test_dr_dsddr(self):
    #     '''check if computed numbers by f(n) are correct '''
    #     nums_to_compute = [5, 56, 28, 64, 18, 31]
    #     answers = [30, 13, 11, 11, 90, 20]
    #     for i in range(len(nums_to_compute)):
    #         self.assertEqual(seba.dr_dsddr(nums_to_compute[i]), answers[i],
    #                          'wrong equal {} != {}'.format(nums_to_compute[i], answers[i]))
    #
    # def test_1(self):
    #     '''all value in list are the same'''
    #     arr1 = [1,1,1,1,1,1]
    #     arr2 = [2,2,2,2,2,2,1]
    #     self.assertEqual(seba.trickey_sorted_array(arr1, arr2), [1],
    #                      'answer should be {} are {}'.format([1], seba.trickey_sorted_array(arr1, arr2)))
    #
    # def test_simple_test1(self):
    #     arr1 = [5, 56, 28, 35, 12, 27, 64, 99, 18, 31, 14, 6]
    #     arr2 = [28, 17, 31, 63, 64, 5, 18, 17, 95, 56, 37, 5, 28, 16]
    #     answer = [18, 5, 31, 56, 28, 64]
    #     func = seba.trickey_sorted_array(arr1, arr2)
    #     self.assertEqual(func, answer,
    #                      'FAILD answer should be {} are {}'.format(answer, func))
    #
    # def test_random_test1(self):
    #     arr1 = [random.randint(1, 2000) for _ in range(2000000)]
    #     arr2 = [random.randint(1, 2000) for _ in range(2000000)]
    #     print('--size-- in MB')
    #     print('{} MB - arr1'.format(sys.getsizeof(arr1) * 10 ** (-6)))
    #     print('{} MB - arr2'.format(sys.getsizeof(arr2) * 10 ** (-6)))
    #     return arr1, arr2
    #



# class differentTests(unittest.TestCase):
#
#     def test_simple_tests(self):
#         equation = ['1 + 1 / 100 * 20 - 10', '1 + 1 + 1 + 1', '2 / 2 / 2 / 2', '10 + 1 * 12 / 3 + 2 + 2',
#                     '1 * 1 * 1 * 1 * 1 * 1']
#         for eq in equation:
#             c = Calc(eq).compute()
#             e = eval(eq)
#             # print(c, eval(eq))
#             self.assertEqual(c, e)
#
#     def eva(self, rand_eq):
#         try:
#             return eval(rand_eq)
#         except ZeroDivisionError:
#             return 'you should not divide by zero !!'
#
#     def test_rand_tests(self):
#         signs = '+-*/'
#         numbers = [str(num) for num in range(100)]
#         for _ in range(10):
#             rand_equation = ' '.join(random.choice(numbers) if i % 2 == 0 else random.choice(signs) for i in range(31))
#             print(rand_equation)
#             c = Calc(rand_equation).compute()
#             print(c)
#             eq = self.eva(rand_equation)
#             print(eq)
#             self.assertEqual(c, eq, 'passed')
#             print('-' * 10)



class Prase_data(unittest.TestCase):

    # def test_save_to_file_basic_test(self):
    #     path = r'C:\Users\seb\Desktop\mieszkanie.txt'
    #     sample = ['jeden', 'dwa', 'trzy']
    #     f = parse_data_from_site.save_to_file(path, sample)
    #     dir_list = os.listdir(r'C:\Users\seb\Desktop')
    #     self.assertIn('mieszkanie.txt', dir_list)
    #     def read_file(file):
    #         with open(file, 'r') as f:
    #             s = f.read()
    #         return s
    #     ans = read_file(path)
    #     self.assertEqual(f, ans)
    pass






if __name__ == '__main__':
    unittest.main()