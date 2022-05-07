####################################################################
# URL du projet : https://github.com/uvsq22100961/projet2_mastermind
# Projet Mastermind MITD2 groupe 4 
# Thibault ROYERE
# Camille ROESLER
# Manira MAHAMAT HAGGAR


##########################
# Import des bibliothèques 

from re import X
import tkinter as tk
import random as rd
import copy
from tkinter.font import NORMAL
from tracemalloc import start
from turtle import left
from venv import create


#########################
# Variables 

x0 = 110 
y0 = 100
x1 = 160 
y1 =  150

nombre_max_d_essais = 10

# Liste avec les couleurs des pions :
liste = [[0]*4 for i in range(nombre_max_d_essais)]
liste2 = 0

# Variables de sauvegarde :
liste_sauvegarde = []
code_sauvegarde = []
Essai_sauvegarde = 0
colonne_sauvegarde = 0
liste_ppions_sauv = []
codesecret_sauvegarde = 0
mode_sauvegarde = 0
mode_sauvegarde2  = 0 # n'est pas modifiée dans la fonction "GrandPions2" --> utile dans la fonction "commencerpartie"

# liste pour l'aide : 
aide = []

liste_ppions = [[0] for i in range(nombre_max_d_essais)]

# Indicateur qui indique à quel essai on est:
Essai = 1

# Indicateur qui indique à quel colonne on est:
colonne = 0

# Compteur qui indique le nombre de pions dans le code secret:
codesecret= 0

# Indicateur du mode de jeu (mode 1 joueur ou mode 2 joueurs):
modesolo = 0
modesolo2 = 0

# Liste qui va contenir le code secret:
code = []

# Dimensions du canvas:
LARGEUR = 800
HAUTEUR = 700

# Indicateur qui indique si on est en train de relancer une partie quand on est dans la fonction commencerpartie (permet
# d'enlever tous les pions du jeu, et de tout réinitialiser)
relancer = False

# Indicateur qui indique si le jeu est arrêté (empêche de poser des pions) :
arrêt = False

# Indicateur qui indique si la partie à laquelle on joue est une partie sauvegardée :
sauvegarder = False

# Indicateur qui indique si, quand on a sauvegardé une partie, on a déjà chargé cette partie (utilisé dans
#  choisir_couleur):
partie_chargee = False

# Boutons
bouton_arrêt = 0 # bouton pour arrêter la partie en cours
bouton_relancer = 0 # bouton pour relancer une partie
bouton_charger = 0 # bouton pour charger une partie

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
    global bouton_arrêt
    global arrêt
    global codesecret
    global code
    global modesolo2
    global Essai
    global colonne
    global liste_ppions
    if relancer == True:
        bouton_relancer.destroy()
        # On enlève tous les Grands pions :
        for i in range(nombre_max_d_essais):
            for j in range(4):
                if liste[i][j] != 0:
                    objet = canvas.find_closest(135 + (j*50), 125 + (i*50))
                    canvas.delete(objet[0])
        # On réinitialise la liste :
        liste = [[0]*4 for i in range(nombre_max_d_essais)]
        # On enlève tous les Petits pions :
        for i in range(nombre_max_d_essais):
            for j in range(liste_ppions[i][0]):
                objet = canvas.find_closest(350, 120 + (i*50))
                canvas.delete(objet[0])
        # En mode 2 joueurs, on enlève les cercles du code secret s'il y en a :
        if modesolo2 == 0:
            for i in range(4): # Pour chaque cercle du code, on prend son identifiant, et on le supprime :
                if i < codesecret:
                    objet = canvas.find_closest(525 + (i*50), 45)
                    canvas.delete(objet[0])
        codesecret = 0 # on réinitialise le compteur pour recréer un code en mode 2 joueurs
        # On réinitialise le code :
        code = []
        # On réinitialise les indicateurs d'essais et de la colonne :
        Essai, colonne = 1, 0
        # On réinitialise liste_ppions :
        liste_ppions = [[0] for i in range(nombre_max_d_essais)]
    # Text d'explication
    label1.config(text="Veuillez choisir un mode de jeux")
    bouton_load.destroy()
    bouton_arrêt = tk.Button(racine, text="Arreter la partie", command=arreter_partie, state=tk.DISABLED, width = 25)
    bouton_arrêt.grid(column=3, row=3)
    # Boutons des deux modes :
    bouton_mode1.config(text="Mode 1 joueur", command= mode1joueur)
    bouton_mode2.config(text="Mode 2 joueurs", command= mode2joueurs)


