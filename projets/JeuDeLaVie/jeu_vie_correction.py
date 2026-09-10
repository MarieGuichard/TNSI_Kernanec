from random import *
import time
import pygame
from pygame.locals import *


def generation_grille(taille):
    ''' genere un tableau de tableaux de longueur et de largeur valant taille et  contenant des zéros (cellules mortes )
        taille <- int '''
    ma_grille = []
    for j in range(taille):
        ligne = []
        for i in range(taille):
            ligne.append(0)
        ma_grille.append(ligne)
    return ma_grille
   

def place_cellules_v(grille, cellules_vivantes):
    '''place des cellules vivantes dans la grille (matérialisés par des 1)
    grille <- généré grace à la fonction generation_grille()
    cellules_vivantes <- tabeau contenant les tuples de coordonnées des cellules vivantes
    renvoie la grille modifiée
    '''
    for cellule in cellules_vivantes:
        ligne = cellule[0]
        colonne = cellule[1]
        grille[ligne][colonne]=1
    return grille
    

def place_cellules_aléa(grille, nombre):
    ''' place de manière aléatoire un nombre de cellules vivantes dans la grille
        grille <- généré grace à la fonction generation_grille()
        renvoie la grille modifiée
        '''
    nombre_cellule_v = 0
    while nombre_cellule_v != nombre:
        ligne = randint(0,len(grille)-1)
        colonne = randint(0,len(grille)-1)
        if grille[ligne][colonne] == 0:
            grille[ligne][colonne] = 1
            nombre_cellule_v +=1
    return grille

def compte_voisins_vivants(grille,coord):
    ''' Compte le nombre de cellules vivantes voisines de la cellule de coordonnées (i,j), i représentant la colonne et j la ligne
        grille <- tableau de tableaux
        coord <- tuple contenant des entiers compris entre 0 et len(grille)-1
        renvoie un entier'''
    l = coord[0]
    c = coord[1]
    if 1<=l<=len(grille)-2 and 1<=c<=len(grille)-2:
        les_voisins=[(l,c-1),(l,c+1),(l+1,c-1),(l+1,c),(l+1,c+1),(l-1,c-1),(l-1,c),(l-1,c+1)]
    if l==0 and c==0:
        les_voisins = [(l,c+1),(l+1,c),(l+1,c+1)]
    if l==0 and c == len(grille)-1:
        les_voisins = [(l,c-1),(l+1,c-1),(l+1,c)]
    if l == len(grille)-1 and c == 0:
        les_voisins = [(l-1,c),(l-1,c+1),(l,c+1)]
    if l == len(grille)-1 and c == len(grille)-1:
       les_voisins = [(l-1,c-1),(l-1,c),(l,c-1)]
    if l == 0 and 1<=c<=len(grille)-2:
        les_voisins = [(l,c-1),(l,c+1),(l+1,c-1),(l+1,c),(l+1,c+1)]
    if l == len(grille)-1 and 1<=c<=len(grille)-2:
        les_voisins = [(l,c-1),(l,c+1),(l-1,c-1),(l-1,c),(l-1,c+1)]
    if c == 0 and 1<=l<=len(grille)-2:
        les_voisins = [(l-1,c),(l+1,c),(l-1,c+1),(l-1,c),(l+1,c+1)]
    if c == len(grille)-1 and 1<=l<=len(grille)-2:
        les_voisins = [(l-1,c-1),(l-1,c),(l,c-1),(l+1,c-1),(l+1,c)]
    return les_voisins
        
  
def grille_voisins(grille):
    ''' genere une grille contenant le nombre de cellules vivantes voisines
    grille <- tableau de tableaux
    renvoie un tableau de tableaux
      '''
    pass

def update_grille(grille):
    ''' actualise la grille aprés un cycle de vie
    grille <- tableau de tableaux contenant les cellules vivantes et les cases vides.
    renvoie la grille modifiée'''
    pass

def trace(grille):
    ''' permet de gérer l'affichage de la grille
    Les cellules vivantes seront en rouge (vous pouvez jouer avec les couleurs si vous voulez quelque chose de plus esthétique'''
    pygame.init()
    taille_grille = 600//len(grille)
    # On crée une fenêtre à la taille de la grille
    fenetre = pygame.display.set_mode((taille_grille*len(grille[0]), taille_grille*len(grille)))
    # On dessine les cellules
    #dessine_cellules(grille)
    carre = pygame.Surface((taille_grille,taille_grille), pygame.SRCALPHA)
    running = True
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            if grille[y][x] == 1:
                color = (255, 0, 0)
            else:
                color = (0,0,0)
            carre.fill(color)
            fenetre.blit(carre, (x*taille_grille, y*taille_grille))
        #modifie la fenêtre
        pygame.display.flip()

 


if __name__ == '__main__':
    # A compléter, doit permettre au jeu de la vie de fonctionner
#     running = True
#     while running:
#         for event in pygame.event.get(): # détecte un évenement pygame
#             if event.type == QUIT: # repère si vous souhaitez fermer la fenêtre pygame
#                 running = False
#     pygame.quit() # ferme la fenêtre pygame
#
    pass
