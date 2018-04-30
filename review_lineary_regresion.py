import numpy as np
import itertools
from time import sleep

def add_x0_to_vectors(matrix):
    new_matrix = [[1]+list(map(int, vector.T)) for vector in matrix]
    return np.matrix(new_matrix)

matrix = np.matrix([[1,2,3],[4,5,6]])
tetas = np.matrix([0,0,0,0])
set_y = [10,12]
m = len(matrix[0].T)
matrix = add_x0_to_vectors(matrix)


def hypotese_func(feature_vector, tetas):
    return float(feature_vector * tetas.T)

def cost_func(hypotese, matrix, tetas, set_y):
    return sum((hypotese(feature_vector, tetas) - y)**2 for feature_vector, y in zip(matrix, set_y))


def grad_test(hypo, matrix, tetas, set_y, i):
    result = 0
    for vector, y in zip(matrix, set_y):
        #print(vector, y, vector.T[i])
        result += (hypo(vector, tetas) - y) * float(vector.T[i])
    return result

#print(grad_test(hypotese_func, matrix, tetas, set_y, 0))

def tetas_update(l):
    print(l)
    pass

def gradient(gradient_teta0, hypotese, matrix, tetas, set_y, alpha, m):
    tetas_copy = tetas[::]
    t0 = []
    t1 = []
    t2 = []
    t3 = []
    f0_l = []
    f1_l = []
    f2_l = []
    f3_l = []

    print(tetas_copy)
    for loop in range(1000):

        #sleep(1)
        f0 = (1/m*(gradient_teta0(hypotese, matrix, tetas_copy, set_y, 0)))# pobiera cały czas dane z wektora tetas... kurwa mać!!
        f1 = (1/m*(gradient_teta0(hypotese, matrix, tetas_copy, set_y, 1)))# pobiera cały czas dane z wektora tetas... kurwa mać!!
        f2 = (1/m*(gradient_teta0(hypotese, matrix, tetas_copy, set_y, 2)))# pobiera cały czas dane z wektora tetas... kurwa mać!!
        f3 = (1/m*(gradient_teta0(hypotese, matrix, tetas_copy, set_y, 3)))# pobiera cały czas dane z wektora tetas... kurwa mać!!

        tmp0 = float(tetas_copy.T[0]) - alpha * f0
        tmp1 = float(tetas_copy.T[1]) - alpha * f1
        tmp2 = float(tetas_copy.T[2]) - alpha * f2
        tmp3 = float(tetas_copy.T[3]) - alpha * f3

        t0 += [tmp0]
        t1 += [tmp1]
        t2 += [tmp2]
        t3 += [tmp3]
        f0_l += [f0]
        f1_l += [f1]
        f2_l += [f2]
        f3_l += [f3]

        # update tetas
        teta_martix = np.matrix([tmp0, tmp1, tmp2, tmp3])
        tetas_copy = teta_martix




    # printer
    print('teta0', t0)
    print('teta1', t1)
    print('teta2', t2)
    print('teta3', t3)
    print('func0', len(f0_l), f0_l)
    print('func1', len(f1_l), f1_l)
    print('func2', len(f2_l), f2_l)
    print('func3', len(f3_l), f3_l)








print(gradient(grad_test, hypotese_func, matrix, tetas, set_y, 0.01, m))

#print(gradient(gradient_teta0, hypotese_func, matrix, tetas, set_y, 0.01, m))



    # teta1 = float(tetas[1])
    # print(teta1)




# best_way = 100
# combinations = None
#
# teta0 = [num*.5 for num in range(-10, 15)]
# print(teta0)
#
# p = set(itertools.permutations(teta0, 4))
# p = map(list, p)
# #print(list(p))
#
# for teta in p:
#     teta = np.matrix(teta)
#     print(teta)
#     f = cost_func(hypotese_func, matrix, teta, set_y)
#     print(f)
#     print('-'*10)
#     if f < best_way:
#         best_way = f
#         combinations = teta
#
# print('optimum {}, {}'.format(best_way, combinations))



def f(teta):
    for n in range(10):
        teta.T[0] = n
    print(teta)


#print(f(tetas))