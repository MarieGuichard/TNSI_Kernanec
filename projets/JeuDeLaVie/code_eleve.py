from random import *
import time
import pygame
from pygame.locals import *


def generation_grille(taille: int)-> list[list]:
    ''' genere un tableau de tableaux de longueur et de largeur valant taille et  contenant des zéros (cellules mortes )
        taille <- int '''
    pass
   

def place_cellules_v(grille:list[list], cellules_vivanteslist[tuple])->list[list]:
    '''place des cellules vivantes dans la grille (matérialisés par des 1)
    grille <- généré grace à la fonction generation_grille()
    cellules_vivantes <- tabeau contenant les tuples de coordonnées des cellules vivantes
    renvoie la grille modifiée
    '''
    pass

def place_cellules_aléa(grille:list[list], nombre: int)->list[list]:
    ''' place de manière aléatoire un nombre de cellules vivantes dans la grille
        grille <- généré grace à la fonction generation_grille()
        renvoie la grille modifiée
        '''
    pass

def compte_voisins_vivants(grille:list[list],coord:tuple)-> int:
    ''' Compte le nombre de cellules vivantes voisines de la cellule de coordonnées (i,j), i représentant la colonne et j la ligne
        grille <- tableau de tableaux
        coord <- tuple contenant des entiers compris entre 0 et len(grille)-1
        renvoie un entier'''
    pass
  
def grille_voisins(grille:list[list])->list[list]:
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