def mode1joueur():
    """fonction qui demarre le mode 1 joueur"""
    global modesolo
    global modesolo2
    global relancer
    global arrêt
    bouton_arrêt.config(state=NORMAL)
    bouton_triche.config(state=NORMAL)
    if arrêt == True:
        arrêt = False
    modesolo = 1 # lorsque le mode 1 joueur est vraie
    modesolo2
    if relancer == False:
        relancer = True
    label1.config(text="Veuillez choisir une combinaison de pions")
    choix_code1() # on appelle la fonction qui choisit un code au hasard
    # clic sur une couleur :
    canvas.bind('<Button-1>', choisir_couleur)

def mode2joueurs():
    """fonction qui demarre le mode 2 joueurs"""
    global modesolo
    global relancer
    global arrêt
    bouton_arrêt.config(state=NORMAL)
    bouton_triche.config(state=NORMAL)
    if arrêt == True:
        arrêt = False
    modesolo = 0 # le mode 1 joueur n'est pas vraie
    modesolo2 = 0
    if relancer == False:
        relancer = True
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
        #Si il s'agit d'une partie en cours et non sauvegardée, alors on debute un mode de jeu
        if arrêt == False and (sauvegarder == False or partie_chargee == False) :
            mode()
        #Si il s'agit d'une partie sauvegardée, alors on continue avec le meme mode
        elif sauvegarder == True and arrêt == False:
            commencer_partie_sauvegardee()
            


def commencer_partie_sauvegardee():
    """fonctions qui nous permet de placer les pions selon le mode de jeux lorsqu'on debute une partie sauvegardée"""
    global colonne, Essai, code, liste_ppions, sauvegarder, codesecret, arrêt
    bouton_arrêt.config(state=NORMAL)
    bouton_triche.config(state=NORMAL)
    liste_ppions = liste_ppions_sauv.copy()
    liste = liste_sauvegarde.copy()
    if mode_sauvegarde == 1 :
        code = code_sauvegarde.copy()
        colonne = colonne_sauvegarde 
        Essai = Essai_sauvegarde
        GrandsPions()
    if mode_sauvegarde == 0 :
        codesecret = codesecret_sauvegarde
        GrandsPions2()   
    sauvegarder = False



def mode():
    """fonctions qui nous permet de placer les pions selon le mode de jeux"""
    # En fonction du mode, les pions sont posés dans le code secret ou sur le jeu :
    if modesolo == 1 : 
        GrandsPions()
    if modesolo == 0 :
        GrandsPions2()


def GrandsPions2():
    """fonction qui place les pions secret dans le mode de jeu 2 joueurs """
    global code
    global codesecret
    global modesolo
    if codesecret < 4:
        canvas.create_oval((500 + (codesecret*50), 20), (550 + (codesecret*50), 70), fill = couleur)
        code.append(couleur)
        print(code)
        codesecret += 1
        if codesecret == 4:
            label1.config(text="Cliquez sur une couleur pour cacher le code et permettre à votre adversaire de jouer")
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
    global Essai, Essai_sauvegarde
    global nombre_max_d_essais
    if Essai <= nombre_max_d_essais:
        if colonne < 4 :
            canvas.create_oval((x0 + colonne*50 , y0 + 50*(Essai - 1)), (x1 + colonne*50, y1 + 50*(Essai - 1)), fill = couleur)
            liste[Essai - 1][colonne] = couleur
            colonne += 1
    if colonne == 4:
        if liste[Essai - 1] == code:
            couleur_utilisee.configure(text="VICTOIRE", fg="green")
            label1.config(text="VICTOIRE!"+"\U0001F600", font=("helvetica", "15"), fg="darkgreen")
            return
        PetitsPions()
        # On réinitialise colonne pour les essais suivants :
        colonne = 0


