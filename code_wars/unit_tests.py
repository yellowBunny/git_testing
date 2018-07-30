import unittest
import seba
import random
#from calc import Calc
import sys
from string import ascii_uppercase, digits
class CodeWars_tests(unittest.TestCase):

    def test_trangle_simple_tests(self):
        array = [[[1,2], [3,8], [4,3]], [[1,2], [3, 7], [7, 8]]]
        ans = [6.325, 8.485]
        for i, arr in enumerate(array):
            self.assertAlmostEqual(seba.trangle(arr), ans[i], places=3)

    def test_trangle_rand_tests(self):
        pass








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







if __name__ == '__main__':
    unittest.main()