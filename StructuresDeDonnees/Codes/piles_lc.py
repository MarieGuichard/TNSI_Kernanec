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
        self.ma_pile = Lc()
        
    def empiler(self,x):
        '''empile l'élèment x dans la pile'''
        self.ma_pile.inserer(x,0)
    
    def depiler(self):
        '''depile un element de la pile'''
        self.ma_pile.supprimer(0)
        
        
    def element_depile(self):
        '''renvoie l'élèment dépilé de la pile'''
        j = self.ma_pile.__getitem__(0) #self.ma_pile[0]
        self.ma_pile.supprimer(0)
        return j
        
    
    def pile_vide(self):
        '''renvoie True si la pile est vide, False sinon
        >>> mapile = Pile_list()
        >>> mapile.pile_vide()
        True
        >>> mapile.empiler(3)
        >>> mapile.pile_vide()
        False
        '''
        return self.ma_pile.vide()

        
    def __len__(self):
        '''affiche le nombre d'élèments contenus dans la pile'''
        return len(self.ma_pile) # self.ma_pile.__len__()
    
    def __str__(self):
        '''renvoie le contenu de la pile sous forme d'une chaine de caractéres'''
        return self.ma_pile.__str__()
    
    def depiler_entierement(self):
        while not self.pile_vide():
            self.depiler()
    
    def inverse_pile(self):
        nv_lc = Lc()
        while not self.pile_vide():
            nv_lc.inserer(self.element_depile(),0)
        self.ma_pile = nv_lc
            
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

