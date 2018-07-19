import unittest
import seba
import random
#from calc import Calc
import sys
class CodeWars_tests(unittest.TestCase):

    def test_simply_test(self):
        numbers = [2, 3, 4, 5]
        answers = [8, 27, 64, 125]
        for i in range(len(numbers)):
            self.assertEqual(seba.sum_odd_numbers(numbers[i]), answers[i],
                             'should be {1} are {0}'.format(seba.sum_odd_numbers(4), answers[i]))



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