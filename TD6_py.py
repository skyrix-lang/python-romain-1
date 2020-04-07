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
            
        def affichage(self):
            #print("x:",self.X, "y:", self.Y, "z:", self.Z, "t:", self.T)
            return str(self.X) + " " + str(self.Y) + " " + str(self.Z) + " " + str(self.T)
            
        def module(self):
            mod = sqrt(self.X**2 + self.Y**2 + self.Z**2 + self.T**2)
            return mod
            
        def addition(self, var):
            return(
            self.X + var.X,
            self.Y + var.Y,
            self.Z + var.Z,
            self.T + var.T)
            
        def soustraction(self, var):
            return(
            self.X - var.X,
            self.Y - var.Y,
            self.Z - var.Z,
            self.T - var.T)
    
        def egal(self, var):
            if(var is Vect4D):
                if(self.X == var.X and self.Y == var.Y and self.Z == var.Z and self.T == var.T):
                    return True
                else:
                    return False
                
        def multiplication_scalaire(self, var):
            self.X = var.X * self.X
            self.Y = var.Y * self.Y
            self.Z = var.Z * self.Z
            self.T = var.T * self.T
                
        def multiplication_par_un_scalaire(self, var):
            self.X = var * self.X
            self.Y = var * self.Y
            self.Z = var * self.Z
            self.T = var * self.T
            
        def to_list(self):
            return [self.X, self.Y, self.Z, self.T]
        
        def __setitem__(self, clé, valeur):
            if((clé == 'X') or (clé == 1)):
                self.X = valeur
            if((clé == 'Y') or (clé == 2)):
                self.Y = valeur
            if((clé == 'Z') or (clé == 3)):
                self.Z = valeur
            if((clé == 'T') or (clé == 4)):
                self.T = valeur
                
        def __getitem__(self, clé):
            if((clé == 'X') or (clé == 1)):
                return self.X
            if((clé == 'Y') or (clé == 2)):
                return self.Y
            if((clé == 'Z') or (clé == 3)):
                return self.Z
            if((clé == 'T') or (clé == 4)):
                return self.T   
            
class Mat4D:
        def __init__(self, V1, V2, V3, V4):
            if (isinstance(V1,Vect4D) and isinstance(V2,Vect4D) and isinstance(V3,Vect4D) and isinstance(V4,Vect4D)):
                self.mat = [V1, V2, V3, V4]
            else:
                print("Une ou plusieurs valeurs ne sont pas des vecteurs")
        
        def affichage_2(self):
            myMat = []
            for vect in self.mat:
                myMat.append([vect.__getitem_2__(valVect) for valVect in range(1, 5)])
            result = "\n".join(str(i) for i in myMat )
            return result
        
        def addition_2(self, matrice):
            return(self.mat + matrice)
            
        def soustraction_2(self, matrice):
            return(self.mat - matrice)
        
        def __setitem_2__(self, ligne, colonne, valeur):
            if(ligne == 1):
                self.mat[ligne].__setitem__(colonne, valeur)
            if(ligne == 2):
                self.mat[ligne].__setitem__(colonne, valeur)
            if(ligne == 3):
                self.mat[ligne].__setitem__(colonne, valeur)
            if(ligne == 4):
                self.mat[ligne].__setitem__(colonne, valeur)
                
        def __getitem_2__(self, ligne, colonne):
            if(ligne == 1):
                return self.mat[0].__getitem__(colonne)
            if(ligne == 2):
                return self.mat[1].__getitem__(colonne)
            if(ligne == 3):
                return self.mat[2].__getitem__(colonne)
            if(ligne == 4):
                return self.mat[3].__getitem__(colonne)
        
        def egal_2(self, matrice):
            if(matrice is mat4D):
                if(self.mat.equals(matrice) == True):
                    return True
                else:
                    return False
                
        def multiplication_par_un_scalaire_2(self, variable):
            return Mat4D(
                Vect4D(self.mat[0].X * variable, self.mat[0].Y * variable, self.mat[0].Z * variable, self.mat[0].T * variable),
                Vect4D(self.mat[1].X * variable, self.mat[1].Y * variable, self.mat[1].Z * variable, self.mat[1].T * variable),
                Vect4D(self.mat[2].X * variable, self.mat[2].Y * variable, self.mat[2].Z * variable, self.mat[2].T * variable),
                Vect4D(self.mat[3].X * variable, self.mat[3].Y * variable, self.mat[3].Z * variable, self.mat[3].T * variable),
            )
            
        def multiplication_matrice_2(self, matrice_ou_vecteur):
            if (isinstance(matrice_ou_vecteur, Mat4D) or isinstance(matrice_ou_vecteur, Vect4D)):
                res = dot(self.to_list(), matrice_ou_vecteur.to_list())
                return Mat4D(
                    Vect4D(res[0][0], res[0][1], res[0][2], res[0][3]),
                    Vect4D(res[1][0], res[1][1], res[1][2], res[1][3]),
                    Vect4D(res[2][0], res[2][1], res[2][2], res[2][3]),
                    Vect4D(res[3][0], res[3][1], res[3][2], res[3][3]),
                )
            else:
                raise Exception("%s n'est une matrice ni un vecteur %s" % (matrice_ou_vecteur, isinstance(matrice_ou_vecteur, Mat4D)))
        
        def to_list(self):
            return [self.mat[0].to_list(), self.mat[1].to_list(), self.mat[2].to_list(), self.mat[3].to_list()]
        
        
