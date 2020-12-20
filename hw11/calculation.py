import re
from collections import Counter

class Calculation:

    def result(self, res):
        print(f"Equation: {res} = ")
        if not res:
            return '0'
        for item in res:
            if item == '=' or item == ' ':
                res = res.replace('=', '')
        c = Counter(res)
        brekets_check = c['('] + c[')']
        pattern = r"([-+]?\d+\.\d+|[-+]?\d+)([-+*/])"
        while int(brekets_check)/2 != 0:
            sub_brackets = re.findall(r'\(([^()]*)\)', res)
            # sub_brackets = sub_brackets.group(1)
            print(f"subbrackets: {sub_brackets}")
            for item in sub_brackets:
                print(f"item  = {item}")
                match = re.split(pattern, str(item).replace(' ', ''))
                if len(match) > 1:
                    match = list(filter(None, match))
                    print(f"match: {match}")
                    self.operation(match)
                res = self._ch_remove(res, res.find(str(item)) - 1)
                res = self._ch_remove(res, res.find(str(item)) + len(item))
                res = res.replace(item, str(match[0]))
                print(f"im here. res after removing is {res}")
            new_c = Counter(res)
            brekets_check = int(new_c['('] + new_c[')'])
            print(f"amount of brackets pairs in the equation is {int(brekets_check) / 2}")
        if brekets_check == 0:
            print(f"res = {res}")
            print(f"new equation is: {res}")
            last_match = re.split(pattern, res.replace(' ', ''))
            last_match = list(filter(None, last_match))
            print(f"last match = {last_match}")
            return (''.join(self.operation(last_match)))
        # else:
        #     raise ValueError

    def _ch_remove(self, string, index):
        s = list(string)  # конвертируем в список
        del s[index]  # удаляем элемент с индексом index
        return "".join(s)

    def operation(self, last_match):
        while len(last_match) != 1:
            if '*' in last_match:
                self.check_for_match(last_match, self._mult, '*')
                print(last_match)
            if '/' in last_match:
                self.check_for_match(last_match, self._div, '/')
                print(last_match)
            if '%' in last_match:
                self.check_for_match(last_match, self._persentage, '%')
                print(last_match)
            if '-' in last_match:
                self.check_for_match(last_match, self._sub, '-')
                print(last_match)
            if '+' in last_match:
                self.check_for_match(last_match, self._sum, '+')
                print(last_match)
        return last_match

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
        print("sum")
        return a + b

    def _sub(self, a, b):
        print("sub")
        return a - b

    def _mult(self, a, b):
        print("mult")
        return a * b

    def _div(self, a, b):
        print("div")
        return a / b

    def _persentage(selfself, a, b):
        return a * b / 100

if __name__ == '__main__':
    calc = Calculation()
    res = '(50-(60+32)+6)/6'
    print(calc.result(res))

