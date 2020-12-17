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
        breckets_result = list()
        c = Counter(res)
        brekets_check = c['('] + c[')']
        pattern = r"([-+]?\d+\.\d+|\d+)([-+*/])"
        if (brekets_check) % 2 == 0:
            sub_brackets = re.findall(r'\(([^\(\)]*)\)', res)
            for item in sub_brackets:
                match = re.split(pattern, str(item).replace(' ', ''))
                match = list(filter(None, match))
                print(f"match: {match}")
                if len(match) == 1:
                    match = match[0]
                    breckets_result = (float(match))
                    print(match)
                else:
                    self.operation(match)
                    breckets_result.append(float(match[0]))
        else:
            raise ValueError
        i = 0
        print(f"brekets_result: {breckets_result} type: {type(breckets_result)}")
        for item in sub_brackets:
            print(f"item: {item}")
            if len(breckets_result) > 0:
                res = res.replace(item, str(breckets_result[i]))
                print("im here")
                i = i + 1
            if breckets_result is list and len(breckets_result) == 1:
                print("im here")
                res = res.replace(item, str(float(breckets_result[0])))
            if breckets_result is float:
                print("im here")

        print(f"res = {res}")
        res = res.replace('(', '')
        res = res.replace(')', '')
        print(res)
        last_match = re.split(pattern, res.replace(' ', ''))
        last_match = list(filter(None, last_match))
        print(f"last match = {last_match}")
        return (''.join(self.operation(last_match)))

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
            for number in last_match:
                if number == '-':
                    self.sum_sub_oper(last_match, self._sub, '-')
                    print(last_match)
                if number == '+':
                    self.sum_sub_oper(last_match, self._sum, '+')
                    print(last_match)
        return last_match

    def sum_sub_oper(self, match_list, func, sign):
        # result = list()
        # i = 0
        # for item in match_list:
        #     a = float(match_list[i])
        #     b = float(match_list[i+2])
        #     if match_list[i+1] == sign:
        #         times_result = func(a, b)
        #         result.append('{:.2f}'.format(times_result))
        #         match_list.pop(i)
        # print(f"match list : {match_list}")
        # print(f"result: {result}")
        # return result
        pass


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
    res = '(5.0+6/54-60+10/8) /2 +9*10'
    print(calc.result(res))

