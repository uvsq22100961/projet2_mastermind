####################################################################
# URL du projet : https://github.com/uvsq22100961/projet2_mastermind
# Projet Mastermind MITD2 groupe 4 
# Thibault ROYERE
# Camille ROESLER
# Manira MAHAMAT HAGGAR


##########################
# import des bibliothèques 

import tkinter as tk
import random as rd
import copy


#########################
# variables 

x0 = 110 
y0 = 100
x1 = 160 
y1 =  150

nombre_max_d_essais = 10
# liste avec les couleurs des pions :
liste = [[0]*4 for i in range(nombre_max_d_essais)]
liste2 = 0
liste_sauvegarde = []
liste_ppions = [[0] for i in range(nombre_max_d_essais)]

# Indicateur qui indique à quel essai on est:
Essai = 1

# Indicateur qui indique à quel colonne on est:
colonne = 0

# Compteur qui indique le nombre de pions dans le code secret:
codesecret= 0

# Indicateur du mode de jeu (mode 1 joueur ou mode 2 joueurs):
modesolo = 0

# Liste qui va contenir le code secret:
code = []

# Dimensions du canvas:
LARGEUR = 800
HAUTEUR = 700

# indicateur qui indique si on est en train de relancer une partie quand on est dans la fonction commencerpartie
relancer = False

# Variables globales :

couleurs_Gpion = ["green", "red", "yellow", "blue", "white", "pink", "orange", "purple"]
couleur_Ppion = ["yellow", "red"]
couleur = "black"


######################
# Fonctions:


def commencerpartie():
    """fonction qui commence la partie"""
    global liste
    global nombre_max_d_essais
    global relancer
    if relancer == True:
        for i in range(nombre_max_d_essais):
            for j in range(4):
                if liste[i][j] != 0:
                    objet = canvas.find_closest(135 + (j*50), 125 + (i*50))
                    canvas.delete(objet[0])
        liste = [[0]*4 for i in range(nombre_max_d_essais)]
        for i in range(nombre_max_d_essais):
            for j in range(liste_ppions[i][0]):
                objet = canvas.find_closest(375, 132 + (i*50))
                canvas.delete(objet[0])
    # Text d'explication
    label1.config(text="Veuillez choisir un mode de jeux")
    bouton_load.config(text ="Arreter la partie")
    # Boutons des deux modes :
    bouton_mode1.config(text="Mode 1 joueur", command= mode1joueur)
    bouton_mode2.config(text="Mode 2 joueurs", command= mode2joueurs)


def mode1joueur():
    """fonction qui demarre le mode 1 joueur"""
    global modesolo
    modesolo = 1 # lorsque le mode 1 joueur est vraie
    label1.config(text="Veuillez choisir une combinaison de pions")
    choix_code1() # on appelle la fonction qui choisit un code au hasard
    # clic sur une couleur :
    canvas.bind('<Button-1>', choisir_couleur)

def mode2joueurs():
    """fonction qui demarre le mode 2 joueurs"""
    global modesolo
    modesolo = 0 # le mode 1 joueur n'est pas vraie
    label1.config(text="Veuillez choisir une combinaison de pions secret a l'abris des regards")
    # clic sur une couleur :
    canvas.bind('<Button-1>', choisir_couleur)
    

def choix_code1():
    """fonction qui permet à l'ordinateur de choisir le code en mode 1 joueur """
    global couleur_Gpion
    global code
    for i in range(4): #on ajoute 4 couleurs à la liste 'code'
        c = rd.choice(couleurs_Gpion)
        code.append(c)
    print(code) # Un code est choisi

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
    y0, y1 = 100, 150

def quadrillage2() : 
    """fonction qui crée les ronds où l'utilisateur cliquera pour choisir la couleur de ses pions"""   
    for i in range (8) : 
        a = couleurs_Gpion[i]
        canvas.create_rectangle((10 + (i*50), 20), (60 + (i*50), 70), fill = "saddlebrown")
        canvas.create_oval((10 + (i*50), 20), (60 + (i*50), 70), fill = a)


