from calculator_app import Calc_UI


class Basic(Calc_UI):
    def __init__(self, r):
        self.root = r
        btn = [
    '7', '8', '9', '/', 'C', 'D',
    '4', '5', '6', '*', '(', ')',
    '1', '2', '3', '-', '^', '\u221A',
    '0', '00', '.', '+', '%', '=']
        super().__init__(r, w=420, h=340, btn=btn, column_num=6)
        self.pack()
        self.set_main_ui()
        self.set_output_field()
        self.set_input_field()
        self.set_calculation_field()

