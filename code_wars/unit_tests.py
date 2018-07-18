import unittest
import seba
import random
#from calc import Calc

class CodeWars_tests(unittest.TestCase):
    def test_simple_test_dr_dsddr(self):
        '''check if computed numbers by f(n) are correct '''
        nums_to_compute = [5, 56, 28, 64, 18, 31]
        answers = [30, 13, 11, 11, 90, 20]
        for i in range(len(nums_to_compute)):
            self.assertEqual(seba.dr_dsddr(nums_to_compute[i]), answers[i],
                             'wrong equal {} != {}'.format(nums_to_compute[i], answers[i]))


    def test_simple_test(self):
        arr1 = [1,1,1,1,1,1]
        arr2 = [2,2,2,2,2,2,1]
        self.assertEqual(seba.trickey_sorted_array(arr1, arr2), [1],
                         'answer should be {} are {}'.format([1], seba.trickey_sorted_array(arr1, arr2)))




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