def quadrillage3() : 
    """fonction qui crée le quadrillage où seront placés les pions secrets en mode 2 joueurs"""   
    for i in range (4) : 
        canvas.create_rectangle((500 + (i*50), 20), (550 + (i*50), 70), fill = "saddlebrown")
        canvas.create_oval((500 + (i*50), 20), (550 + (i*50), 70), fill = "peru")


def choisir_couleur(event):
    """fonction qui permet de cliquer sur une couleur qui est ensuite enregistrée"""
    global couleur
    x = event.x
    y = event.y
    if (y > 20 and y < 70):
        if (x > 10 and x < 60):
            couleur = "green"
        elif (x > 60 and x < 110):
            couleur = "red"
        elif (x > 110 and x < 160):
            couleur = "yellow"
        elif (x > 160 and x < 210):
            couleur = "blue"
        elif (x > 210 and x < 260):
            couleur = "white"
        elif (x > 260 and x < 310):
            couleur = "pink"
        elif (x > 310 and x < 360):
            couleur = "orange"
        elif (x > 360 and x < 410):
            couleur = "purple"
        couleur_utilisee.configure(text=couleur, fg=couleur)
        mode()


def mode():
    """fonctions qui nous permet de placer les pions selon le mode de jeux"""
    # En fonction du mode, les pions sont posés dans le code secret ou sur le jeu :
    if modesolo == 1: 
        GrandsPions()
    if modesolo == 0:
        GrandsPions2()


def GrandsPions2():
    """fonction qui place les pions secret dans le mode de jeu 2 joueurs """
    global code
    global codesecret
    if codesecret < 4:
        canvas.create_oval((500 + (codesecret*50), 20), (550 + (codesecret*50), 70), fill = couleur)
        code.append(couleur)
        print(code)
        codesecret += 1
        if codesecret == 4:
            label1.config(text="Qliquez sur une couleur pour cacher le code")
    elif codesecret == 4:
        codesecret += 1
        for i in range(4): # Pour chaque cercle, on prend leur identifiant, et modifie leur couleur :
                objet = canvas.find_closest(525 + (i*50), 45)
                canvas.itemconfigure(objet, fill="black")
        label1.config(text="Veuillez choisir une combinaison de pions")
    else: # Quand on a fini de composé le code, les grands pions sont posés sur le jeu
        modesolo = 1
        GrandsPions()


def GrandsPions():
    """fonction qui pose les grands pions de la couleur choisie sur le jeu"""
    global colonne
    global Essai
    global nombre_max_d_essais
    global relancer
    if relancer == False:
        relancer = True
    if Essai <= nombre_max_d_essais:
        if colonne < 4 :
            canvas.create_oval((x0 + colonne*50 , y0 + 50*(Essai - 1)), (x1 + colonne*50, y1 + 50*(Essai - 1)), fill = couleur)
            liste[Essai - 1][colonne] = couleur
            colonne += 1
    if colonne == 4:
        if liste[Essai - 1] == code:
            couleur_utilisee.configure(text="VICTOIRE", fg="green")
            return
        PetitsPions()
        # On réinitialise colonne pour les essais suivants :
        colonne = 0


