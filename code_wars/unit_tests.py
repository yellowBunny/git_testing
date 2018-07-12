import unittest
import seba
import random
from string import ascii_lowercase as alphabet


#class differentTests(unittest.TestCase):
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

    # def test_cat_in_room(self):
    #     cats = [[random.choice(range(-50,50)), random.choice(range(-50, 50))] for _ in range(10)]


        # l = [[0 for i in range(3)] for _ in range(3)]
        # self.assertTrue(seba.cat_coordinate(cat, l))
        # cat = [1, 1]
        # l = [[0 for i in range(3)] for _ in range(3)]
        # self.assertFalse(seba.cat_coordinate(cat, l))

    # def test_find_cat(self):
    #     n = 3
    #     l = [[0 for i in range(n)] for _ in range(n)]
    #     rand = random.choice(range(1, n**2))
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
    #     f = board(l, rand)
    #     print(f)

    # def test_cat_in_room(self):
    #     n = 100
    #     cats = [[random.choice(range(-20, 20)), random.choice(range(-20, 20))] for _ in range(n)]
    #     for cat in cats:
    #         rand1, rand2 = random.choices(range(1,20), k=2)
    #         l = [[0 for i in range(rand1)] for _ in range(rand2)]
    #         r, c = cat
    #         if r < 0 or c < 0:
    #             print('negatie nums')
    #             self.assertTrue(seba.cat_coordinate(cat, l))
    #         if r > len(l) or c > len(l[0]):
    #             print('second condition')
    #             self.assertTrue(seba.cat_coordinate(cat, l))


    # def test_coordinate_table(self):
    #     for _ in range(20):
    #         n, n1 = random.choices(range(2, 10), k=2)
    #         l = [[0 for i in range(n1)] for _ in range(n)]
    #         rand = random.choice(range((n*n1)//2))
    #         board = add_value(l, rand)
    #         ans = find_table(board)
    #         print(board)
    #         print(ans)
    #         print('-'*10)
    #         self.assertEqual(seba.room_map(board), ans)

    # def test_longest_empty_arr(self):
    #     arr = []
    #     c = 0
    #     while c < 20:
    #         i, j = random.choices(range(len(alphabet)), k=2)
    #         if i < j:
    #             arr.append(alphabet[i:j])
    #             c += 1
    #     for ele in arr:
    #         k = random.randint(len(ele),50)
    #         self.assertEqual(seba.longest_consec(ele, k), '')
    # def test_my_dict(self):
    #     d = seba.Dictionary()
    #     add_words = [['Socer', 'A sport'], ['Apple', 'a fruit'], ['RPG', 'a game'],
    #                  ['seba', 'a man'], ['', '']]
    #
    #     for key, word in add_words:
    #         d.newentry(key, word)
    #     print(d.__dict__)
    #
    #     for key, word in add_words:
    #         self.assertEqual(d.look(key), word)


class Seba_tests(unittest.TestCase):
    # manual tests
    def test_frelancer_manual(self):
        args = [[60, [(1,0)]], [60, [(0,0)]], [141, [(1,55), (0,25)]]]
        results = ['Easy Money!', "I need to work 1 hour(s) and 0 minute(s)", "I need to work 0 hour(s) and 1 minute(s)"]
        for i in range(len(results)):
            minutes, frelancers = args[i]
            func = seba.frelancer(minutes, frelancers)
            self.assertEqual(func, results[i])


if __name__ == '__main__':
    unittest.main()