def Id4D():
    matrice_identité = Mat4D(Vect4D(1,0,0,0), Vect4D(0,1,0,0), Vect4D(0,0,1,0), Vect4D(0,0,0,1))
    return matrice_identité

def SymX():
    matrice_SymX = Mat4D(Vect4D(-1,0,0,0), Vect4D(0,1,0,0), Vect4D(0,0,1,0), Vect4D(0,0,0,1))
    return matrice_SymX
        
def SymY():
    matrice_SymY = Mat4D(Vect4D(1,0,0,0), Vect4D(0,-1,0,0), Vect4D(0,0,1,0), Vect4D(0,0,0,1))
    return matrice_SymY
            
def SymZ():
    matrice_SymZ = Mat4D(Vect4D(1,0,0,0), Vect4D(0,1,0,0), Vect4D(0,0,-1,0), Vect4D(0,0,0,1))
    return matrice_SymZ

def TransX(X):
    matrice_TransX = Mat4D(Vect4D(1,0,0,X), Vect4D(0,1,0,0), Vect4D(0,0,1,0), Vect4D(0,0,0,1))
    return matrice_TransX
    #x1 = [1,0,0,a]
    #x2 = [0,1,0,0]
    #x3 = [0,0,1,0]
    #x4 = [0,0,0,1]
    #return Mat4D(x1,x2,x3,x4)
    
def TransY(Y):
    matrice_TransY = Mat4D(Vect4D(1,0,0,0), Vect4D(0,1,0,Y), Vect4D(0,0,1,0), Vect4D(0,0,0,1))
    return matrice_TransY
    #y1 = [1,0,0,0]
    #y2 = [0,1,0,a]
    #y3 = [0,0,1,0]
    #y4 = [0,0,0,1]
    #return Mat4D(y1,y2,y3,y4)
    
def TransZ(Z):
    matrice_TransZ = Mat4D(Vect4D(1,0,0,0), Vect4D(0,1,0,0), Vect4D(0,0,1,Z), Vect4D(0,0,0,1))
    return matrice_TransZ
    #z1 = [1,0,0,0]
    #z2 = [0,1,0,0]
    #z3 = [0,0,1,a]
    #z4 = [0,0,0,1]
    #return Mat4D(z1,z2,z3,z4)
    
def RotX(thêta):
    matrice_RotX = Mat4D(Vect4D(1,0,0,0), Vect4D(0,cos(thêta),sin(thêta),0), Vect4D(0,-sin(thêta),cos(thêta),0), Vect4D(0,0,0,1))
    return matrice_RotX
        
def RotY(thêta):
    matrice_RotY = Mat4D(Vect4D(cos(thêta),0,sin(thêta),0), Vect4D(0,1,0,0), Vect4D(-sin(thêta),0,cos(thêta),0), Vect4D(0,0,0,1))
    return matrice_RotY
        
def RotZ(thêta):
    matrice_RotZ = Mat4D(Vect4D(cos(thêta),sin(thêta),0,0), Vect4D(-sin(thêta),cos(thêta),0,0), Vect4D(0,0,1,0), Vect4D(0,0,0,1))
    return matrice_RotZ





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

def Calcul_Final(Resultat_Final):
    θ1 = float(Entrée_θ1.get())
    θ2 = float(Entrée_θ2.get())
    θ3 = float(Entrée_θ3.get())
    θ4 = float(Entrée_θ4.get())
    L = float(Entrée_L.get())
    X = float(Entrée_X.get())
    Y = float(Entrée_Y.get())
    Z = float(Entrée_Z.get())
    T = 1
    Matrice_Temporaire_1 = RotX(θ1).multiplication_matrice_2(RotY(θ2))
    Matrice_Temporaire_2 = Matrice_Temporaire_1.multiplication_matrice_2(RotZ(θ3))
    Matrice_Temporaire_3 = Matrice_Temporaire_2.multiplication_matrice_2(RotZ(θ4))
    Matrice_Transformation = Matrice_Temporaire_3.multiplication_matrice_2(TransX(L))
    X_prime = Matrice_Transformation.multiplication_par_un_scalaire_2(X)
    Y_prime = Matrice_Transformation.multiplication_par_un_scalaire_2(Y)
    Z_prime = Matrice_Transformation.multiplication_par_un_scalaire_2(Z)
    Resultat_Final.config(text='('+str(X_prime)+','+str(Y_prime)+','+str(Z_prime)+','+str(T)+')')
    print(Resultat_Final)
    print('Raoult')

    

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