def PetitsPions():
    """fonction qui pose automatiquement les petits pions blancs et rouges en fonction de l'essai"""
    global liste2
    global liste_ppions
    global Essai
    nombre = 0
    nombre2 = 0
    # on utilise une deuxième liste pour les pions blancs :
    liste2 = list(code)
    for i in range(4):
        if liste[Essai - 1][i] == code[i]:
            canvas.create_oval((320 + nombre*20, y0 + 50*(Essai - 1)), (335 + nombre*20, y0 + 50*(Essai - 1) + 15), fill="red")
            nombre += 1
            # s'il y a une couleur déjà utilisé on l'enlève de liste2 :
            liste2[i] = 0
            # on ajoute 1 à la liste ppion quand on ajoute des petits pions :
            liste_ppions[Essai - 1][0] += 1
    for i in range(4):
        # si la couleur liste[essai-1][i] est dans le code, mais pas à la bonne place, et que cette couleur dans le code
        # n'est pas déjà utilisée pour les pions rouges (cad qu'elle est dans liste2)... :
        if (liste[Essai - 1][i] in liste2) and (liste[Essai - 1][i] != code[i]):
            # ...on met un pion blanc
            canvas.create_oval((320 + nombre2*20, y0 + 25 + 50*(Essai - 1)), (335 + nombre2*20, y0 + 40 + 50*(Essai - 1))
            , fill="white")
            nombre2 += 1
            liste_ppions[Essai - 1][0] += 1
            # s'il y a une couleur déjà utilisé on l'enlève de liste2 :
            for j in range(4):
                if liste2[j] == liste[Essai - 1][i]:
                    liste2[j] = 0
    # On ajoute 1 à Essai pour dire qu'on passe à l'eessai suivant
    if Essai == 10:
        couleur_utilisee.configure(text="GAME OVER", fg="black")
    Essai += 1
    #canvas.bind('<Button-1>', choisir_couleur)


def sauvegarde():
    """fonction qui sauvegarde la partie"""
    global liste_sauvegarde
    liste_sauvegarde = copy.deepcopy(liste) # permet de copier 'en profondeur' la liste
    print(liste_ppions)



# Création des widgets :
racine = tk.Tk()
canvas = tk.Canvas(racine, height= HAUTEUR, width= LARGEUR, bg="grey")
Titre = racine.title("Mastermind")
bouton_sauv = tk.Button(racine, text="Sauvegarder partie", command=sauvegarde)
bouton_load = tk.Button(racine, text="Commencer une nouvelle partie", command= commencerpartie)
bouton_triche = tk.Button(racine, text="revenir en arrière")
bouton_aide = tk.Button(racine, text="aide")
bouton_mode1 = tk.Button(racine)
bouton_mode2 = tk.Button(racine)

# Surface de textes :
label1 = tk.Label(racine, text="Regles du jeu : .....", font=("helvetica", "10"), bg="grey")

# Indicateur de la couleur actuelle utilisée :
couleur_utilisee = tk.Label(racine, text="aucune", font=("helvetica", "15"), fg=couleur, bg="grey")


quadrillage()
quadrillage2()
quadrillage3()





# Placement des widgets :
canvas.grid(column=0, row=0, columnspan=3, rowspan=5)
bouton_sauv.grid(column=3, row=2)
bouton_load.grid(column=3, row=3)
bouton_triche.grid(column=3, row = 0)
bouton_aide.grid(column=3, row=1)
couleur_utilisee.grid(column=5, row=4)
bouton_mode1.grid(column=4, row=4)
bouton_mode2.grid(column=3, row=4)
label1.grid(column=2, row=3)

# Boucle principale :
canvas.mainloop()



## nouvelles choses :
# -fonction choisir_couleur
# -Label couleur_utilisee
# -Modification de la fonction GrandsPions
# -fonction PetitsPions
# -Modification des fonction, ce qui permet de jouer normalement
# - Mode 2 joueurs et les boutons partiellement
# -on ne peut plus mettre des couleurs sur le jeu tant que le mode n'est pas choisi (T)
# -Cacher le code secret dans le mode 2 joueurs (T)
# -début bouton arreter (T)
# début du fichier readme (je le fait dans la journée)

## choses à faire:
# -Corriger le mode 2 joeurs:
#   - régler probleme avec bouton arreter (en soit il fonctionne, mais il faut cliquer 1 seule fois dessus) C
#-faire fontionner les boutons Arreter, sauvegarder ,aide et revenir en arriere
# (pour sauvegarder : créer une copie de la liste contenant toutes les couleurs)

# REMARQUES :
#   -les essais sont les lignes et pas le nombre de grands pions que l'on peut mettre par ligne, 
# il y a 10 essais de bases


## choses pour améliorer à la fin: