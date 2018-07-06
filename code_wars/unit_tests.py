import unittest
import seba
import random
class differentTests(unittest.TestCase):
    # def testVertical(self):
    #     start = [0, 0]
    #     start1 = [2, 0]
    #     signs = ['', 'D', 'DD']
    #     signs1 = ['UU', 'U', '']
    #     for j in range(3):
    #         l = [[1 if col == 1 else 0 for col in range(3)] if row == j else [0 for col in range(3)] for row in
    #              range(3)]
    #         print('dla D = {}'.format(signs[j] if signs[j] else None))
    #         print('dla U = {}'.format(signs1[j] if signs1[j] else None))
    #         for arr in l:
    #             print(arr)
    #         self.assertEqual(seba.solutions(start, l), signs[j])
    #         self.assertEqual(seba.solutions(start1, l), signs1[j])

    # # testing for LEFT and RIGHT
    # def testHorizontal(self):
    #     start = [0, 0]
    #     start1 = [0, 2]
    #     signs = ['','R','RR']
    #     signs1 = ['LL','L','']
    #     for j in range(3):
    #         l = [[1 if i == j else 0 for i in range(3)] if row == 0 else [0 for _ in range(3)] for row in range(3)]
    #         for arr in l:
    #             print(arr)
    #         self.assertEqual(seba.solutions(start, l), signs[j])
    #         self.assertEqual(seba.solutions(start1, l), signs1[j])
    # #
    # testing vertival and horizontal solution
    # def testVerticalAndHoizontal(self):
    #     start = [0, 0]
    #     start1 = [0, 2]
    #     l = [[0, 0, 0], [0, 0, 1], [0 ,0, 0]]
    #     solutions = ['DRR','RRD']
    #     solutions1 = ['D']
    #     self.assertIn(seba.solutions(start, l),solutions)
    #     self.assertIn(seba.solutions(start1, l), solutions1)
    #
    #
    #     def board(l,rand):
    #         c = 0
    #         for i in range(len(l)):
    #             for j in range(len(l[i])):
    #                 c += 1
    #                 if c == rand:
    #                     l[i][j] = 1
    #                     return l
    #
    #     solutions_dict = {1: [''], 2: ['R'], 3: ['RR'], 4: ['D'], 5: ['DR', 'RD'],
    #                       6: ['DRR', 'RRD'], 7: ['DD'], 8: ['DDR', 'RDD'], 9: ['DDRR', 'RRDD']}
    #     # RANDOM TESTS
    #     for i in range(10):
    #         l = [[0 for i in range(3)] for row in range(3)]
    #         rand = random.choice(range(1, 10))
    #         print(rand)
    #         f = board(l, rand)
    #         for arr in f:
    #             print(arr)
    #         self.assertIn(seba.solutions(start, f), solutions_dict[rand])

    # check if cat in room
    def test_cat_in_room(self):
        cat = [-1,3]
        l = [[0 for i in range(3)] for _ in range(3)]
        self.assertTrue(seba.cat_coordinate(cat, l))
        cat = [1, 1]
        l = [[0 for i in range(3)] for _ in range(3)]
        self.assertFalse(seba.cat_coordinate(cat, l))




if __name__ == '__main__':
    unittest.main()