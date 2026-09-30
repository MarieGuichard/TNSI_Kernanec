class Cell:
    '''Cellule d'une liste chainee'''
    def __init__(self,valeur,suivant=None):
        self.valeur=valeur
        self.suivant=suivant

    def __str__(self):
        return str(self.valeur)

class Lc:
    '''Liste chaînée'''
    def __init__(self, tete=None):
        '''tete : lien vers la premiere cellule'''
        self.tete=tete
        
        
    
     
    
class Pile_lc:
    '''implémentation d'une pile à l'aide d'un tableau python'''
    def __init__(self):
        '''constructeur de la pile'''
        pass 
        
    def empiler(self,x):
        '''empile l'élèment x dans la pile'''
        self.ma_pile.inserer(x,0)
    
    def depiler(self):
        '''depile un element de la pile'''
        pass
        
        
    def element_depile(self):
        '''renvoie l'élèment dépilé de la pile'''
        pass
        
    
    def pile_vide(self):
        '''renvoie True si la pile est vide, False sinon
        >>> mapile = Pile_list()
        >>> mapile.pile_vide()
        True
        >>> mapile.empiler(3)
        >>> mapile.pile_vide()
        False
        '''
        pass

        
    def __len__(self):
        '''affiche le nombre d'élèments contenus dans la pile'''
        pass
    
    def __str__(self):
        '''renvoie le contenu de la pile sous forme d'une chaine de caractéres'''
        pass
    
    def depiler_entierement(self):
        pass
        
    def inverse_pile(self):
       pass
            
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

