# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:16:57 2020

@author: romain
"""

from math import *
from tkinter import *
from tkinter import messagebox

# Initialize parameters
param_background = '#ECECEC'
param_from = -100
param_to = 100
param_width = 3
param_justify = CENTER
param_row_line_1 = 0
param_row_line_2 = 3
param_row_line_3 = 6
param_row_line_4 = 9
param_row_line_5 = 13
param_row_line_6 = 18


class Vect4D:
    def __init__(self, x, y, z, t):
        self.X = x
        self.Y = y
        self.Z = z
        self.T = t

    def __str__(self):
        return "(" + str(self.X) + " " + str(self.Y) + " " + str(self.Z) + " " + str(self.T) + ")"

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
        if mat.replace(".", "", 1).isdigit():
            self.X = float(mat) * self.X
            self.Y = float(mat) * self.Y
            self.Z = float(mat) * self.Z
            self.T = float(mat) * self.T

        elif isinstance(mat, Vect4D):
            return (
                    mat.X * self.X +
                    mat.Y * self.Y +
                    mat.Z * self.Z +
                    mat.T * self.T)
        else:
            raise Exception("Error: Invalid value (only float or vector)")

    def __eq__(self, var):
        if (var is Vect4D):
            if (self.X == var.X and self.Y == var.Y and self.Z == var.Z and self.T == var.T):
                return True
            else:
                return False

    def set_item(self, clef, valeur):
        if ((clef == 'X') or (clef == 1)):
            self.X = valeur
        if ((clef == 'Y') or (clef == 2)):
            self.Y = valeur
        if ((clef == 'Z') or (clef == 3)):
            self.Z = valeur
        if ((clef == 'T') or (clef == 4)):
            self.T = valeur

    def get_item(self, clef):
        if ((clef == 'X') or (clef == 1)):
            return self.X
        if ((clef == 'Y') or (clef == 2)):
            return self.Y
        if ((clef == 'Z') or (clef == 3)):
            return self.Z
        if ((clef == 'T') or (clef == 4)):
            return self.T

    def to_list(self):
        return [self.X, self.Y, self.Z, self.T]

    def module(self):
        mod = sqrt(self.X ** 2 + self.Y ** 2 + self.Z ** 2 + self.T ** 2)
        return mod


class Mat4D:
    def __init__(self, V1, V2, V3, V4):
        if (isinstance(V1, Vect4D) and isinstance(V2, Vect4D) and isinstance(V3, Vect4D) and isinstance(V4, Vect4D)):
            self.mat = [V1, V2, V3, V4]
        else:
            print("Une ou plusieurs valeurs ne sont pas des vecteurs")

    def __str__(self):
        V1 = 'V1: ' + str(self.mat[0].affichage()) + ', '
        V2 = 'V2: ' + str(self.mat[1].affichage()) + ', '
        V3 = 'V3: ' + str(self.mat[2].affichage()) + ', '
        V4 = 'V4: ' + str(self.mat[3].affichage())
        return V1 + V2 + V3 + V4

    def __add__(self, matrice):
        return (self.mat + matrice)

    def __sub__(self, matrice):
        return (self.mat - matrice)

    def __mul__(self, mat):
        if (isinstance(mat, int) or isinstance(mat, float)):
            vec = Vect4D(0, 0, 0, 0)
            result = Mat4D(vec, vec, vec, vec)
            for i in range(1, 5):
                for j in range(1, 5):
                    for k in range(1, 5):
                        result.set_item(i, j, self.get_item(i, j) * float(mat))
            return result

        elif (isinstance(mat, Vect4D)):
            vec = Vect4D(0, 0, 0, 0)
            result = Mat4D(vec, vec, vec, vec)
            temp = 0
            for i in range(1, 5):
                for j in range(1, 5):
                    for k in range(1, 5):
                        temp += self.get_item(j, k) * mat.get_item(i)
                    result.set_item(i, j, temp)
                temp = 0
            return result

        elif (isinstance(mat, Mat4D)):
            vec = Vect4D(0, 0, 0, 0)
            result = Mat4D(vec, vec, vec, vec)
            temp = 0
            for i in range(1, 5):
                for j in range(1, 5):
                    for k in range(1, 5):
                        temp += self.get_item(i, k) * mat.get_item(k, j)
                    result.set_item(i, j, temp)
                temp = 0
            return result
        else:
            raise Exception("Error: Invalid value (only float or vector or matrix 4D)")

    def __eq__(self, matrice):
        if (matrice is Mat4D):
            if (self.mat.equals(matrice) == True):
                return True
            else:
                return False

    def set_item(self, ligne, colonne, valeur):
        if (ligne == 1):
            self.mat[ligne].set_item(colonne, valeur)
        if (ligne == 2):
            self.mat[ligne].set_item(colonne, valeur)
        if (ligne == 3):
            self.mat[ligne].set_item(colonne, valeur)
        if (ligne == 4):
            self.mat[ligne].set_item(colonne, valeur)

    def get_item(self, ligne, colonne):
        if (ligne == 1):
            return self.mat[0].get_item(colonne)
        if (ligne == 2):
            return self.mat[1].get_item(colonne)
        if (ligne == 3):
            return self.mat[2].get_item(colonne)
        if (ligne == 4):
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


def trans_x(X):
    return Mat4D(Vect4D(1, 0, 0, X), Vect4D(0, 1, 0, 0), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))


def trans_y(Y):
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, 1, 0, Y), Vect4D(0, 0, 1, 0), Vect4D(0, 0, 0, 1))


def trans_z(Z):
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, 1, 0, 0), Vect4D(0, 0, 1, Z), Vect4D(0, 0, 0, 1))


def rot_x(teta):
    return Mat4D(Vect4D(1, 0, 0, 0), Vect4D(0, cos(teta), sin(teta), 0), Vect4D(0, -sin(teta), cos(teta), 0),
                 Vect4D(0, 0, 0, 1))


def rot_y(teta):
    return Mat4D(Vect4D(cos(teta), 0, sin(teta), 0), Vect4D(0, 1, 0, 0), Vect4D(-sin(teta), 0, cos(teta), 0),
                 Vect4D(0, 0, 0, 1))


def rot_z(teta):
    return Mat4D(Vect4D(cos(teta), sin(teta), 0, 0), Vect4D(-sin(teta), cos(teta), 0, 0), Vect4D(0, 0, 1, 0),
                 Vect4D(0, 0, 0, 1))


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
    mat_temp = mat_temp * rot_z(teta3)
    mat_temp = mat_temp * rot_z(teta4)
    mat_trans = mat_temp * trans_x(l)
    vector_p = mat_trans * Vect4D(x, y, z, t)

    lblResultText = Label(window, text='The result is :', bg=param_background, highlightbackground=param_background)
    lblResultValue = Label(window, text=vector_p, bg=param_background, highlightbackground=param_background)
    lblResultText.grid(column=6, row=param_row_line_5, sticky="e")
    lblResultValue.grid(column=7, row=param_row_line_5, sticky="w")


def main():
    # Create tkinter window with properties
    window = Tk()
    window.title("Python TP6")
    window.geometry('1080x500')
    window.minsize(500, 400)
    window.configure(bg=param_background) 
    
    # Make window responsive
    for i in range(0, 20):
        window.rowconfigure(index=i, weight=1)
        window.columnconfigure(index=i, weight=1)
    
    # Set default values
    defaultValue = 0
    defaultValueTeta1 = IntVar(); defaultValueTeta1.set(defaultValue)
    defaultValueTeta2 = IntVar(); defaultValueTeta2.set(defaultValue)
    defaultValueTeta3 = IntVar(); defaultValueTeta3.set(defaultValue)
    defaultValueTeta4 = IntVar(); defaultValueTeta4.set(defaultValue)
    defaultValueL = IntVar(); defaultValueL.set(defaultValue)
    defaultValueX = IntVar(); defaultValueX.set(defaultValue)
    defaultValueY = IntVar(); defaultValueY.set(defaultValue)
    defaultValueZ = IntVar(); defaultValueZ.set(defaultValue)
    
    # Initialize Label
    lblTeta1 = Label(window, text='θ1', bg=param_background, highlightbackground=param_background)
    lblTeta2 = Label(window, text='θ2', bg=param_background, highlightbackground=param_background)
    lblTeta3 = Label(window, text='θ3', bg=param_background, highlightbackground=param_background)
    lblTeta4 = Label(window, text='θ4', bg=param_background, highlightbackground=param_background)
    lblL = Label(window, text='L', bg=param_background, highlightbackground=param_background)
    lblX = Label(window, text='X', bg=param_background, highlightbackground=param_background)
    lblY = Label(window, text='Y', bg=param_background, highlightbackground=param_background)
    lblZ = Label(window, text='Z', bg=param_background, highlightbackground=param_background)

    # Initialize Spinbox
    teta1 = Spinbox(window, from_=param_from, to=param_to, width=param_width, justify=param_justify,
                    textvariable=defaultValueTeta1, bg=param_background, highlightbackground=param_background)
    teta2 = Spinbox(window, from_=param_from, to=param_to, width=param_width, justify=param_justify,
                    textvariable=defaultValueTeta2, bg=param_background, highlightbackground=param_background)
    teta3 = Spinbox(window, from_=param_from, to=param_to, width=param_width, justify=param_justify,
                    textvariable=defaultValueTeta3, bg=param_background, highlightbackground=param_background)
    teta4 = Spinbox(window, from_=param_from, to=param_to, width=param_width, justify=param_justify,
                    textvariable=defaultValueTeta4, bg=param_background, highlightbackground=param_background)
    l = Spinbox(window, from_=param_from, to=param_to, width=param_width, justify=param_justify,
                textvariable=defaultValueL, bg=param_background, highlightbackground=param_background)
    x = Spinbox(window, from_=param_from, to=param_to, width=param_width, justify=param_justify,
                textvariable=defaultValueX, bg=param_background, highlightbackground=param_background)
    y = Spinbox(window, from_=param_from, to=param_to, width=param_width, justify=param_justify,
                textvariable=defaultValueY, bg=param_background, highlightbackground=param_background)
    z = Spinbox(window, from_=param_from, to=param_to, width=param_width, justify=param_justify,
                textvariable=defaultValueZ, bg=param_background, highlightbackground=param_background)

    # Initialize Button
    btnCalculate = Button(window, text='Calculate', justify=param_justify, highlightbackground=param_background,
                          bg=param_background, command=lambda: calculate(window, teta1.get(), teta2.get(), teta3.get(),
                                                                         teta4.get(), l.get(), x.get(), y.get(),
                                                                         z.get()))
    btnQuit = Button(window, text='Quit', justify=param_justify, command=window.destroy, bg=param_background,
                     highlightbackground=param_background)

    # Place all widgets in the window
    lblTeta1.grid(column=4, row=param_row_line_1, sticky="e"); teta1.grid(column=5, row=param_row_line_1, sticky="w")
    lblTeta2.grid(column=6, row=param_row_line_1, sticky="e"); teta2.grid(column=7, row=param_row_line_1, sticky="w")
    lblTeta3.grid(column=8, row=param_row_line_1, sticky="e"); teta3.grid(column=9, row=param_row_line_1, sticky="w")
    lblTeta4.grid(column=10, row=param_row_line_1, sticky="e"); teta4.grid(column=11, row=param_row_line_1, sticky="w")
    
    lblL.grid(column=7, row=param_row_line_2, sticky="e"); l.grid(column=8, row=param_row_line_2, sticky="w")
    
    lblX.grid(column=5, row=param_row_line_3, sticky="e"); x.grid(column=6, row=param_row_line_3, sticky="w")
    lblY.grid(column=7, row=param_row_line_3, sticky="e"); y.grid(column=8, row=param_row_line_3, sticky="w")
    lblZ.grid(column=9, row=param_row_line_3, sticky="e"); z.grid(column=10, row=param_row_line_3, sticky="w")
    
    btnCalculate.grid(column=8, row=param_row_line_4, sticky="ew")
    
    btnQuit.grid(column=18, row=param_row_line_6, sticky="ew")
    
    window.mainloop()


main()
