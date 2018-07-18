import re

class Calc:
    def __init__(self, equation):
        self.equation = equation
        self.operators = {'+' : lambda x, y: x + y,
                          '-' : lambda x, y: x - y,
                          '*' : lambda x, y: x * y,
                          '/' : lambda x, y: x / y,}

    def compute(self):
        first_operators = self.first_to_compute(self.equation, '/', '*')
        if first_operators:
            second_operators = self.first_to_compute(first_operators, '+','-')
            return second_operators[-1]
        else:
            return 'you should not divide by zero !!'

    def first_to_compute(self, equation, *signs):
        if type(equation) == str:
            splited_eq = re.findall(r'[0-9]+|[+-/*]', equation)
        else:
            splited_eq = equation

        cp = splited_eq[:]

        for _ in range(cp.count(signs[0]) + cp.count(signs[1])):
            for i in range(len(cp)):
                if cp[i] in signs:
                    try:
                        equal = self.operators[cp[i]](float(cp[i-1]), float(cp[i+1]))
                        cp[i - 1] = equal
                        del cp[i : i + 2]
                        break
                    except ZeroDivisionError:
                        return False
        return cp




s = '1 + 1 / 100 * 20 - 10'
ss = '1 + 1 / 0'
c = Calc(s)
print(c.compute())

# print(c.first_to_compute('1 + 1 / 0', '/', '*'))


