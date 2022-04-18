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

code = []
LARGEUR = 500
HAUTEUR = 800

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


def quadrillage():
    """fonction qui crée le quadrillage"""
    for ligne in range(11):
        for colonne in range(3):
            canvas.create_line((50, 70 + ligne * HAUTEUR//12), (LARGEUR - 50, 70 + ligne * HAUTEUR//12))
            canvas.create_line((50 + ligne * HAUTEUR//12,70),(50 + ligne * HAUTEUR//12, HAUTEUR - 50))


# création des widgets 
racine = tk.Tk()
canvas = tk.Canvas(racine, height= HAUTEUR, width= LARGEUR)

liste = []
quadrillage()

# placement des widgets 
canvas.grid()

# boucle principale 
canvas.mainloop()