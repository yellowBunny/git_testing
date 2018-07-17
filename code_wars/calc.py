import re

class Calc:
    def __init__(self, equation):
        self.operators = {'+' : lambda x, y: x + y,
                          '-' : lambda x, y: x - y,
                          '*' : lambda x, y: x * y,
                          '/' : lambda x, y: x / y,}

        self.splited_eq = re.findall(r'[0-9]+|[+-/*]', equation)
        # print(self.splited_eq)

    def compute(self):
        first_operators = self.first_to_compute(self.splited_eq, '/', '*')
        second_operators = self.first_to_compute(first_operators, '+','-')
        return second_operators

    def first_to_compute(self, equasion, *signs):
        cp = equasion[:]
        for _ in range(cp.count(signs[0]) + cp.count(signs[1])):
            for i in range(len(cp)):
                if cp[i] in signs:
                    print(cp[i])
                    equal = self.operators[cp[i]](float(cp[i-1]),float(cp[i+1]))
                    print(equal)
                    print(cp[i-1:i+2])
                    cp[i-1] = equal
                    del cp[i:i+2]
                    break
        return cp




s = '1 + 1 / 100 * 20 - 10'
c = Calc(s)
# print(c.compute())
c.first_to_compute('1 / 0', '/', '*')


