from calculator_app import Calc_UI


class Advanced(Calc_UI):

    def __init__(self, r):
        self.root = r
        btn = [
            '7', '8', '9', '/', 'C', 'D', 'cos', 'sin',
            '4', '5', '6', '*', '(', ')', 'log', 'ln',
            '1', '2', '3', '-', '^', '\u221A', '\u221B', '\u03C0',
            '0', '00', '.', '+', '%', 'mod', 'x!', '=']
        super().__init__(r, w=590, h=340, btn=btn, column_num=8)
        self.pack()
        self.set_main_ui()
        self.set_output_field()
        self.set_input_field()
        self.set_calculation_field()
