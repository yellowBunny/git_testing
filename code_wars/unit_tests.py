import unittest
import seba
import random
from string import ascii_lowercase as alphabet
from calc import Calc

class differentTests(unittest.TestCase):

    def test_simple_tests(self):
        equation = ['1 + 1 / 100 * 20 - 10', '1 + 1 + 1 + 1', '2 / 2 / 2 / 2', '10 + 1 * 12 / 3 + 2 + 2',
                    '1 * 1 * 1 * 1 * 1 * 1']
        for eq in equation:
            c = Calc(eq).compute()[-1]
            e = eval(eq)
            print(c, eval(eq))
            self.assertEqual(c, e)

    def test_rand_tests(self):
        signs = '+-*/'
        numbers = [str(num) for num in range(10)]
        rand_equation = ' '.join(random.choice(numbers) if i % 2 == 0 else random.choice(signs) for i in range(9))
        print(rand_equation)


if __name__ == '__main__':
    unittest.main()