from time import sleep
from matplotlib import pylab
from random import choice
# funkcja hipotezy h(x) = teta0 + teta1*x
# funkcja kosztu  J(teta0, teta1) = 1/(2*m)*sum((h(x) - y)**2)
# minimalizacja J(teta0, teta1)
# funkcja gradientu prostego: teta0 = teta0 - alpha * 1/m * sum((h(x) - y)
#                             teta1 = teta1 - alpha * 1/m * sum((h(x) - y)*x

# [choice(range(10)) for _ in range(50)]
# [choice(range(10)) for _ in range(50)]

s_x =[9, 4, 5, 3, 8, 2, 5, 4, 3, 5, 9, 1, 3, 1, 2, 0, 6, 9, 3, 2, 8, 4, 0, 4, 9, 7, 4, 5, 6, 0, 8, 9, 1, 4, 8, 7, 9, 5, 4, 3, 8, 2, 8, 2, 7, 4, 0, 9, 1, 7]
s_y =[6, 3, 4, 6, 1, 4, 1, 9, 8, 1, 0, 8, 0, 5, 3, 7, 4, 5, 5, 4, 8, 1, 0, 7, 8, 0, 3, 2, 0, 7, 2, 2, 4, 1, 6, 1, 6, 8, 5, 9, 8, 4, 8, 8, 5, 1, 6, 7, 9, 1]

m  = len(s_x)

def cost_func_teta0(s_x, s_y, m, teta0, teta1):
    return 1/m * sum((((teta0 + teta1 * x) - y)) for x, y in zip(s_x, s_y))

def cost_func_teta1(s_x, s_y, m, teta0, teta1):
    return 1/m * sum(((teta0 + teta1 * x) - y)*x for x, y in zip(s_x, s_y))

def hipotese_f(x, teta0, teta1):
    return teta0 + teta1 * x


def gradient_descent(func0, func1, s_x, s_y, m, teta0, teta1, alpha, hipotese):
    gen = 0
    for loop in range(50000):
        f0 = func0(s_x, s_y, m, teta0, teta1)
        f1 = func1(s_x, s_y, m, teta0, teta1)
        tmp0 = teta0 - alpha * f0
        tmp1 = teta1 - alpha * f1
        teta0 = tmp0
        teta1 = tmp1
        print(teta0,'teta0')
        print(teta1, 'teta1')
        # set_h_x = [round(hipotese(x, teta0, teta1), 1) for x in s_x]
        # print(s_x)
        # print(set_h_x)
        # pylab.plot(s_x, set_h_x, 'b-', s_x, s_y, 'ro')
        # pylab.grid(True)
        # pylab.text(5, 10, 'generation {}'.format(gen))
        # pylab.show()
        gen += 1
    else:
        set_h_x = [round(hipotese(x, teta0, teta1), 1) for x in s_x]
        print(s_x)
        print(set_h_x)
        pylab.plot(s_x, set_h_x,'b-', s_x, s_y, 'ro')
        pylab.grid(True)
        pylab.text(5,10, 'generation {}'.format(gen))
        pylab.show()





print(gradient_descent(cost_func_teta0, cost_func_teta1, s_x, s_y, m, 0, 0, 0.01, hipotese_f))


set_x = [3, 1, 0, 4]
set_y =[2, 2, 1, 3]

def cost_func(teta0, teta1, set_x, set_y, m):
    return 1/(2 * m) * sum(((teta0 + teta1 * x) - y)**2 for x, y in zip(set_x, set_y))







