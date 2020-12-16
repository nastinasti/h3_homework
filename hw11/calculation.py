import re

class Calculation:

    def result(self, res):

        result_list = list()
        # while input_str != '=':
        #     input_str = input("Please input: ")
        #     res += input_str
        # res = '220 % 10= '
        print(res)
        for item in res:
            if item == '=' or item == ' ':
                res = res.replace('=', '')
        match = re.split(r"\s*([%+*/-])\s*", res)

        if '*' in match:
            self.check_for_match(match, self._mult, '*')
        if '/' in match:
            self.check_for_match(match, self._div, '/')
        if '%' in match:
            self.check_for_match(match, self._persentage, '%')
        if '+' in match:
            self.check_for_match(match, self._sum, '+')
        if '-' in match:
            self.check_for_match(match, self._sub, '-')
        return float(''.join(match))

    def check_for_match(self, match_list, func, sign):
        for item in match_list:
            if item == sign:
                a = float(match_list[match_list.index(item) - 1])
                b = float(match_list[match_list.index(item) + 1])
                match_list.pop(match_list.index(item) - 1)
                match_list.pop(match_list.index(item) + 1)
                times_result = func(a, b)
                match_list.insert(match_list.index(item), '{:.2f}'.format(times_result))
                match_list.pop(match_list.index(item))
                print(match_list)

    def _sum(self, a, b):
        return a + b

    def _sub(self, a, b):
        return a - b

    def _mult(self, a, b):
        return a * b

    def _div(self, a, b):
        return a / b

    def _persentage(selfself, a, b):
        return a * b / 100

if __name__ == '__main__':
    calc = Calculation()
    print(calc.result())