def PetitsPions():
    """fonction qui pose automatiquement les petits pions blancs et rouges en fonction de l'essai"""
    global liste2
    global liste_ppions
    global Essai,Essai_sauvegarde
    nombre = 0
    nombre2 = 0
    # on utilise une deuxième liste pour les pions blancs :
    liste2 = list(code)
    ## Petits pions rouges :
    for i in range(4):
        if liste[Essai - 1][i] == code[i]:
            canvas.create_oval((320 + nombre*20, y0 + 50*(Essai - 1)), (335 + nombre*20, y0 + 50*(Essai - 1) + 15), fill="red")
            nombre += 1
            # s'il y a une couleur déjà utilisé on l'enlève de liste2 :
            liste2[i] = 0
            # on ajoute 1 à la liste ppion quand on ajoute des petits pions :
            liste_ppions[Essai - 1][0] += 1
    ## Petits pions blancs :
    for i in range(4):
        nbr_couleur_sup = 0 # indique quand on supprime une couleur de liste2
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
                    if nbr_couleur_sup == 0:
                        liste2[j] = 0
                        nbr_couleur_sup += 1
    # On ajoute 1 à Essai pour dire qu'on passe à l'essai suivant
    if Essai == 10:
        couleur_utilisee.configure(text="GAME OVER", fg="black")
        label1.config(text="PERDU!"+"\U0001F610", font=("helvetica", "15"), fg="darkred")
    Essai += 1
    #canvas.bind('<Button-1>', choisir_couleur)


def sauvegarde():
    """fonction qui sauvegarde la partie"""
    global liste_sauvegarde
    global code_sauvegarde 
    global codesecret_sauvegarde
    global bouton_charger
    global Essai_sauvegarde 
    global colonne_sauvegarde
    global liste_ppions_sauv
    global mode_sauvegarde
    global mode_sauvegarde2
    global sauvegarder
    sauvegarder = True
    liste_sauvegarde = copy.deepcopy(liste) # permet de copier 'en profondeur' la liste
    code_sauvegarde = code.copy()
    codesecret_sauvegarde = codesecret
    Essai_sauvegarde = Essai
    mode_sauvegarde = modesolo
    mode_sauvegarde2 = modesolo2
    colonne_sauvegarde = colonne
    liste_ppions_sauv = copy.deepcopy(liste_ppions)
    bouton_charger = tk.Button(racine, text="charger la partie sauvegardée", command=charger_partie, width = 25)
    bouton_charger.grid(column=3, row=6)

