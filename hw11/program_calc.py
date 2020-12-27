from calculator_app import Calc_UI


class Programming(Calc_UI):

    def __init__(self, r):
        self.root = r
        btn = [
            'C', 'D', 'E', 'F', '/', 'mod', '\u221A', 'x\u207B\u00B9', 'AND', 'Bin',
            '8', '9', 'A', 'B', '*', '(',   ')', '.', 'NOT', 'Dec',
            '4', '5', '6', '7', '-', 'C', 'D', 'x!',        'OR', 'Oct',
            '0', '1', '2', '3', '+', 'log', 'log\u00B2', '=', 'XOR', 'Hex']
        super().__init__(r, w=700, h=340, btn=btn, column_num=10)
        self.pack()
        self.set_main_ui()
        self.set_output_field()
        self.set_input_field()
        self.set_calculation_field()