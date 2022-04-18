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

x0 = 110 
y0 = 100
x1 = 160 
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
            canvas.create_rectangle((x0 + l*50, y0), (x1 + l*50, y1), fill = "saddlebrown")
            canvas.create_oval((x0 + l*50, y0), (x1 + l*50, y1), fill = "peru")
        y0 = y1 
        y1 = y1 + 50    

def quadrillage2() : 
    """fonction qui crée les ronds où l'utilisateur cliquera pour choisir la couleur de ses pions"""   
    for i in range (8) : 
        a = couleurs_Gpion[i]
        canvas.create_rectangle((10 + (i*50), 20), (60 + (i*50), 70), fill = "saddlebrown")
        canvas.create_oval((10 + (i*50), 20), (60 + (i*50), 70), fill = a)



# création des widgets 
racine = tk.Tk()
canvas = tk.Canvas(racine, height= HAUTEUR, width= LARGEUR, bg="grey")
bouton_sauv = tk.Button(racine, text="Sauvegarder partie")
bouton_load = tk.Button(racine, text="charger partie")
bouton_triche = tk.Button(racine, text="revenir en arrière")
bouton_aide = tk.Button(racine, text="aide")

liste = []
quadrillage()
quadrillage2()

# placement des widgets 
canvas.grid(column=0, row=0, columnspan=3, rowspan=4)
bouton_sauv.grid(column=3, row=2)
bouton_load.grid(column=3, row=3)
bouton_triche.grid(column=3, row = 0)
bouton_aide.grid(column=3, row=1)

# boucle principale 
canvas.mainloop()