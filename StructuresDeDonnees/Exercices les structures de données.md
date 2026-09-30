## Exercices: les structures de données



### Exercice 1:

Pour chacune des situations suivantes, donnez la structure de données la plus adaptée.

1. La gestion du flux de personnes arrivant dans une préfecture.
2.  Les opérations effectuées dans un logiciel de dessin pour que l'on puisse les annuler.
3. Envoyer des fichiers à un serveur d'impression. 
4. Un répertoire téléphonique où l'on accède au téléphone en rentrant un nom. 
5. Mémoriser tous les coups d'une partie d'échecs. 



### Exercice 2: 

On s’intéresse aux expressions pouvant contenir des parenthèses `(` et `)`, des crochets  `[`  et `]` et des accolades `{ ` et  `}`. 

L’objectif de l’exercice est d’étudier quelles expressions sont bien ou mal parenthésées. 

Par exemple l’expression `[a-(b-c]+d)`est mal parenthésée car la parenthèse fermante ne peut pas venir après le crochet fermant.

 En utilisant une pile, écrire une fonction `bien_parenthesee(s)` qui renvoie un booléen indiquant si une expression est bien parenthésée ou non (s est une chaîne de caractères comportant les trois types de parenthèses précédentes).



### Exercice 3: 

On considère l’expression (7-8)∗6∗(10+3).

 En notation polonaise inversée (NPI) ou notation post-fixée, cette expression est codée par une liste Python de la manière suivante : ` L = [7, 8, ’-’, 6, ’∗’, 10, 3, ’+’, ’∗’] `. Certaines calculatrices de marque HP des années 1990 adoptaient cette notation et utilisaient une pile pour effectuer les calculs.

 Pour calculer cette expression, on parcourt les éléments de la liste L :

 • si l’élément est un nombre, on l’empile ; 

• s’il s’agit d’une opération, on effectue l’opération à partir des deux derniers éléments de la pile puis on empile le résultat (attention à l’ordre si l’opération n’est pas commutative).

 Écrire une fonction evalNPI(L) utilisant une pile qui calcule l’expression post-fixée correspondant à la liste L et renvoie la valeur.

```
>>> evalNPI([7, 8, ’-’, 6, ’∗’, 10, 3, ’+’, ’∗’]
- 78
```



### Exercice 4 pour aller vers le Bac: 

La classe `Pile`dans cet exercice est implémentée en utilisant des listes Python et propose quatre éléments d'interface:

- un constructeur qui permet de créer une pile vide, représentée par [ ];
- la méthode `est_vide()`qui renvoie `True`si l'objet est une plie ne contenant aucun élément et `False` sinon;
- la méthode `empiler`qui prend un objet quelconque en paramètre et ajoute cet objet au somme de la pile. Dans la représentation de la pile dans la console, cet objet apparaît à droite des autres éléments de la pile;
- la méthode `depiler` qui renvoie l'objet présent au sommet de la pile et le retire de la pile. 



Exemples:

``` 
>>> mapile = Pile()
>>> mapile.empiler(2)
>>> mapile
[2]
>>> mapile.empiler(3)
>>> mapile.empiler(50)
>>> mapile
[2, 3, 50]
>>> mapile.depiler()
50
>>> mapile
[2, 3]
```

La méthode `est_triee`ci-dessous renvoie `True`si, en dépilant tous les éléments, ils sont traités dans l'ordre croissant, et `False`sinon. 

```
1. def est_triee(self):
2.    if not self.est_vide():
3.      e1 = self.depiler()
4.    while not self.est_vide():
5.      e2 = self.depiler()
6.      if e1 ... e2:
7.         return False
8.      e1 = ....
9.    return True
```

1. Compléter les lignes 6 et 8 en remplaçant les points de suspension. 

   On créé dans la console la pile `A`représentée par `[1, 2, 3, 4]`

