import tkinter as calc_tk
from tkinter import messagebox as msg
from functools import partial
from calculation import Calculation


class Calc_UI(calc_tk.Canvas):

    def __init__(self, root, w, h, btn, column_num):
        self.root = root
        self.width = w
        self.height = h
        self.main_colours = ["#c0c0c0", "#1d1d1b", "#2b2b2b", "#343434"]
        self.btn_list = btn
        self.column_num = column_num

        super().__init__(root, width=w, height=h)
        self.pack()
        self.set_main_ui()
        self.set_output_field()
        self.set_input_field()
        self.set_calculation_field()
        self.calc_manage = Calculation()
        root.bind('<Return>', self.result)
        root.bind('<KP_Enter>', self.result)
        root.bind('<BackSpace>', self._d_the_last)
        root.bind("<Key>", self.key)
        root.bind("<Control-q>", self.exit_win)

    def set_main_ui(self):
        self.root.title("Duck Calcurator 3.1.0")
        self.frame = calc_tk.Frame(self, bg=self.main_colours[1])
        self.frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    def set_output_field(self):
        output = calc_tk.Frame(self.frame, bg=self.main_colours[2])
        output.place(relx=0.5, rely=0, relwidth=1, relheight=0.4, anchor='n')
        self.output_entry = calc_tk.Entry(output, bg=self.main_colours[2], bd=0,
                                          highlightbackground=self.main_colours[2], foreground=self.main_colours[0])
        self.output_entry.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    def set_input_field(self):
        input_field = calc_tk.Frame(self.frame, bg=self.main_colours[3])
        input_field.place(relx=0.5, rely=0.405, relwidth=1, relheight=0.15, anchor='n')
        self.input_entry = calc_tk.Entry(input_field, bg=self.main_colours[3], bd=0,
                                         highlightbackground=self.main_colours[3], foreground=self.main_colours[0])
        self.input_entry.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    def set_calculation_field(self):
        calculate = calc_tk.Frame(self.frame, bg='#3e3e3e')
        calculate.place(relx=0.5, rely=0.56, relwidth=1, relheight=0.45, anchor='n')
        r = 0
        c = 1
        n = 0

        for number in self.btn_list:
            cmd = partial(self.click, number)
            numbers = calc_tk.Button(calculate, text=number, width=3, height=1,
                                     bg="#484848", bd=0.2, highlightbackground="#484847",
                                     foreground=self.main_colours[0],
                                     command=cmd)
            numbers.grid(row=r, column=c, ipadx=8, ipady=2, padx=2, pady=2)
            n += 1
            c += 1
            if c > self.column_num:
                c = 1
                r += 1

    def _d_the_last(self, event):
        self.input_entry.delete(len(self.input_entry.get()) - 1)

    def key(self, event):
        self.input_entry.insert(calc_tk.END, str(event.char))

    def exit_win(self, event):
        self.root.destroy()

    def click(self, btn):
        if btn == "C":
            self.input_entry.delete(0, calc_tk.END)
            self.output_entry.delete(0, calc_tk.END)
        elif btn == "=":
            self.output_entry.delete(0, calc_tk.END)
            self.result('<Return>')
        elif btn == "D":
            self._d_the_last('<BackSpace>')
        else:
            self.input_entry.insert(calc_tk.END, str(btn))

    def result(self, event):
        self.output_entry.delete(0, calc_tk.END)
        check_str = "%+-/*)(.0123456789√^"
        input_string = str(self.input_entry.get()).replace(' ', '')
        for item in input_string:
            if item not in check_str or not self.calc_manage.result(input_string):
                msg.showerror("Error!", "Please check your input")
                self.output_entry.insert(0, '0')
                raise ValueError
        self.output_entry.insert(0, self.calc_manage.result(input_string))

