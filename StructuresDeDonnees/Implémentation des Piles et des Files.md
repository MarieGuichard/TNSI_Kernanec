# Implémentation des Piles et des Files.  



## I. Les Piles.  

### 1. avec les list.

​	Une première implémentation des piles a été faite dans la class `Pile_list`dont vous trouverez le code dans le répertoire Code. 

1. Écrire un jeu de test pour chacune des méthodes écrites.
2. Écrire une méthode `depile_entierement(self)` qui vide complétement la pile.  		
3. Ecrire une méthode `inverse_pile(self)` qui renvoie la pile dans l'ordre inverse.  		



### 2. Avec les listes chaînées.  	



​	Une deuxième manière d'implémenter les piles est d'utiliser les listes chaînées. 	 

En reprenant la classe `Lc` vu précédemment,

1. Ecrire les mêmes méthodes que celles fournies au 1. 
2. Tester ces méthodes avec les tests élaborés précédemment. 
3. Ecrire une  méthode `depile_entierement(self)` qui vide complétement la pile.  		
4. Ecrire une méthode `inverse_pile(self)` qui renvoie la pile dans l'ordre inverse.  		






## II. Les Files.

### 1. avec les list.



​	Écrire les méthodes permettant d'implémenter une file (reprendre les méthodes faites pour les Piles). 

```python
class File_list:
    '''implémenation d' une classe file avec une liste'''
    def __init__(self):
        self.ma_file = []
```



### 2. Avec deux piles. 

​	Il est possible d'implémenter une file avec deux piles. 



​	Prenons un exemple pour comprendre comment cela fonctionne.



​	Soit un jeu de cartes sur lequel on disposerait d'une pioche, au sommet de laquelle on prend des cartes, disposées face cachée, et d'une défausse, au sommet de laquelle on repose des 	cartes, disposées face visible. 

​	Chacun de ces deux paquets de cartes est une pile, et ces deux paquets forment ensemble la réserve de cartes. 

​	On a ensuite la discipline suivante : 

- toute carte prise dans la réserve est retirée dans l'une de ces piles (la pioche) ,

- toute carte remise dans la réserve est ajoutée à l'autre pile (la défausse).  	

​	A cela, s'ajoute un mécanisme liant les deux paquets : une fois la pioche vide, on retourne la défausse pour en faire une nouvelle pioche, laissant la place à une défausse vide. 



​	Cette gestion des cartes correspond à une structure de file : une fois la pioche initiale vidée, 	les cartes seront piochées précisément dans l'ordre dans lequel elles ont été défaussées. La 	première défaussée sera la première piochée. 



​	En utilisant la class File de votre choix, implémenter une classe File en utilisant deux Piles.

​		

```python
class Files_2piles:
    def __init__(self):
        self.entree = Pile() # pile dans laquelle on ajoute les nouveaux élèments
        self.sortie = Pile() # pile dans laquelle on prend les élèments retirés
```

​	
