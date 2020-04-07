# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 09:16:57 2020

@author: romai
"""

from math import *
from tkinter import *
from numpy import dot

class Vect4D:

        def __init__(self, x, y, z, t):
            self.X = x
            self.Y = y
            self.Z = z
            self.T = t


        def __str__(self):
            return "(" + str(self.X) + " " + str(self.Y) + " " + str(self.Z) + " " + str(self.T) + ")"


        def __add__(self, var):
            return(
            self.X + var.X,
            self.Y + var.Y,
            self.Z + var.Z,
            self.T + var.T)


        def __sub__(self, var):
            return(
            self.X - var.X,
            self.Y - var.Y,
            self.Z - var.Z,
            self.T - var.T)


        def __mul__(self, var):
            if (isinstance(mat, float) or isinstance(mat, int)):
                return(
                self.X = float(var) * self.X
                self.Y = float(var) * self.Y
                self.Z = float(var) * self.Z
                self.T = float(var) * self.T)

            elif(isinstance(mat, Vect4D)):
                return(
                var.X * self.X +
                var.Y * self.Y +
                var.Z * self.Z +
                var.T * self.T)
            else:
                raise Exception("Error: Invalid value (only float or vector)")


        def __eq__(self, var):
            if(var is Vect4D):
                if(self.X == var.X and self.Y == var.Y and self.Z == var.Z and self.T == var.T):
                    return True
                else:
                    return False


        def setItem(self, clé, valeur):
            if((clé == 'X') or (clé == 1)):
                self.X = valeur
            if((clé == 'Y') or (clé == 2)):
                self.Y = valeur
            if((clé == 'Z') or (clé == 3)):
                self.Z = valeur
            if((clé == 'T') or (clé == 4)):
                self.T = valeur


        def getItem(self, clé):
            if((clé == 'X') or (clé == 1)):
                return self.X
            if((clé == 'Y') or (clé == 2)):
                return self.Y
            if((clé == 'Z') or (clé == 3)):
                return self.Z
            if((clé == 'T') or (clé == 4)):
                return self.T


        def to_list(self):
            return [self.X, self.Y, self.Z, self.T]


        def module(self):
            mod = sqrt(self.X**2 + self.Y**2 + self.Z**2 + self.T**2)
            return mod






class Mat4D:

        def __init__(self, V1, V2, V3, V4):
            if (isinstance(V1,Vect4D) and isinstance(V2,Vect4D) and isinstance(V3,Vect4D) and isinstance(V4,Vect4D)):
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
            return(self.mat + matrice)


        def __sub__(self, matrice):
            return(self.mat - matrice)


        def __mul__(self, mat):
            if (isinstance(mat, int) or isinstance(mat, float)):
                vec = Vect4D(0,0,0,0)
                result= Mat4D(vec,vec,vec,vec)
                for i in range(1,5)
                    for j in range(1,5)
                        for k in range(1,5)
                            result.setItem(i,j,self.getItem(i,j)*float(mat))
                return result

            elif (isinstance(mat, Vect4D)):
                vec = Vect4D(0,0,0,0)
                result= Mat4D(vec,vec,vec,vec)
                temp =0
                for i in range(1,5)
                    for j in range(1,5)
                        for k in range(1,5)
                            temp += self.getItem(j,k)*mat.getItem(i)
                    result.setItem(i,j,temp)
                    temp=0
                return result

            elif (isinstance(mat, Mat4D)):
                vec = Vect4D(0,0,0,0)
                result= Mat4D(vec,vec,vec,vec)
                temp=0
                for i in range(1,5)
                    for j in range(1,5)
                        for k in range(1,5)
                            temp+=self.getItem(i,k)*mat.getItem(k,j))
                    result.setItem(i,j,temp)
                    temp=0
                return result
            else:
                raise Exception("Error: Invalid value (only float or vector or matrix 4D)")


        def __eq__(self, matrice):
            if(matrice is mat4D):
                if(self.mat.equals(matrice) == True):
                    return True
                else:
                    return False


        def setItem(self, ligne, colonne, valeur):
            if(ligne == 1):
                self.mat[ligne].__setitem__(colonne, valeur)
            if(ligne == 2):
                self.mat[ligne].__setitem__(colonne, valeur)
            if(ligne == 3):
                self.mat[ligne].__setitem__(colonne, valeur)
            if(ligne == 4):
                self.mat[ligne].__setitem__(colonne, valeur)


        def getItem(self, ligne, colonne):
            if(ligne == 1):
                return self.mat[0].__getitem__(colonne)
            if(ligne == 2):
                return self.mat[1].__getitem__(colonne)
            if(ligne == 3):
                return self.mat[2].__getitem__(colonne)
            if(ligne == 4):
                return self.mat[3].__getitem__(colonne)


        def to_list(self):
            return [self.mat[0].to_list(), self.mat[1].to_list(), self.mat[2].to_list(), self.mat[3].to_list()]





def Id4D():
    return Mat4D(Vect4D(1,0,0,0), Vect4D(0,1,0,0), Vect4D(0,0,1,0), Vect4D(0,0,0,1))


def SymX():
    return Mat4D(Vect4D(-1,0,0,0), Vect4D(0,1,0,0), Vect4D(0,0,1,0), Vect4D(0,0,0,1))


def SymY():
    return Mat4D(Vect4D(1,0,0,0), Vect4D(0,-1,0,0), Vect4D(0,0,1,0), Vect4D(0,0,0,1))


def SymZ():
    return Mat4D(Vect4D(1,0,0,0), Vect4D(0,1,0,0), Vect4D(0,0,-1,0), Vect4D(0,0,0,1))


def TransX(X):
    return Mat4D(Vect4D(1,0,0,X), Vect4D(0,1,0,0), Vect4D(0,0,1,0), Vect4D(0,0,0,1))


def TransY(Y):
    return Mat4D(Vect4D(1,0,0,0), Vect4D(0,1,0,Y), Vect4D(0,0,1,0), Vect4D(0,0,0,1))


def TransZ(Z):
    return Mat4D(Vect4D(1,0,0,0), Vect4D(0,1,0,0), Vect4D(0,0,1,Z), Vect4D(0,0,0,1))


def RotX(teta):
    return Mat4D(Vect4D(1,0,0,0), Vect4D(0,cos(teta),sin(teta),0), Vect4D(0,-sin(teta),cos(teta),0), Vect4D(0,0,0,1))


def RotY(teta):
    return Mat4D(Vect4D(cos(teta),0,sin(teta),0), Vect4D(0,1,0,0), Vect4D(-sin(teta),0,cos(teta),0), Vect4D(0,0,0,1))


def RotZ(teta):
    returnMat4D(Vect4D(cos(teta),sin(teta),0,0), Vect4D(-sin(teta),cos(teta),0,0), Vect4D(0,0,1,0), Vect4D(0,0,0,1))


def Calc_Fin():
    teta1 = float(teta1.get())
    teta2 = float(teta2.get())
    teta3 = float(teta3.get())
    teta4 = float(teta4.get())
    L = float(L.get())
    X = float(X.get())
    Y = float(Y.get())
    Z = float(Z.get())
    T = 1
    mat_temp = RotX(teta1)*RotY(teta2)
    mat_temp = mat_temp*RotZ(teta3)
    mat_temp = mat*RotZ(teta4)
    mat_trans = mat_temp*TransX(L)
    vect_p = mat_trans*Vect4D(X,Y,Z,T)
    print(vect_p)



fenetre = Tk()    
    
fenetre.geometry("700x500") #Pour créer une fenêtre de taille 900x600
fenetre.minsize(700,500)
fenetre.maxsize(700,500)#Taille minimale

#Txt_theta_3 = Label(fenetre, text = "θ3")
#Txt_theta_4 = Label(fenetre, text = "θ4")
#Txt_theta_3.pack()
#Txt_theta_4.pack()

Label(fenetre).pack()
Label(fenetre).pack()

cadre_1 = Frame(fenetre, width = 80., height = 60, borderwidth = 1)
cadre_1.pack(fill=BOTH)


Label(cadre_1, text = "               ").pack(side="left")

Entrée_θ1 = StringVar() 
Entrée_θ1.set("0")
Txt_θ1 = Label(cadre_1, text = "θ1")
Txt_θ1.pack(side="left", fill=X)
Valeur_θ1 = Entry(cadre_1, textvariable = Entrée_θ1, width = 30)
Valeur_θ1.pack(side="left", fill=X)



Label(cadre_1, text = "               ").pack(side="right")

Entrée_θ2 = StringVar() 
Entrée_θ2.set("0")
Valeur_θ2 = Entry(cadre_1, textvariable = Entrée_θ2, width = 30)
Valeur_θ2.pack(side="right", fill=X)
Txt_θ2 = Label(cadre_1, text = "θ2")
Txt_θ2.pack(side="right", fill=X)


Label(cadre_1, text = "          ").pack(side="right")






cadre_2 = Frame(fenetre, width = 80., height = 60, borderwidth = 1)
cadre_2.pack(fill=BOTH)


Label(cadre_2, text = "               ").pack(side="left")

Entrée_θ3 = StringVar() 
Entrée_θ3.set("0")
Txt_θ3 = Label(cadre_2, text = "θ3")
Txt_θ3.pack(side="left", fill=X)
Valeur_θ3 = Entry(cadre_2, textvariable = Entrée_θ3, width = 30)
Valeur_θ3.pack(side="left", fill=X)


Label(cadre_2, text = "               ").pack(side="right")

Entrée_θ4 = StringVar() 
Entrée_θ4.set("0")
Valeur_θ4 = Entry(cadre_2, textvariable = Entrée_θ4, width = 30)
Valeur_θ4.pack(side="right", fill=X)
Txt_θ4 = Label(cadre_2, text = "θ4")
Txt_θ4.pack(side="right", fill=X)

Label(cadre_2, text = "          ").pack(side="right")


Label(fenetre).pack()

cadre_3 = Frame(fenetre, width = 80., height = 60, borderwidth = 1)
cadre_3.pack(fill=BOTH)



Label(cadre_3, text = "                          ").pack(side="left")
Label(cadre_3, text = "                          ").pack(side="left")
Label(cadre_3, text = "                          ").pack(side="left")


Entrée_L = StringVar() 
Entrée_L.set("0")
Txt_L = Label(cadre_3, text = "L").pack(side = "left")
Valeur_L = Entry(cadre_3, textvariable = Entrée_L, width = 30)
Valeur_L.pack(side="left")

Label(fenetre).pack()
Label(fenetre).pack()

cadre_4 = Frame(fenetre, width = 80., height = 60, borderwidth = 1)
cadre_4.pack(fill=BOTH)

Label(cadre_4, text = "        ").pack(side="left")

Entrée_X = StringVar() 
Entrée_X.set("0")
Txt_X = Label(cadre_4, text = "X").pack(side="left", fill=X)
Coord_X = Entry(cadre_4, textvariable = Entrée_X, width = 30)
Coord_X.pack(side="left", fill=X)

Label(cadre_4, text = "      ").pack(side="left")

Entrée_Y = StringVar() 
Entrée_Y.set("0")
Txt_Y = Label(cadre_4, text = "Y").pack(side="left", fill=X)
Coord_Y = Entry(cadre_4, textvariable = Entrée_Y, width = 30)
Coord_Y.pack(side="left", fill=X)

Label(cadre_4, text = "      ").pack(side="left")

Entrée_Z= StringVar() 
Entrée_Z.set("0")
Txt_Z = Label(cadre_4, text = "Z").pack(side="left", fill=X)
Coord_Z = Entry(cadre_4, textvariable = Entrée_Z, width = 30)
Coord_Z.pack(side="left", fill=X)

Label(fenetre).pack()





#value = StringVar() 
#value.set("texte par défaut")
#entree = Entry(fenetre, textvariable = value, width = 30)
#entree.pack()

cadre_5= Frame(fenetre, width = 80., height = 60, borderwidth = 1)
cadre_5.pack(fill=BOTH)

cadre_6= Frame(fenetre, width = 80., height = 60, borderwidth = 1)
cadre_6.pack(fill=BOTH)

cadre_7= Frame(fenetre, width = 80., height = 60, borderwidth = 1)
cadre_7.pack(fill=BOTH)

Resultat_Final = Label(cadre_7)
Resultat_Final.pack(side='left')

bouton_calculer = Button(cadre_5, text = " calculer", command = print('ta mere'), background = "grey", width = 15, relief = "raised")
bouton_calculer.pack()
#Calcul_Final(Resultat_Final)

Label(fenetre).pack()
Label(fenetre).pack()


Txt_coord_abs = Label(cadre_6, text = "Le vecteur en coordonnées absolu est : ")
Txt_coord_abs.pack(side = "left")



Label(fenetre).pack()
Label(fenetre).pack()
Label(fenetre).pack()

bouton_quitter = Button(fenetre, text = " Fermer", command = fenetre.quit, background = "red",foreground = "blue",cursor = "pirate", width = 15, relief = "raised")
bouton_quitter.pack()

fenetre.mainloop()
    
    
#if __name__=='__main__':

