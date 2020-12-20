import re
from collections import Counter

class Calculation:

    operations = {
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b > 0 else False,
        '\u221A': lambda a, b: b ** a if a > 0 else False,
        '^': lambda a, b: pow(a, b),
        '%': lambda a, b: a * b / 100,
        '-': lambda a, b: a - b,
        '+': lambda a, b: a + b
    }

    def result(self, res):
        signs = ['+', '-', '*', '/', '%', '^', '\u221A']
        print(f"Equation: {res} = ")
        if not res:
            return '0'
        for item in res:
            if item == '=' or item == ' ':
                res = res.replace('=', '')
        c = Counter(res)
        brekets_check = c['('] + c[')']
        pattern = r"([-+]?\d+\.\d+|[-+]?\d+)(\u221A?)([-+*/^])(\u221A?)"
        try:
            while brekets_check/2 != 0:
                sub_brackets = re.findall(r'\(([^()]*)\)', res)
                if sub_brackets[0] == '':
                    return 0
                for item in sub_brackets:
                    print(f"item  = {item}")
                    match = re.split(pattern, str(item).replace(' ', ''))
                    print(f"match before: {match}")
                    if len(match) > 1:
                        match = list(filter(None, match))
                        print(f"match after: {match}")
                        self.operation(match)
                    res = self._ch_remove(res, res.find(str(item)) - 1)
                    res = self._ch_remove(res, res.find(str(item)) + len(item))
                    res = res.replace(item, str(match[0]))
                    print(f"im here. res after removing is {res}")
                new_c = Counter(res)
                brekets_check = int(new_c['('] + new_c[')'])
                print(f"amount of brackets pairs in the equation is {int(brekets_check) / 2}")
            for sign in signs:
                while sign in res:
                    if brekets_check == 0:
                        print(f"res = {res} for sign {sign}")
                        print(f"new equation is: {res}")
                        last_match = re.split(pattern, res.replace(' ', ''))
                        last_match = list(filter(None, last_match))
                        print(f"last match = {last_match}")
                        return ''.join(self.operation(last_match))
        except ValueError and IndexError:
            return False

    def _ch_remove(self, string, index):
        s = list(string)  # конвертируем в список
        del s[index]  # удаляем элемент с индексом index
        return "".join(s)

    def operation(self, last_match):
        keys = self.operations.keys()
        while len(last_match) != 1:
            if '\u221A' in last_match:
                self.check_for_match(last_match, self.operations['\u221A'], '\u221A')
            elif '^' in last_match:
                self.check_for_match(last_match, self.operations['^'], '^')
            elif '/' in last_match:
                self.check_for_match(last_match, self.operations['/'], '/')
            elif '*' in last_match:
                self.check_for_match(last_match, self.operations['*'], '*')
            elif '%' in last_match:
                self.check_for_match(last_match, self.operations['%'], '%')
            elif '-' in last_match:
                self.check_for_match(last_match, self.operations['-'], '-')
            elif '+' in last_match:
                self.check_for_match(last_match, self.operations['+'], '+')
        return last_match

    def check_for_match(self, match_list, func, sign):
        for item in match_list:
            if item == sign:

                if sign == '\u221A':
                    match_list.insert(match_list.index(item), '0')
                    a = 0.5
                else:
                    a = float(match_list[match_list.index(item) - 1])
                b = float(match_list[match_list.index(item) + 1])
                match_list.pop(match_list.index(item) - 1)
                match_list.pop(match_list.index(item) + 1)
                times_result = func(a, b)
                match_list.insert(match_list.index(item), '{:.2f}'.format(times_result))
                match_list.pop(match_list.index(item))

if __name__ == '__main__':
    calc = Calculation()
    res = '√50*((-600)/6*10+13*√(900)-3^6)/18+11'
    print(calc.result(res))

