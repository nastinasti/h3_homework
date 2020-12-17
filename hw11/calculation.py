import re
from collections import Counter

class Calculation:

    def result(self, res):
        print(res)
        for item in res:
            if item == '=' or item == ' ':
                res = res.replace('=', '')
        breckets_result = list()
        c = Counter(res)
        brekets_check = c['('] + c[')']
        if (brekets_check) % 2 == 0:
            sub_brackets = re.findall(r'\(([^\(\)]*)\)', res)
            for item in sub_brackets:
                match = re.split(r"[-+]?[.]?[\s]+?([)(%+*/-])?\s*", item)
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
                breckets_result.append(match[0])
        else:
            raise ValueError
        i = 0
        for item in sub_brackets:
            res = res.replace(item, breckets_result[i])
            i = i+ 1
        res = res.replace('(', '')
        res = res.replace(')', '')
        last_match = re.split(r"\s*([%+*/-])\s*", res)

        if '*' in last_match:
            self.check_for_match(last_match, self._mult, '*')
        if '/' in last_match:
            self.check_for_match(last_match, self._div, '/')
        if '%' in last_match:
            self.check_for_match(last_match, self._persentage, '%')
        if '+' in last_match:
            self.check_for_match(last_match, self._sum, '+')
        if '-' in last_match:
            self.check_for_match(last_match, self._sub, '-')
        return float(''.join(last_match))

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
    res = '(-50 + 60 * 4)*2 - (90 - 1)'
    print(calc.result(res))