def charger_partie():
    """fonction qui permet de charger une partie précédement sauvegardée"""
    global liste
    global liste_ppions
    global arrêt
    global partie_chargee
    partie_chargee = True # on indique qu'on viens de charger la partie sauvegardée
    label1.config(text="Veuillez choisir une combinaison de pions")
    ### -On supprime d'abord graphiquement l'ancienne partie, si ce n'est pas déjà fait, et on reprend les valeurs sauvegardées
    # On enlève tous les Grands pions :
    for i in range(nombre_max_d_essais):
        for j in range(4):
            if liste[i][j] != 0:
                objet = canvas.find_closest(135 + (j*50), 125 + (i*50))
                canvas.delete(objet[0])
    # On reprend la liste sauvegardée :
    liste = copy.deepcopy(liste_sauvegarde)
    # On enlève tous les Petits pions :
    for i in range(nombre_max_d_essais):
        for j in range(liste_ppions[i][0]):
            objet = canvas.find_closest(350, 120 + (i*50))
            canvas.delete(objet[0])
    # En mode 2 joueurs, on enlève les cercles du code secret s'il y en a:
    if modesolo == 0:
        for i in range(4): # Pour chaque cercle du code, on prend son identifiant, et on le supprime :
            if i < codesecret:
                objet = canvas.find_closest(525 + (i*50), 45)
                canvas.delete(objet[0])
    # On reprend le code sauvegardé :
    code = code_sauvegarde.copy()
    # On reprend les indicateurs d'essais et de la colonne sauvegardés:
    Essai, colonne = Essai_sauvegarde, colonne_sauvegarde
    # On reprend la liste_ppions sauvegardée :
    liste_ppions = copy.deepcopy(liste_ppions_sauv)
    modesolo2 = mode_sauvegarde2
    ### -Maintenant on recréer graphiquement la partie
    # les Grands Pions :
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j] != 0:
                canvas.create_oval((x0 + j*50 , y0 + 50*i), (x1 + j*50, y1 + 50*i), fill = liste[i][j])               
    ################## (Partie adaptée de la fonction petit pions) Les Petits Pions
    #print(colonne)
    if colonne != 0: # si le dernier essai sauvegardé ne contient pas 4 grands pions... :
        a = Essai - 2
    else: a = Essai
    for j in range(Essai): # on pose les petits pions pour chaque essais
        if (j <= a): # on pose les petits pions ssi on est sur une ligne avec 4 grands pions placés
            # on utilise une deuxième liste pour les pions blancs :
            liste2 = list(code)
            nombre = 0
            nombre2 = 0
            ## Petits pions rouges :
            for i in range(4):
                    if liste[j][i] == code[i]:
                        canvas.create_oval((320 + nombre*20, y0 + 50*j), (335 + nombre*20, y0 + 50*j + 15),\
                        fill="red")
                        nombre += 1
                        # s'il y a une couleur déjà utilisé on l'enlève de liste2 :
                        liste2[i] = 0
            ## Petits pions blancs :
            for i in range(4):
                nbr_couleur_sup = 0 # indique quand on supprime une couleur de liste2
                    # si la couleur liste[j][i] est dans le code, mais pas à la bonne place, et que cette couleur dans le code
                # n'est pas déjà utilisée pour les pions rouges (cad qu'elle est dans liste2)... :
                if (liste[j][i] in liste2) and (liste[j][i] != code[i]):
                    # ...on met un pion blanc
                    canvas.create_oval((320 + nombre2*20, y0 + 25 + 50*j), (335 + nombre2*20, y0 + 40 + 50*j)
                    , fill="white")
                    nombre2 += 1
                    # s'il y a une couleur déjà utilisé on l'enlève de liste2 :
                    for k in range(4):
                        if liste2[k] == liste[j][i]:
                            if nbr_couleur_sup == 0:
                                liste2[k] = 0
                                nbr_couleur_sup += 1
            if j == 9:
                couleur_utilisee.configure(text="GAME OVER", fg="black")
    arrêt = False
    print(liste_ppions)
    #print(liste)
    canvas.bind('<Button-1>', choisir_couleur)

def arreter_partie():
    """foncton qui permet d'arrêter une partie en cours"""
    global bouton_relancer
    global arrêt
    arrêt = True
    bouton_arrêt.destroy()
    bouton_relancer = tk.Button(racine, text="Relancer une nouvelle partie", command=commencerpartie, width = 25)
    bouton_relancer.grid(column=3, row=3)


def retourner_en_arrière():
    """Fonction qui permet de revenir en arrière"""
    global Essai, colonne
    rev=[]
    for e in reversed(liste): # on lit la liste dans l'ordre inverse,
        # dans un premier temps, on cherche la derniere liste dans la liste qui contient des elements
        if e != [0, 0, 0, 0] : 
            rev = e
            Essai = liste.index(e)
            # dans un second temps, on cherche le dernier element de cette liste .
            for e in reversed(rev): 
                if e != [0]:
                    colonne = rev.index(e,-1) 
                    if rev.count(0) == 0: 
                        pass
                    elif rev.count(0) == 1:
                        colonne-=1
                    elif rev.count(0) == 2:
                        colonne-=2
                    elif rev.count(0) == 3:
                        colonne-=3
                    liste[Essai][colonne] = 0
                    canvas.create_oval((x0 + (colonne)*50 , y0 + 50*(Essai )), (x1 + (colonne)*50, y1 + 50*(Essai)),\
                    fill = "peru")
                    Essai +=1
                    break
            break


