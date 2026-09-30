class Pile_list:
    '''implémentation d'une pile à l'aide d'un tableau python'''
    def __init__(self):
        '''constructeur de la pile'''
        self.ma_pile =[]
    
    def pile_vide(self):
        '''renvoie True si la pile est vide, False sinon'''
        return self.ma_pile == []
    
    def empiler(self,x):
        '''empile l'élèment x dans la pile'''
        self.ma_pile.append(x)
    
    def depiler(self):
        '''depile un element de la pile'''
        self.ma_pile.pop()
        
    def element_depile(self):
        '''renvoie l'élèment dépilé de la pile'''
        return self.ma_pile.pop()
        
    def __len__(self):
        '''affiche le nombre d'élèments contenus dans la pile'''
        return len(self.ma_pile)
    
    def __str__(self):
        '''renvoie le contenu de la pile sous forme d'une chaine de caractéres'''
        contenu=''
        for i in range(len(self)):
            contenu = contenu +" " + str(self.ma_pile[i])
        return contenu
    
    def depiler_entierement(self):
        for i in range(len(self)):
            print(self.depiler())
    
    def inverse_pile(self):
        retourne = []
        for i in range(len(self)):
            dessus = self.element_depile()
            retourne.append(dessus)
        self.ma_pile = retourne

    
    