2. a. Donner la valeur renvoyée par l'appel `A.est_triee()`

   b. Donner le contenu de la pile `A`après l'exécution de cette instruction. 

   On souhaite maintenant écrire le code d'une méthode `depileMax`d'une pile non vide ne contenant que des nombres entiers et renvoyant le plus grand élément de cette pile en le retirant de la pile. 

   Après l'exécution de `p.depileMax()`, le nombre d'élèments de la pile `p`diminue donc de 1.

   ```
   1. def depileMax(self):
   2.     assert not self.est_vide(), "Pile vide"
   3.     q = Pile()
   4.     maxi = self.depiler()
   5.     while not self.est_vide() :
   6.        elt = self.depiler()
   7.        if maxi < elt:
   8.            q.empiler(maxi)
   9.            maxi = ......
   10.       else:
   11.           ......
   12.    while not q.est_vide():
   13.       self.empiler(q.depiler())
   14.    return maxi
   ```

   3. Compléter les lignes 9 et 11. 

   On créé la pile `B`représentée par `[9, -7, 8, 12, 4]`et on effectue l'appel `B.depileMax()`.

   4. a. Donner le contenu des piles `B` et `q` à la fin de chaque itération de la boucle `while`de la ligne 5. 

      b. Donner le contenu des piles `B `et  `q` avant l'exécution de la ligne 14. 

      c. Donner un exemple de pile qui montre que l'ordre des éléments restants n'est pas préservé après l'exécution de `depileMax`. 

   On donne le code de la méthode `traiter()`.

   ```
   1. def traiter(self):
   2.    q = Pile()
   3.    while not self.est_vide():
   4. 	      q.empiler(self.depileMax())
   5.    while not q.est_vide():
   6.        self.empiler(q.depiler())
   ```

   5. a. Donner les contenus successifs des piles `B` et `q`. 
      - avant la ligne 3,
      - avant la ligne 5, 
      - à la fin de l'exécution de la fonction `traiter`

​				lorsque la fonction `traiter`est appliquée sur la pile `B`contenant

​				 `[1, 6, 4, 3, 7, 2]`. 

​				b. Expliquer le traitement effectué par cette méthode. 

### Exercice 5 pour aller vers le Bac:

On dispose de la liste `jour`suivante et du dictionnaire `mois`suivant:

`jours = ["dimanche","lundi","mardi","mercredi","jeudi","vendredi","samedi"]`

`mois={1 :("janvier",31) , 2 :("février",28) , 3 :("mars",31),  4 :("avril",30) , 5 :("mai",31) , 6 :("juin",30) ,  7 :("juillet",31) , 8 :("aout",31) , 9 :("septembre",30) ,  10 :("octobre",31) , 11 :("novembre",30) ,  12 :("décembre",31)} `

1. a. A partir de la liste `jours`, comment obtenir l'élément `"lundi"`? 

   b. On rappelle que l'opérateur % ("modulo") renvoie le reste de la division entière (division euclidienne). 

   Exemple: 7%3 renvoie 1 qui est le reste de la division de 7 par 3. 

   Que renvoie l'instruction `jours[18%7]`? 

2. On rappelle que `jours.index[element]`renvoie l'indice de `element`dans la liste `jours` . 

   Par exemple: `jours.index["mercredi"]`renvoie 3. 

   Le nom du jour actuel est stocké dans une variable `j`. 

   Par exempe: `j="mardi"`. 

   Compléter l'instruction suivante permettant d'obtenir le numéro du jour de la semaine `n `jours plus tard:

   `numero_jour=(jours.index[...]+...)%....`

3. a. A partir du dictionnaire `mois`, comment obtenir le nombre de jours du mois de mars? 

   b. Le numéro du mois actuel est stocké dans une variable `numero_mois`, écrire le code permettant d'obtenir le nom du mois qu'il sera `x`mois plus tard à partir du dictionnaire `mois`

   Par exemple:

   si `numero_mois =4 et x = 5`, on doit obtenir ` "septembre"`

   si `numero_mois =10 et x = 3`, on doit obtenir ` "janvier"`

