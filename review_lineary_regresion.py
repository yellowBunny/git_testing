import numpy as np
import itertools

def add_x0_to_vectors(matrix):
    new_matrix = [[1]+list(map(int, vector.T)) for vector in matrix]
    return np.matrix(new_matrix)

matrix = np.matrix([[1,2,3],[4,5,6]])
tetas = np.matrix([12,10,1,3])
set_y = [10,12]
m = len(matrix[0].T)
matrix = add_x0_to_vectors(matrix)

print(matrix)

def hypotese_func(feature_vector, tetas):
    return float(feature_vector * tetas.T)

def cost_func(hypotese, matrix, tetas, set_y):
    return sum((hypotese(feature_vector, tetas) - y)**2 for feature_vector, y in zip(matrix, set_y))


def grad_test(hypo, matrix, tetas, set_y, i):
    result = 0
    for vector, y in zip(matrix, set_y):
        print(vector, y, vector.T[i])
        result += (hypo(vector, tetas) - y) * float(vector.T[i])
    return result

#print(grad_test(hypotese_func, matrix, tetas, set_y, 0))

def gradient(gradient_teta0, hypotese, matrix, tetas, set_y, alpha, m):
    t0 = []
    t1 = []
    t2 = []
    t3 = []
    teta0 = float(tetas.T[0])
    teta1 = float(tetas.T[1])
    teta2 = float(tetas.T[2])
    teta3 = float(tetas.T[3])

    for loop in range(1000):
        tmp0 = teta0 - alpha *(1/m*(gradient_teta0(hypotese, matrix, tetas, set_y, 0)))
        print('-'*10)
        tmp1 = teta1 - alpha *(1/m*(gradient_teta0(hypotese, matrix, tetas, set_y, 1)))
        print('-'*10)
        tmp2 = teta2 - alpha *(1/m*(gradient_teta0(hypotese, matrix, tetas, set_y, 2)))
        print('-'*10)
        tmp3 = teta3 - alpha *(1/m*(gradient_teta0(hypotese, matrix, tetas, set_y, 3)))
        print('-'*10)
        t0 += [tmp0]
        t1 += [tmp1]
        t2 += [tmp2]
        t3 += [tmp3]
        teta0 = tmp0
        teta1 = tmp1
        teta2 = tmp2
        teta3 = tmp3

    print(t0)
    print(t1)
    print(t2)
    print(t3)








print(gradient(grad_test, hypotese_func, matrix, tetas, set_y, 0.0001, m))

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






