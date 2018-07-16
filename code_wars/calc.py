import re
import operator

class Calc:
    def __init__(self, equation):
        self.operators = {'+' : lambda x, y: x + y,
                          '-' : lambda x, y: x - y,
                          '*' : lambda x, y: x * y,
                          '/' : lambda x, y: x / y,}

        self.splited_eq = re.findall(r'[0-9]+|[+-/*]', equation)
        # print(self.splited_eq)

    def first_to_compute(self):
        result = []
        c = []
        allowed_signs = ['/', '*']
        for i in range(len(self.splited_eq)):
            if self.splited_eq[i] in allowed_signs:
                result += self.splited_eq[i-1:i+2]
                print(self.splited_eq[i])
                c += [self.operators[self.splited_eq[i]](int(self.splited_eq[i-1]),int(self.splited_eq[i+1]))]
        print(result)
        print(c)

    def second_to_compute(self):
        result = []
        allowed_signs = ['+', '-']
        for i in range(len(self.splited_eq)):
            if self.splited_eq[i] in allowed_signs:
                result += self.splited_eq[i - 1:i + 2]
        print(result)



s = '1 + 1 / 100 * 20 - 10'
c = Calc(s)
c.first_to_compute()
# c.second_to_compute()
print(eval(s))

