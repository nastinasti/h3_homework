import tkinter as calc_tk
from tkinter import messagebox as msg
from functools import partial
from basic_calc import Basic
from advance_calc import Advanced


class Calc_Menu(calc_tk.Canvas):
    def __init__(self, root, w=200, h=100):
        self.root = root
        self.width = w
        self.height = h
        self.main_colours = ["#c0c0c0", "#1d1d1b", "#2b2b2b", "#343434"]
        self.window_width = root.winfo_screenwidth() // 2
        self.window_height = root.winfo_screenheight() // 2

        super().__init__(root, width=w, height=h)
        self.pack()
        self.set_main_ui()

    def set_main_ui(self):
        self.root.title("Duck Calcurator 3.1.0")
        calculator_choices = {'Basic Mode', 'Advanced Mode', 'Programming Mode'}
        menu_bar = calc_tk.Menu(self.root, bg=self.main_colours[2], bd=0, foreground=self.main_colours[0])
        calcmenu = calc_tk.Menu(menu_bar, bg=self.main_colours[0], foreground=self.main_colours[2], tearoff=False)
        for choice in calculator_choices:
            cmd = partial(self.menuBar, choice)
            calcmenu.add_command(label=choice, command=cmd)
        menu_bar.add_cascade(label='Mode', menu=calcmenu)
        self.root.config(menu=menu_bar)
        self.frame = calc_tk.Frame(self, bg=self.main_colours[1])
        self.frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    def hide(self):
        self.root.withdraw()

    def menuBar(self, choice):
        if str(choice) == 'Basic Mode':
            msg.showinfo("INFO", "You are in the Basic mode")
            self.basic_win()
        elif str(choice) == 'Advanced Mode':
            msg.showinfo("INFO", "You are in the Advanced mode")
            self.advanced_win()
        elif str(choice) == 'Programming Mode':
            msg.showinfo("INFO", "You are in the Basic mode")

    def onCloseOtherFrame(self, otherFrame):
        otherFrame.destroy()
        self.show()

    def show(self):
        self.root.update()
        self.root.deiconify()

    def basic_win(self):
        root = calc_tk.Tk()
        basic = Basic(root)
        root.geometry('+{}+{}'.format(self.calc_window_width(root, 420), self.calc_window_height(root, 340)))
        root.resizable(width=False, height=False)
        basic.mainloop()

    def advanced_win(self):
        root = calc_tk.Tk()
        advanced = Advanced(root)
        root.geometry('+{}+{}'.format(self.calc_window_width(root, 500), self.calc_window_height(root, 340)))
        root.resizable(width=False, height=False)
        advanced.mainloop()

    def calc_window_width(self, root, width):
        return (root.winfo_screenwidth() // 2) - width // 2

    def calc_window_height(self, root, height):
        return root.winfo_screenheight() // 2 - height // 2


root = calc_tk.Tk()
menu = Calc_Menu(root)
root.geometry('+{}+{}'.format(menu.calc_window_width(root, 200), menu.calc_window_height(root, 100)))
root.resizable(width=False, height=False)
menu.mainloop()
