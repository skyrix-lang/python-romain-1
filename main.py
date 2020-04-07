# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:16:57 2020

@author: romain
"""

from math import *
from tkinter import *
from tkinter import messagebox, ttk, filedialog
import os
import json

# Initialize parameters
tk_width = 1280
tk_height = 720
param_background = '#ECECEC'
param_from = -100
param_to = 100
param_width = 3
param_justify = CENTER
param_row_line_1 = 3
param_row_line_2 = 6
param_row_line_3 = 9
param_row_line_4 = 12
param_row_line_5 = 13
param_row_line_6 = 17
param_row_line_7 = 22



class Vect4D:
    def __init__(self, x, y, z, t):
        self.X = x
        self.Y = y
        self.Z = z
        self.T = t

    def __str__(self):
        return "(" + str(self.X) + " , " + str(self.Y) + " , " + str(self.Z) + " , " + str(self.T) + ")"

    def __add__(self, var):
        return (
            self.X + var.X,
            self.Y + var.Y,
            self.Z + var.Z,
            self.T + var.T)

    def __sub__(self, var):
        return (
            self.X - var.X,
            self.Y - var.Y,
            self.Z - var.Z,
            self.T - var.T)

    def __mul__(self, mat):
        if isinstance(mat, int) or isinstance(mat, float):
            return Vect4D(
            float(mat) * self.X,
            float(mat) * self.Y,
            float(mat) * self.Z,
            float(mat) * self.T)

        elif isinstance(mat, Vect4D):
            return Vect4D(
                    mat.X * self.X,
                    mat.Y * self.Y,
                    mat.Z * self.Z,
                    mat.T * self.T)
        else:
            raise Exception("Error: Invalid value (only float or vector)")

    def __eq__(self, var):
        if var is Vect4D:
            if self.X == var.X and self.Y == var.Y and self.Z == var.Z and self.T == var.T:
                return True
            else:
                return False

    def set_item(self, clef, valeur):
        if (clef == 'X') or (clef == 0):
            self.X = valeur
        elif (clef == 'Y') or (clef == 1):
            self.Y = valeur
        elif (clef == 'Z') or (clef == 2):
            self.Z = valeur
        elif (clef == 'T') or (clef == 3):
            self.T = valeur

    def get_item(self, clef):
        if (clef == 'X') or (clef == 0):
            return self.X
        elif (clef == 'Y') or (clef == 1):
            return self.Y
        elif (clef == 'Z') or (clef == 2):
            return self.Z
        elif (clef == 'T') or (clef == 3):
            return self.T

    def to_list(self):
        return [self.X, self.Y, self.Z, self.T]

    def module(self):
        mod = sqrt(self.X ** 2 + self.Y ** 2 + self.Z ** 2 + self.T ** 2)
        return mod


class Mat4D:
    def __init__(self, V1, V2, V3, V4):
        if isinstance(V1, Vect4D) and isinstance(V2, Vect4D) and isinstance(V3, Vect4D) and isinstance(V4, Vect4D):
            self.mat = [V1, V2, V3, V4]
        else:
            print("Une ou plusieurs valeurs ne sont pas des vecteurs")

    def __str__(self):
        return str(self.mat[0]) + "\n" + str(self.mat[1]) + "\n" + str(self.mat[2]) + "\n" + str(self.mat[3])

    def __add__(self, matrice):
        return self.mat + matrice

    def __sub__(self, matrice):
        return self.mat - matrice

    def __mul__(self, mat):
        if isinstance(mat, int) or isinstance(mat, float):
            vec = Vect4D(0, 0, 0, 0)
            result = Mat4D(vec, vec, vec, vec)
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        result.set_item(i, j, self.get_item(i, j) * float(mat))
            return result

        elif isinstance(mat, Vect4D):
            result = Vect4D(0, 0, 0, 0)
            temp = 0
            for i in range(4):
                for j in range(4):
                    temp += self.get_item(i, j) * mat.get_item(j)
                result.set_item(i, temp)
                temp = 0
            return result

        elif isinstance(mat, Mat4D):
            result = Mat4D(Vect4D(0, 0, 0, 0), Vect4D(0, 0, 0, 0), Vect4D(0, 0, 0, 0), Vect4D(0, 0, 0, 0))
            temp = 0
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        temp += self.get_item(i, k) * mat.get_item(k, j)
                    result.set_item(i, j, temp)
                    temp = 0
            return result
        else:
            raise Exception("Error: Invalid value (only float or vector or matrix 4D)")

    def __eq__(self, matrice):
        if matrice is Mat4D:
            return self.mat == matrice

    def set_item(self, ligne, colonne, valeur):
        if ligne == 0:
            self.mat[ligne].set_item(colonne, valeur)
        if ligne == 1:
            self.mat[ligne].set_item(colonne, valeur)
        if ligne == 2:
            self.mat[ligne].set_item(colonne, valeur)
        if ligne == 3:
            self.mat[ligne].set_item(colonne, valeur)

    def get_item(self, ligne, colonne):
        if ligne == 0:
            return self.mat[0].get_item(colonne)
        if ligne == 1:
            return self.mat[1].get_item(colonne)
        if ligne == 2:
            return self.mat[2].get_item(colonne)
        if ligne == 3:
            return self.mat[3].get_item(colonne)

    def to_list(self):
        return [self.mat[0].to_list(), self.mat[1].to_list(), self.mat[2].to_list(), self.mat[3].to_list()]


def id_4d():
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, 1, 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))


def sym_x():
    return Mat4D(Vect4D(-1, 0, 0, 0), Vect4D(0, 1, 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))


def sym_y():
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, -1, 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))


def sym_z():
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, 1, 0, 0), Vect4D(0, 0, -1, 0), Vect4D(0, 0, 0, 1))


def trans_x(x):
    return Mat4D(Vect4D(1, 0, 0, x), Vect4D(0, 1, 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))


def trans_y(y):
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, 1, 0, y), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))


def trans_z(z):
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, 1, 0, 0), Vect4D(0, 0, 1, z), Vect4D(0, 0, 0, 1))


def rot_x(teta):
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, cos(teta), sin(teta), 0), Vect4D(0, -sin(teta), cos(teta), 0), Vect4D(0, 0, 0, 1))


def rot_y(teta):
    return Mat4D(Vect4D(cos(teta), 0, sin(teta), 0), Vect4D(0, 1, 0, 0), Vect4D(-sin(teta), 0, cos(teta), 0), Vect4D(0, 0, 0, 1))


def rot_z(teta):
    return Mat4D(Vect4D(cos(teta), sin(teta), 0, 0), Vect4D(-sin(teta), cos(teta), 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def verify_spinbox(num):
    if check_int(num) is True:
        return True

    messagebox.showerror('Error', 'Values must be integers between ' + str(param_from) + ' and ' + str(param_to) + '!')
    return False


def calculate(window, val_teta1, val_teta2, val_teta3, val_teta4, val_l, val_x, val_y, val_z):
    values = [val_teta1, val_teta2, val_teta3, val_teta4, val_l, val_x, val_y, val_z]

    for i in values:
        if verify_spinbox(i) is False:
            return

    teta1 = float(val_teta1)
    teta2 = float(val_teta2)
    teta3 = float(val_teta3)
    teta4 = float(val_teta4)
    l = float(val_l)
    x = float(val_x)
    y = float(val_y)
    z = float(val_z)
    t = 1
    mat_temp = rot_x(teta1) * rot_y(teta2)
    mat_temp = mat_temp * rot_x(teta3)
    mat_temp = mat_temp * rot_z(teta4)
    mat_trans = mat_temp * trans_x(l)
    vector_p = mat_trans * Vect4D(x, y, z, t)

    lbl_mat_trans_value = Label(window, text=mat_trans, bg=param_background, highlightbackground=param_background)
    lbl_mat_trans_value.grid(column=7, columnspan=6, row=param_row_line_5, rowspan=4, sticky="ew")

    lbl_result_value = Label(window, text=vector_p, bg=param_background, highlightbackground=param_background)
    lbl_result_value.grid(column=7, columnspan=6, row=param_row_line_6, sticky="ew")

def laod(window):

    with open('path_to_file/person.json') as f:
        data = json.load(f)

    data_values =json.dumps(data)



def save(window, val_teta1, val_teta2, val_teta3, val_teta4, val_l, val_x, val_y, val_z):

    values={"teta1":val_teta1,
    "teta2":val_teta2,
    "teta3":val_teta3,
    "teta4":val_teta4,
    "L":val_l,
    "X":val_x,
    "Y":val_y,
    "Z":val_z,
    }

    with open('person.txt', 'w') as json_file:
        json.dump(values, json_file)

def make_responsive(tab):
    for i in range(0, 20):
        tab.rowconfigure(index=i, weight=1)
        tab.columnconfigure(index=i, weight=1)


def import_file(window, tab):
    root = Tk()
    root.withdraw()  # use to hide tkinter window

    currdir = os.getcwd()

    root.filename = filedialog.askopenfilename(initialdir=currdir, title="Select file",
                                               filetypes=[("Json", '*.json')])
    print(root.filename)


def fill_tab(window, tab, disabled=False, val_teta1=0, val_teta2=0, val_teta3=0, val_teta4=0, val_l=0, val_x=0, val_y=0,
             val_z=0):
    # Set default values
    default_value_teta_1 = IntVar()
    default_value_teta_1.set(val_teta1)
    default_value_teta_2 = IntVar()
    default_value_teta_2.set(val_teta2)
    default_value_teta_3 = IntVar()
    default_value_teta_3.set(val_teta3)
    default_value_teta_4 = IntVar()
    default_value_teta_4.set(val_teta4)
    default_value_l = IntVar()
    default_value_l.set(val_l)
    default_value_x = IntVar()
    default_value_x.set(val_x)
    default_value_y = IntVar()
    default_value_y.set(val_y)
    default_value_z = IntVar()
    default_value_z.set(val_z)

    # Initialize Label
    lbl_teta_1 = Label(tab, text='θ1', bg=param_background, highlightbackground=param_background)
    lbl_teta_2 = Label(tab, text='θ2', bg=param_background, highlightbackground=param_background)
    lbl_teta_3 = Label(tab, text='θ3', bg=param_background, highlightbackground=param_background)
    lbl_teta_4 = Label(tab, text='θ4', bg=param_background, highlightbackground=param_background)
    lbl_l = Label(tab, text='L', bg=param_background, highlightbackground=param_background)
    lbl_x = Label(tab, text='X', bg=param_background, highlightbackground=param_background)
    lbl_y = Label(tab, text='Y', bg=param_background, highlightbackground=param_background)
    lbl_z = Label(tab, text='Z', bg=param_background, highlightbackground=param_background)
    lbl_mat_trans_text = Label(tab, text='Matrice de transformation :', bg=param_background,
                               highlightbackground=param_background)
    lbl_result_text = Label(tab, text='The result is :', bg=param_background, highlightbackground=param_background)

    # Initialize Spinbox
    if disabled:
        active = 'disabled'
    else:
        active = 'normal'

    teta1 = Spinbox(tab, from_=param_from, to=param_to, width=param_width, justify=param_justify, state=active,
                    textvariable=default_value_teta_1, bg=param_background, highlightbackground=param_background,
                    command=lambda: calculate(tab, teta1.get(), teta2.get(), teta3.get(), teta4.get(), l.get(),
                                              x.get(), y.get(), z.get()))
    teta2 = Spinbox(tab, from_=param_from, to=param_to, width=param_width, justify=param_justify, state=active,
                    textvariable=default_value_teta_2, bg=param_background, highlightbackground=param_background,
                    command=lambda: calculate(tab, teta1.get(), teta2.get(), teta3.get(), teta4.get(), l.get(),
                                              x.get(), y.get(), z.get()))
    teta3 = Spinbox(tab, from_=param_from, to=param_to, width=param_width, justify=param_justify, state=active,
                    textvariable=default_value_teta_3, bg=param_background, highlightbackground=param_background,
                    command=lambda: calculate(tab, teta1.get(), teta2.get(), teta3.get(), teta4.get(), l.get(),
                                              x.get(), y.get(), z.get()))
    teta4 = Spinbox(tab, from_=param_from, to=param_to, width=param_width, justify=param_justify, state=active,
                    textvariable=default_value_teta_4, bg=param_background, highlightbackground=param_background,
                    command=lambda: calculate(tab, teta1.get(), teta2.get(), teta3.get(), teta4.get(), l.get(),
                                              x.get(), y.get(), z.get()))
    l = Spinbox(tab, from_=param_from, to=param_to, width=param_width, justify=param_justify, state=active,
                textvariable=default_value_l, bg=param_background, highlightbackground=param_background,
                command=lambda: calculate(tab, teta1.get(), teta2.get(), teta3.get(), teta4.get(), l.get(),
                                          x.get(), y.get(), z.get()))
    x = Spinbox(tab, from_=param_from, to=param_to, width=param_width, justify=param_justify, state=active,
                textvariable=default_value_x, bg=param_background, highlightbackground=param_background,
                command=lambda: calculate(tab, teta1.get(), teta2.get(), teta3.get(), teta4.get(), l.get(),
                                          x.get(), y.get(), z.get()))
    y = Spinbox(tab, from_=param_from, to=param_to, width=param_width, justify=param_justify, state=active,
                textvariable=default_value_y, bg=param_background, highlightbackground=param_background,
                command=lambda: calculate(tab, teta1.get(), teta2.get(), teta3.get(), teta4.get(), l.get(),
                                          x.get(), y.get(), z.get()))
    z = Spinbox(tab, from_=param_from, to=param_to, width=param_width, justify=param_justify, state=active,
                textvariable=default_value_z, bg=param_background, highlightbackground=param_background,
                command=lambda: calculate(tab, teta1.get(), teta2.get(), teta3.get(), teta4.get(), l.get(),
                                          x.get(), y.get(), z.get()))

    # Initialize Button
    if disabled:
        btn_calculate = Button(tab, text='Select File...', justify=param_justify, highlightbackground=param_background,
                               bg=param_background, command=lambda: import_file(window, tab))
    else:
        btn_calculate = Button(tab, text='Calculate', justify=param_justify, highlightbackground=param_background,
                               bg=param_background, command=lambda: calculate(tab, teta1.get(), teta2.get(),
                                                                              teta3.get(), teta4.get(), l.get(),
                                                                              x.get(), y.get(), z.get()))
    btn_quit = Button(tab, text='Quit', justify=param_justify, command=window.destroy, bg=param_background,
                      highlightbackground=param_background)

    # Place all widgets in the tab
    lbl_teta_1.grid(column=4, row=param_row_line_1, sticky="e")
    teta1.grid(column=5, row=param_row_line_1, sticky="w")
    lbl_teta_2.grid(column=6, row=param_row_line_1, sticky="e")
    teta2.grid(column=7, row=param_row_line_1, sticky="w")
    lbl_teta_3.grid(column=8, row=param_row_line_1, sticky="e")
    teta3.grid(column=9, row=param_row_line_1, sticky="w")
    lbl_teta_4.grid(column=10, row=param_row_line_1, sticky="e")
    teta4.grid(column=11, row=param_row_line_1, sticky="w")

    lbl_l.grid(column=7, row=param_row_line_2, sticky="e")
    l.grid(column=8, row=param_row_line_2, sticky="w")

    lbl_x.grid(column=5, row=param_row_line_3, sticky="e")
    x.grid(column=6, row=param_row_line_3, sticky="w")
    lbl_y.grid(column=7, row=param_row_line_3, sticky="e")
    y.grid(column=8, row=param_row_line_3, sticky="w")
    lbl_z.grid(column=9, row=param_row_line_3, sticky="e")
    z.grid(column=10, row=param_row_line_3, sticky="w")

    btn_calculate.grid(column=8, row=param_row_line_4, sticky="ew")

    lbl_mat_trans_text.grid(column=6, row=param_row_line_5, rowspan=4, sticky="ew")
    lbl_result_text.grid(column=6, row=param_row_line_6, sticky="ew")

    btn_quit.grid(column=18, row=param_row_line_7, sticky="ew")


def main():
    # Create tkinter window with properties
    window = Tk()
    window.title("Python TP6")
    window.geometry(str(tk_width) + 'x' + str(tk_height))
    window.minsize(tk_width//2, tk_height//2)
    window.configure(bg=param_background)

    # Create tabs
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Manual')
    tab_control.add(tab2, text='From Data')
    tab_control.pack(expand=1, fill='both')
    
    # Make window responsive
    make_responsive(tab1)
    make_responsive(tab2)

    # Fill tabs
    fill_tab(window, tab1)
    fill_tab(window, tab2, True)

    # Run calculate() method only one time for each tab
    window.after_idle(calculate, tab1, '0', '0', '0', '0', '0', '0', '0', '0')
    window.after_idle(calculate, tab2, '0', '0', '0', '0', '0', '0', '0', '0')

    # Loop
    window.mainloop()


main()