def aide() : 
    """fonction qui propose un code avec les informations des essais précédents, sans donner le code secret"""
    global aide 
    # note pour continuer la fonction :  aide est une liste vide
    # en fonction du nombre d'essai effectué, ajouter 4 couleurs déjà utilisées par l'utilisateur dans la liste et les afficher 
    # faire en sorte que l'aide ne soit pas identique au code secret 
    



# Création des widgets :
racine = tk.Tk()
canvas = tk.Canvas(racine, height= HAUTEUR, width= LARGEUR, bg="darkgray")
Titre = racine.title("Mastermind")
bouton_sauv = tk.Button(racine, text="Sauvegarder partie", command=sauvegarde, width = 25)
bouton_load = tk.Button(racine, text="Commencer une nouvelle partie", command= commencerpartie, width = 25, fg ="green")
bouton_triche = tk.Button(racine, text="Revenir en arrière",command= retourner_en_arrière,state=tk.DISABLED, width = 25)
bouton_aide = tk.Button(racine, text="Aide", command=aide, width = 25)
bouton_mode1 = tk.Button(racine, width = 25)
bouton_mode2 = tk.Button(racine, width = 25)

# Surface de textes :
label1 = tk.Label(racine, text="Bienvenue sur Mastermind ! Le but du jeu est de trouver la combinaison secrete \
de son adversaire en  10 coups. Pour commencer, il faut décider avec quel mode de jeu vous voulez jouer, \
c'est à dire si vous jouer contre l'ordinateur ou bien contre un adversaire . Bon Courage !",\
 font=("helvetica", "10"),wraplength=350,justify="left", bg="darkgray")


racine['bg']='gainsboro'

# Indicateur de la couleur actuelle utilisée :
couleur_utilisee = tk.Label(racine, text="aucune", font=("helvetica", "15"), fg=couleur, bg="grey")


quadrillage()
quadrillage2()
quadrillage3()





# Placement des widgets :
canvas.grid(column=0, row=0, columnspan=3, rowspan=7)
bouton_sauv.grid(column=3, row=2)
bouton_load.grid(column=3, row=3)
bouton_triche.grid(column=3, row = 0)
bouton_aide.grid(column=3, row=1)
couleur_utilisee.grid(column=5, row=4)
bouton_mode1.grid(column=3, row=4)
bouton_mode2.grid(column=3, row=5)
label1.grid(column=2, row=4)




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
# début du fichier readme (je le fait dans la journée) (C)
# -fin bouton arreter (T)
# -fin bouton recommencer (T)
# -mauvaises supressions des petits pions réglé (T)
# -problème sur les petits pions quand des grands pions ont la même couleur, réglé (T)
# -fonction sauvgarde et début fonction charger partie (T)
# -fonction commencer_partie_sauvegardee et fin fonction charger partie (M)
# -problème de disparition du code secret en mode 2 joueur lors du chargement d'une partie, réglé (T)
# -problème des Petits Pions quand on charge une partie où on a pas placé tous les Grands Pions sur la dernière ligne, réglé (T)
# -Fonction revenir en arrière terminée (T)
# -problème pour charger une partie quand on joue une nouvelle partie avant de la charher, réglé (T)
# début de la fonction aide
# -problèmes de la reprise de ligne, et de l'apparition des petits pions rouges, réglé (T)

## choses à faire:
# Désactiver les boutons mode si un choisit -- > sinon peut creer des erreurs
#-Faire fontionner les boutons aide 
#-les lignes trop longues à reduire

# REMARQUES :
# -les essais sont les lignes et pas le nombre de grands pions que l'on peut mettre par ligne, 
# il y a 10 essais de bases


## choses pour améliorer à la fin: