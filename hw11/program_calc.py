from calculator_app import Calc_UI


class Programming(Calc_UI):

    def __init__(self, r):
        self.root = r
        btn = [
            'C', 'D', 'E', 'F', '/', 'mod', '\u221A', 'AND',
            '8', '9', 'A', 'B', '*', '(',   ')',      'NOT',
            '4', '5', '6', '7', '-', 'OR', 'C',       'log',
            '0', '1', '2', '3', '+', 'XOR', '=',      'D']
        super().__init__(r, w=490, h=340, btn=btn, column_num=7)
        self.pack()
        self.set_main_ui()
        self.set_output_field()
        self.set_input_field()
        self.set_calculation_field()