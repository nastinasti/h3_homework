import tkinter as calc_tk
from tkinter import messagebox as msg
from functools import partial
from calculation import Calculation


class Calc_UI(calc_tk.Canvas):
    def __init__(self, root):
        self.width = 420
        self.heigth = 340

        super().__init__(root, width=self.width, height=self.heigth)
        self.pack()
        self.set_main_ui()
        self.set_output_field()
        self.set_input_field()
        self.set_calculation_field()
        self.calc_manage = Calculation()


    def set_main_ui(self):
        root.title("Duck Calcurator 1.1.0")
        calculator_choices = {'Basic Mode', 'Advanced Mode', 'Programming Mode'}
        menu_bar = calc_tk.Menu(root, bg="#2b2b2b", bd=0, foreground="#c0c0c0")
        calcmenu = calc_tk.Menu(menu_bar, bg="#2b2b2b", foreground="#c0c0c0", tearoff=False)
        radio_option = calc_tk.StringVar()
        for choice in calculator_choices:
            cmd = partial(self.menuBar, choice)
            calcmenu.add_command(label=choice, command=cmd)
        menu_bar.add_cascade(label='Mode', menu=calcmenu)
        root.config(menu=menu_bar)
        self.frame = calc_tk.Frame(self, bg="#1d1d1b")
        self.frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    def set_output_field(self):
        output = calc_tk.Frame(self.frame, bg='#2b2b2b')
        output.place(relx=0.5, rely=0, relwidth=1, relheight=0.4, anchor='n')
        self.output_entry = calc_tk.Entry(output, bg="#2b2b2b", bd=0,
                                          highlightbackground="#2b2b2b", foreground="#c0c0c0")
        self.output_entry.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')


    def set_input_field(self):
        input_field = calc_tk.Frame(self.frame, bg='#343434')
        input_field.place(relx=0.5, rely=0.405, relwidth=1, relheight=0.15, anchor='n')
        self.input_entry = calc_tk.Entry(input_field, bg="#343434", bd=0,
                                         highlightbackground="#343434", foreground="#c0c0c0")
        self.input_entry.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    def set_calculation_field(self):
        calculate = calc_tk.Frame(self.frame, bg='#3e3e3e')
        calculate.place(relx=0.5, rely=0.56, relwidth=1, relheight=0.45, anchor='n')
        r = 0
        c = 1
        n = 0
        btn_list = [
            '7', '8', '9', '/', 'C', 'D',
            '4', '5', '6', '*', '(', ')',
            '1', '2', '3', '-', 'x^2', 'sqrt',
            '0', '00', '.', '+', '%', '=']
        for number in btn_list:
            cmd = partial(self.click, number)
            numbers = calc_tk.Button(calculate, text=number, width=3, height=1,
                                     bg="#484848", bd=0.2, highlightbackground="#484847", foreground="#c0c0c0",
                                     command=cmd)
            numbers.grid(row=r, column=c, ipadx=8, ipady=2, padx=2, pady=2)
            n += 1
            c += 1
            if c > 6:
                c = 1
                r += 1

    def click(self, btn):

        if btn == "C":
            self.input_entry.delete(0, calc_tk.END)
            self.output_entry.delete(0, calc_tk.END)
        elif btn == "=":
            self.result()
        elif btn == "D":
            self.input_entry.delete(self.input_entry.get()[-2], calc_tk.END)
        else:
            self.input_entry.insert(calc_tk.END, str(btn))

    def menuBar(self, choice):
        if str(choice) == 'Basic Mode':
            self.output_entry.delete(0, calc_tk.END)
            self.output_entry.insert(0, 'You are in the Basic mode')
        elif str(choice) == 'Advanced Mode':
            self.output_entry.delete(0, calc_tk.END)
            self.output_entry.insert(0, 'You are in the Advanced mode')
        elif str(choice) == 'Programming Mode':
            self.output_entry.delete(0, calc_tk.END)
            self.output_entry.insert(0, 'You are in the Programming mode')

    def result(self):
        check_str = "%+-/*)(.0123456789 "
        input_string = str(self.input_entry.get()).replace(' ', '')
        for item in input_string:
            if item not in check_str or self.calc_manage.result(input_string) == 0:
                msg.showerror("Error!", "Value error. Please check your input")
                raise ValueError

        self.output_entry.insert(0, self.calc_manage.result(input_string))



root = calc_tk.Tk()
calculator = Calc_UI(root)
root.resizable(width=False, height=False)
calculator.mainloop()
