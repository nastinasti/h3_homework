import re
from collections import Counter
from logger_calculator import logger
import math

class Calculation:

    operations = {
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b if b != 0 else False,
        '\u221A': lambda a, b: b ** a if a > 0 else False,
        '^': lambda a, b: pow(a, b),
        '%': lambda a, b: a * b / 100,
        '-': lambda a, b: a - b,
        '+': lambda a, b: a + b,
        'sin': lambda a, b: math.sin(math.radians(b)) + a,
        'cos': lambda a, b: math.cos(math.radians(b)) + a,
        'tan': lambda a, b: math.tan(math.radians(b)) + a if b != 90 or b != 180 else False,
        'lg': lambda a, b: math.log(b, 10) + a,
        'ln': lambda a, b: math.log(b, math.e) + a,
        '\u221B': lambda a, b: b ** a,
        'rad': lambda a, b: b * math.pi / 180 + a,
        'deg': lambda a, b: b * 180 / math.pi + a,
        'abs': lambda a, b: math.fabs(b) + a,
        'fac': lambda a, b: math.factorial(b) + a
    }

    def result(self, res):
        signs = ['+', '-', '*', '/', '%', '^', '\u221A', '\u221B', '.',
                 'sin', 'cos', 'tan', 'rad', 'deg', 'abs', 'lg', 'ln', 'fac']
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
        print(f"res = {res}")
        pattern = r"([-]?\u221A|\u221B|sin|cos|tan|rad|deg|abs|lg|ln|fac)|([-]?\d+\.\d+|[-]?\d+|\d+\.\d+)" \
                  r"(\u221A?|\u221B?|sin?|cos?|tan?|rad?|deg?|abs?|lg?|ln?|fac?)" \
                  r"([-+*/^])(\u221A?|\u221B?|sin?|cos?|tan?|rad?|deg?|lg?|ln?|fac?)"
        check = re.findall(r"(\u221A)([-+]?\d+\.\d+|[-+]?\d+)(\u221A)", res.replace(' ', ''))
        print(f"check = {check}")
        try:
            while brekets_check/2 != 0:
                sub_brackets = re.findall(r'\(([^()]*)\)', res)
                if sub_brackets[0] == '':
                    logger.info(f"subbreckets with [0] {sub_brackets}")
                    return 0
                for item in sub_brackets:
                    match = re.split(pattern, str(item).replace(' ', ''))
                    print(f"match = {match}")
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
                            print("Good bye America O")
                            return False
                        last_match = re.split(pattern, res.replace(' ', ''))
                        last_match = list(filter(None, last_match))
                        logger.info(f"List of the last equation items = {last_match}")
                        return  ''.join(self.operation(last_match))
        except (ValueError, IndexError, ZeroDivisionError):
            logger.error(f"Input Error of the equation {res}")
            return False

    def _ch_remove(self, string, index):
        s = list(string)
        del s[index]
        return "".join(s)

    def operation(self, last_match):
        while len(last_match) != 1:
            if '\u221A' in last_match:
                self.check_for_match(last_match, self.operations['\u221A'], '\u221A')
            elif '\u221B' in last_match:
                self.check_for_match(last_match, self.operations['\u221B'], '\u221B')
            elif 'sin' in last_match:
                self.check_for_match(last_match, self.operations['sin'], 'sin')
            elif 'cos' in last_match:
                self.check_for_match(last_match, self.operations['cos'], 'cos')
            elif 'tan' in last_match:
                self.check_for_match(last_match, self.operations['tan'], 'tan')
            elif 'rad' in last_match:
                self.check_for_match(last_match, self.operations['rad'], 'rad')
            elif 'deg' in last_match:
                self.check_for_match(last_match, self.operations['deg'], 'deg')
            elif 'abs' in last_match:
                self.check_for_match(last_match, self.operations['abs'], 'abs')
            elif 'lg' in last_match:
                self.check_for_match(last_match, self.operations['lg'], 'lg')
            elif 'ln' in last_match:
                self.check_for_match(last_match, self.operations['ln'], 'ln')
            elif 'fac' in last_match:
                self.check_for_match(last_match, self.operations['fac'], 'fac')
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
            print(f"last match is = {last_match}")
        return last_match

    def check_for_match(self, match_list, func, sign):
        for item in match_list:
            if item == sign:
                if sign == '\u221A':
                    match_list.insert(match_list.index(item), '0')
                    a = 0.5
                elif sign == '\u221B':
                    print("here")
                    match_list.insert(match_list.index(item), '0')
                    a = 1/3
                elif sign == 'sin' or sign == 'cos' or sign == 'tan' \
                        or sign == 'rad' or sign == 'deg' or sign == 'abs'\
                        or sign == 'lg' or sign == 'ln' or sign == 'fac':
                    print(f"sign = {sign}")
                    match_list.insert(match_list.index(item), '0')
                    a = 0
                else:
                    a = float(match_list[match_list.index(item) - 1])
                b = float(match_list[match_list.index(item) + 1])
                if sign == '/' and b == 0:
                    raise ZeroDivisionError
                elif sign == 'tan' and (b == 90 or b == 180):
                    raise ValueError
                match_list.pop(match_list.index(item) - 1)
                match_list.pop(match_list.index(item) + 1)
                match_list.insert(match_list.index(item), '{:.2f}'.format(func(a, b)))
                match_list.pop(match_list.index(item))
                if match_list[0] == '-':
                    match_list[1] = str((-1) * float(match_list[1]))
                    match_list.pop(0)

if __name__ == '__main__':
    calc = Calculation()
    res = '3.14'#'fac3 + sin10 * cos30 + tan30 - deg2 + abs(-500) + lg50 - ln80 + rad18 * fac5 + √50*((-600)/6*10+13*∛(900)-3^6)/18+11'
    print(calc.result(res))

