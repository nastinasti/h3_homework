from calculator_app import Calc_UI


class Advanced(Calc_UI):

    def __init__(self, r):
        self.root = r
        btn = [
            '7', '8', '9', '/', 'C', 'D', 'cos', 'sin', 'tan',
            '4', '5', '6', '*', '(', ')', 'lg', 'ln', '\u03C0',
            '1', '2', '3', '-', '^', '\u221A', '\u221B', 'rad', 'deg',
            '0', '00', '.', '+', '%', 'abs', 'fac', '=']
        super().__init__(r, w=630, h=340, btn=btn, column_num=9)
        self.pack()
        self.set_main_ui()
        self.set_output_field()
        self.set_input_field()
        self.set_calculation_field()
