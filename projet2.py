# Projet Mastermind
# Thibault ROYERE
# Camille ROESLER
# Manira MAHAMAT HAGGAR

############################

# BIBLIOTHEQUE
import tkinter as tk
import random as rd

# VARIABLES
couleurs_Gpion = ["green", "red", "yellow", "blue", "white", "pink", "orange", "purple"]
couleur_Ppion = ["yellow", "red"]
code = []
LARGEUR = 500
HAUTEUR = 800

# FONCTION

def choix_code1():
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

#
racine = tk.Tk()
canvas = tk.Canvas(racine, height= HAUTEUR, width= LARGEUR)
canvas.grid()
liste = []
quadrillage()

#
canvas.mainloop()