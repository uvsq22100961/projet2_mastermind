####################################
# Projet Mastermind MITD2 groupe 4 
# Thibault ROYERE
# Camille ROESLER
# Manira MAHAMAT HAGGAR
####################################


# import des bibliothèques 

import tkinter as tk
import random as rd

# variables 

x0 = 70 
y0 = 100
x1 = 120 
y1 =  150

code = []
LARGEUR = 800
HAUTEUR = 700

# variables globales 

couleurs_Gpion = ["green", "red", "yellow", "blue", "white", "pink", "orange", "purple"]
couleur_Ppion = ["yellow", "red"]

###########
# fonctions

def choix_code1():
    """fonction qui permet à l'ordinateur de choisir le code en mode 1 joueur """
    global couleur_Gpion
    global code
    for i in range(4):
        c = rd.choice(couleurs_Gpion)
        code.append(c)


def quadrillage() : 
    """ fonction qui crée le quadrillage des essais"""
    global x0, y0
    global x1, y1 
    for i in range (10) :  
        for l in range (4) : 
            canvas.create_rectangle((x0 + l*50, y0), (x1 + l*50, y1))
        y0 = y1 
        y1 = y1 + 50       


# création des widgets 
racine = tk.Tk()
canvas = tk.Canvas(racine, height= HAUTEUR, width= LARGEUR, bg="grey")

liste = []
quadrillage()

# placement des widgets 
canvas.grid()

# boucle principale 
canvas.mainloop()