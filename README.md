# Projet n°2 : MASTERMIND - MITD02 groupe 4 
- URL du projet : https://github.com/uvsq22100961/projet2_mastermind 

## Membres du groupe : 
- Thibault ROYERE
- Camille ROESLER
- Manira MAHAMAT HAGGAR

## Présentation globale du projet 



![interface début](https://user-images.githubusercontent.com/98943826/167256807-4392cdca-ad87-4c82-b1b2-89460736f2ef.png)



### But du jeu :  

Le but du MASTERMIND est de trouver un code secret, choisi par un utilisateur ou l'ordinateur, tout en prenant en compte les informations données sur les pions. 
Le code est composé de quatre pions colorés, chaque couleur peut apparaître plusieurs fois dans le code. Des cercles rouges et blancs indiquent à chaque essai le nombre de pion bien ou mal placés.

Notre MASTERMIND peut se jouer seul ou à deux joueurs, et possède trois fonctionnalités non présentes dans le jeu original sur plateau.  

#### Les pions 

- Un cercle rouge indique un pion bien placé 
- Un cercle blanc indique un cercle mal placé 

Un pion bien placé est un pion de la bonne couleur et à la bonne place 

Un pion mal placé est un pion ayant une couleur apparaîssant dans le code secret mais pas à la bonne place 


![image](https://user-images.githubusercontent.com/98943826/167257812-9edde2d3-d23a-43f7-ae2d-44fd653592bc.png)

Dans l'exemple ci-dessus, à la 3e ligne il y a 1 pion bien placé et 2 pions mal placés.

### Les modes de jeu : 

![image](https://user-images.githubusercontent.com/98943826/167257691-501890aa-bfb6-41af-8b35-b9535c07fb9b.png)

Image : Choix du mode de jeu 


#### Mode 1 joueur 

Déroulement du jeu : après avoir choisi le mode 1 joueur l'ordinateur génère automatiquement un code secret. le joueur à ensuite 10 essais pour trouver ce code secret. 


#### Mode 2 joueur 

Déroulement du jeu : le joueur 1 choisi un code en cliquant sur les cercles de couleurs en haut de la fenêtre. Une couleur peut apparaître plusieurs fois dans le code secret. Ensuite, le joueur n°2 a 10 essai pour décoder le code choisi par le joueur n°1. 

![choix code 2 joueurs](https://user-images.githubusercontent.com/98943826/167257388-299f361e-73aa-4987-a767-16dfe0738be5.png)
![code caché](https://user-images.githubusercontent.com/98943826/167257321-42fa62db-9874-4598-848a-1d9878b5a26a.png)

A gauche : le code choisi par le premier joueur, à droite : le code est caché pour que le joueur n°2 ne le voit pas. 
 

## Autres fonctionalités 

- Revenir en arrière 

Le bouton "revenir en arrière" permet au joueur d'éffacer le/les dernier(s) pions. Ce bouton est donc un bouton de triche car le joueur aura vu les cercles lui indiquant le nombre de pions bien/mal placés. 

![image](https://user-images.githubusercontent.com/98943826/167311126-1d493560-8c4a-47f7-ba34-826fcafe5b80.png)

Image illustrant un joueur qui vient de cliquer sur "revenir en arrière"


- Aide 

Le bouton "aide" propose un code possible, en prenant en compte les indications données par les cercles rouges et blancs, sans donner le code secret. 



- Sauvegarder / Charger une partie 

Les boutons "sauvegarder partie" et "charger la partie sauvegardée" permette de sauvegarder une partie en cours qui pourra être chargée plus tard. 


## Fin de partie 

Lorsque au bout de 10 essais le joueur qui décode n'a pas trouvé le code, la partie s'arrête et un message "perdu" est affiché. Mais, si il a réussi à trouver le code, un message "victoire" est affiché. les images ci-dessous illustrent les deux cas. 

![image](https://user-images.githubusercontent.com/98943826/167312373-c50fc0b8-e546-468c-bcc7-4014712e0d94.png)
![image](https://user-images.githubusercontent.com/98943826/167312380-e4a43b3b-59b4-4383-a99a-aeee5e9c8281.png)




A vous de jouer ! 
