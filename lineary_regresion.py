from time import sleep
from matplotlib import pylab

# funkcja hipotezy h(x) = teta0 + teta1*x
# funkcja kosztu  J(teta0, teta1) = 1/(2*m)*sum((h(x) - y)**2)
# minimalizacja J(teta0, teta1)
# funkcja gradientu prostego: teta0 = teta0 - alpha * 1/m * sum((h(x) - y)**2)
#                             teta1 = teta1 - alpha * 1/m * sum((h(x) - y)**2)*x
s_x = [1,2,3]
s_y = [1,2,3]
m  = len(s_x)



def cost_func_teta0(s_x, s_y, m, teta0, teta1):
    return 1/m * sum((((teta0 + teta1 * x) - y)) for x, y in zip(s_x, s_y))

def cost_func_teta1(s_x, s_y, m, teta0, teta1):
    return 1/m * sum(((teta0 + teta1 * x) - y)*x for x, y in zip(s_x, s_y))

def hipotese_f(x, teta0, teta1):
    return teta0 + teta1 * x


def gradient_descent(func0, func1, s_x, s_y, m, teta0, teta1, alpha, hipotese):

    for loop in range(100):
        tmp0 = teta0 - alpha * func0(s_x, s_y, m, teta0, teta1)
        tmp1 = teta1 - alpha * func1(s_x, s_y, m, teta0, teta1)
        teta0 = tmp0
        teta1 = tmp1
        print(teta0,'teta0')
        print(teta1, 'teta1')
        set_h_x = [round(hipotese(x, teta0, teta1), 1) for x in s_x]
        print(s_x , set_h_x)
        # pylab.plot(s_x, set_h_x)
        # pylab.grid(True)
        # pylab.show()


print(gradient_descent(cost_func_teta0, cost_func_teta1, s_x, s_y, m, 0, 0, 0.3, hipotese_f))