4. On définit une date comme un tuple:

   `(nom_jour,numero_jour, numero_mois,annee) `.

   a. Sachant que `date = ("samedi", 21, 10, 1995)`, que renvoie  `mois[date[2]][1]`  ? 

    b. Ecrire une fonction `jour_suivant(date)` qui prend en paramètre une  date sous forme de tuple et qui renvoie un tuple désignant la date du  lendemain. 

   Par exemple :  

   `jour_suivant( ("samedi", 21, 10, 1995) )` renvoie  `("dimanche", 22, 10, 1995) ``jour_suivant( ("mardi", 31, 10, 1995) )` renvoie ` ("mercredi", 1, 11, 1995)` 

   On ne tient pas compte des années bissextiles et on considère que le mois  de février comporte toujours 28 jours.



### Exercice 6(Bac):

Un supermarché met en place un système de passage automatique en caisse.  Un client scanne les articles à l’aide d’un scanner de code-barres au fur et à mesure  qu’il les ajoute dans son panier.  Les articles s’enregistrent alors dans une structure de données.  

La structure de données utilisée est une file définie par la classe ` Panier`, avec les  primitives habituelles sur la structure de file. 

 Pour faciliter la lecture, le code de la classe `Panier` n’est pas écrit.

```
class Panier(): 
 def __init__(self): 
 """Initialise la file comme une file vide.""" 
 def est_vide(self):
 """Renvoie True si la file est vide, False sinon.""" 
 def enfiler(self, e):
 """Ajoute l'élément e en dernière position de la file, 
 ne renvoie rien.""" 
 def defiler(self):
 """Retire le premier élément de la file et le renvoie.""" 
```

Le panier d’un client sera représenté par une file contenant les articles scannés.  Les articles sont représentés par des tuples `(code_barre, designation,  prix, horaire_scan)` où  

- ` code_barre` est un nombre entier identifiant l’article ;  
- `designation `est une chaine de caractères qui pourra être affichée sur le  ticket de caisse ;  
- ` prix ` est un nombre décimal donnant le prix d’une unité de cet article ;  
- ` horaire_scan`est un nombre entier de secondes permettant de connaitre  l’heure où l’article a été scanné.

1. On souhaite ajouter un article dont le tuple est le suivant

     `(31002, "café noir", 1.50, 50525)`. 

    Ecrire le code utilisant une des quatre méthodes ci-dessus permettant d’ajouter  l’article à l’objet de classe `Panier` appelé `panier1`.

2. On souhaite définir une méthode `remplir(panier_temp)` dans la classe  `Panier` permettant de remplir la file avec tout le contenu d’un autre panier  `panier_temp` qui est un objet de type ` Panier`.

   Recopier et compléter le code de la méthode` remplir` en remplaçant chaque  …………… par la primitive de file qui convient.

   ```
   def remplir(self, panier_temp): 
   	while not panier_temp. …………… : 
    		article = panier_temp. ……………
   	self. ……………(article)
   ```

3. Pour que le client puisse connaitre à tout moment le montant de son panier, on  souhaite ajouter une méthode `prix_total()` à la classe Panier qui renvoie  la somme des prix de tous les articles présents dans le panier.  Ecrire le code de la méthode `prix_total`. Attention, après l’appel de cette  méthode, le panier devra toujours contenir ses articles.
4.  Le magasin souhaite connaitre pour chaque client la durée des achats. Cette  durée sera obtenue en faisant la différence entre le champ `horaire_scan` du  dernier article scanné et le champ `horaire_scan` du premier article scanné  dans le panier du client. Un panier vide renverra une durée égale à zéro. On  pourra accepter que le panier soit vide après l’appel de cette méthode.  Ecrire une méthode `duree_courses` de la classe Panier qui renvoie cette  durée.



### 



