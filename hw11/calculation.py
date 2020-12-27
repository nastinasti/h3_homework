import re
from collections import Counter
from logger_calculator import logger

class Calculation:

    operations = {
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else False,
        '\u221A': lambda a, b: b ** a if a > 0 else False,
        '^': lambda a, b: pow(a, b),
        '%': lambda a, b: a * b / 100,
        '-': lambda a, b: a - b,
        '+': lambda a, b: a + b
    }

    def result(self, res):
        signs = ['+', '-', '*', '/', '%', '^', '\u221A']
        logger.info(f"Equation: {res} = ")
        if not res:
            return '0'
        elif res.isdigit():
            return float(res)
        for item in res:
            if item == '=' or item == ' ':
                res = res.replace('=', '')
        c = Counter(res)
        brekets_check = c['('] + c[')']
        pattern = r"([-+]?)(\u221A)|([-+]?\d+\.\d+|[-+]?\d+)(\u221A?)([-+*/^])(\u221A?)"
        check = re.findall(r"(\u221A)([-+]?\d+\.\d+|[-+]?\d+)(\u221A)", res.replace(' ', ''))
        try:
            while brekets_check/2 != 0:
                sub_brackets = re.findall(r'\(([^()]*)\)', res)
                if sub_brackets[0] == '':
                    logger.info(f"subbreckets with [0] {sub_brackets}")
                    return 0
                for item in sub_brackets:
                    match = re.split(pattern, str(item).replace(' ', ''))
                    if len(match) > 1:
                        match = list(filter(None, match))
                        self.operation(match)
                    res = self._ch_remove(res, res.find(str(item)) - 1)
                    res = self._ch_remove(res, res.find(str(item)) + len(item))
                    res = res.replace(item, str(match[0]))
                new_c = Counter(res)
                brekets_check = int(new_c['('] + new_c[')'])
            for sign in signs:
                while sign in res:
                    if brekets_check == 0:
                        logger.info(f"new equation is: {res}")
                        if check:
                            return False
                        last_match = re.split(pattern, res.replace(' ', ''))
                        last_match = list(filter(None, last_match))
                        logger.info(f"List of the last equation items = {last_match}")
                        return ''.join(self.operation(last_match))
        except (ValueError, IndexError, ZeroDivisionError):
            logger.error(f"Input Error of the equation {res}")
            return False

    def _ch_remove(self, string, index):
        s = list(string)
        del s[index]
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
                if sign == '/' and b == 0:
                    raise ZeroDivisionError
                match_list.pop(match_list.index(item) - 1)
                match_list.pop(match_list.index(item) + 1)
                match_list.insert(match_list.index(item), '{:.2f}'.format(func(a, b)))
                match_list.pop(match_list.index(item))
                if match_list[0] == '-':
                    match_list[1] = str((-1) * float(match_list[1]))
                    match_list.pop(0)

if __name__ == '__main__':
    calc = Calculation()
    res = '√50000*√50000'#'√50*((-600)/6*10+13*√(900)-3^6)/18+11'
    print(calc.result(res))

