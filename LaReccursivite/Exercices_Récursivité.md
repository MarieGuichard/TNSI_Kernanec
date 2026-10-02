# Récursivité: les exercices. 



#### Exercice 1: 

On suppose que l'on dispose déjà d'une fonction `demande_mdp()` qui demande à l'utilisateur d'entrer une chaine de caractéres et d'une fonction `message_erreur()`qui renvoie à l'utilisateur un message d'erreur. 

La consigne de l'enseignante est d'écrire, de manière récursive, une fonction `verifie_mdp()` qui permet de demander à l'utilisateur le mot de passe, lui renvoie un message d'erreur s'il s'est trompé et refait une demande tant qu'il n'a pas trouvé. 

Voici la réponse proposée par Hugo:

```python
def verifie_mdp():
	mdp=demande_mdp()
	while mdp != "secret_1234":
		message_erreur()
		mdp = demande_mdp()
```



Voici la réponse proposée par Adib:

```python
def verifie_mdp():
	mdp=demande_mdp()
	if  mdp != "secret_1234":
		message_erreur()
		verifie_mdp()
```

1.  Les fonctions proposées par Adib et Hugo fonctionnent-elles correctement ?
2.  Lequel de ces deux élèves a-t-il respecté la consigne donnée par l'enseignante? 
3. Dans la fonction récursive, identifiez le cas de base. 



#### Exercice 2: 

On veut créer une fonction récursive `somme(n)` qui **renvoie** la somme des entiers de `1` à `n` inclus.

- `n` est un entier strictement supérieur à 0.
- Exemples :
  - $1+2+3+4=10$ , donc `somme(4)` renvoie `10`.
  - $1+2+3+4+5=15$, donc `somme(5)` renvoie `15`.

1. Exprimer `somme(5)`en fonction de `somme(4)`. 
2. Pour `n>0`, exprimer `somme(n)`en fonction de `n`et de `somme(n-1)`. 
3. Combien vaut `somme(1)`? 
4. Ecrire de manière récursive la fonction `somme(n)`. 



#### Exercice 3:

Nous voulons écrire une fonction `retourne(texte)`qui prend en paramètre une chaine de caractères et qui renvoie cette chaine de caractères retournée. 

1. Ecrire une série de trois tests permettant de vérifier que cette fonction effectue bien le travail demandé. 

2. Cette fonction doit être écrite de manière récursive. 

   Nous utiliserons pour cela les slices:

   ```python
   >>> machaine = "Chocolat"
   >>> machaine[0:4]
   "Choc"
   >>> machaine[1:6]
   "hocol"
   >>> machaine[1:]
   "hocolat"
   
   ```

   

   a. Quel est le cas de base de notre fonction récursive ? 

   b. Ecrire la fonction `retourne(texte)` et tester la.



#### Exercice 4 :

 Écrire une fonction qui calcule la moyenne d'un tableau t non vide :

1. de manière itérative,
2. de manière récursive. 	



#### Exercice 5 : 

Écrire une fonction récursive `nombre_de_chiffres (n)` qui prend en paramètre un entier positif ou non et renvoie son nombre de chiffres. 

Par exemple, `nombre_de_chiffres(34126)` doit renvoyer 5. 



#### Exercice 6 :

 Écrire une fonction récursive `nombre_de_bits(n)` qui prend en paramètre un entier positif ou nul et renvoie le nombre de bits valant 1 dans la représentation binaire de n. 

Par exemple, `nombre_de_bits(255)` doit renvoyer 8.



#### Exercice 7 (**): 

1. En partant du coin supérieur gauche, dessinez sur une feuille la figure suivante sans lever le stylo et sans repasser deux fois sur le même trait :

![img](https://kxs.fr/cours/recursivite/img/carres.png)

2. Écrire une fonction récursive à deux paramètres (la longueur du plus grand carré, le nombre de carrés imbriqués) permettant de réaliser ce dessin avec le module turtle [](https://docs.python.org/fr/3/library/turtle.html)

   

#### Exercice 8(**): 

L'objectif de cet exercice est de  dessiner le flocon de Von Koch avec le module turtle.

1. Ecrire une fonction récursive qui permet de dessiner le fractal de Kosh ci-dessous. 

![](F:\lycee\T NSI\recursivité\fractaldevonkoch.jpg)



. La fonction de Koch prendra comme argument la longueur du segment et l'ordre : `koch(l,n)`

2. Ecrire une fonction (non récursive) utilisant la fonction de Kosh qui permet de dessiner le flocon de Kosh ci-dessous. Sont dessinés ci-dessous les flocons d'ordre 0, 1, 2 et 3. Cette fonction aura comme arguments la longueur du segment et l'ordre : `flocon(1,n)`

![img](https://kxs.fr/cours/recursivite/img/flocon.jpg)



#### Exercice 9 (en route vers le bac):

On se déplace dans une grille rectangulaire. On s’intéresse aux chemins dont le départ est sur la case en haut à gauche et l’arrivée en bas à droite. Les seuls déplacements autorisés sont composés de déplacements élémentaires d’une case vers le bas ou d’une case vers la droite. Un itinéraire est noté sous la forme d’une suite de lettres :

- D pour un déplacement vers la droite d’une case;
- B pour un déplacement vers le bas d’une case.

Le nombre de caractères D est la longueur de l’itinéraire. Le nombre de caractères B est sa largeur. 

Ainsi l’itinéraire `DDBDBBDDDDB` a pour longueur 7 et pour largeur 4. Sa représentation graphique est :

```
S * *
    * *
      *
      * * * * *
              E
```



- S représente la case de départ (start). Ses coordonnées sont (0; 0);

- `*`représente les cases visitées;
- E représente la case d’arrivée (end).
  

Partie A – Programmation orientée objet

On représente un itinéraire avec la classe Chemin suivante :



```python
1 class Chemin:
2
3 	def __init__(self, itineraire):
4.		self.itineraire = itineraire
5 		longueur, largeur = 0, 0
6 		for direction in self.itineraire:
7 			if direction == "D":
8 				longueur = longueur + 1
9 			if direction == "B":
10 				largeur = largeur +1
11		self.longueur = longueur
12 		self.largeur = largeur
13 		self.grille = [['.' for i in range(longueur+1)] for j in
range(largeur+1)]
14
15 def remplir_grille(self):
16 		i, j = 0, 0 # Position initiale
17 		self.grille[0][0] ='S' # Case de départ marquée d'un S
18 		for direction in...:
19 			if direction =='D':
20				... =... # Déplacement vers la droite 
21 			elif direction =='B':
22				... =... # Déplacement vers le bas
23 			self.grille[i][j] ='*' *# Marquer le chemin avec '*'
24 		self.grille[self.largeur][self.longueur] ='E' # Case d'arrivée marquée d'un E
```

1. Donner un attribut et une méthode de la classe `Chemin`.
   On exécute le code ci-dessous dans la console Python : 

   ```python
   chemin_1 = Chemin("DDBDBBDDDDB") 
   
   a = chemin_1.largueur 
   
   b = chemin_1.longueur
   ```

   

2. Préciser les valeurs contenues dans chacune des variables `a` et `b`.

3. Recopier et compléter la méthode `remplir_grille` qui remplace les '.' par des '*' pour signifier que le déplacement est passé par cette cellule du tableau.

4. Écrire une méthode `get_dimensions` de la classe `Chemin` qui renvoie la longueur et la largeur de l’itinéraire sous la forme d’un tuple.

5. Écrire une méthode `tracer_chemin` de la classe `Chemin` qui affiche une représentation graphique d’un itinéraire.

Partie B – Génération aléatoire d’itinéraires

On souhaite créer des chemins de façon aléatoire. Pour cela, on utilise la méthode `choice` de la bibliothèque `random` dont on fournit ci-dessous la documentation.

### 

```
`random.choice(sequence : list)`
Renvoie un élément choisi dans une liste non vide.
Si la population est vide, lève `IndexError`.
```

On rappelle que l’opérateur * permet de répéter une chaîne de caractères. Par exemple, on a : 

```python
>>> "Hello world ! " * 3
'Hello world ! Hello world ! Hello world ! '
```

L’algorithme proposé est le suivant :

- on initialise :

   – une variable `itineraire` comme une chaîne de caractères vide, 

   – les variables `i` et `j` à 0;

- tant que l’on n’est pas sur la dernière ligne ou la dernière colonne du tableau :

   – on tire au sort entre un déplacement à droite ou en bas,

   – le déplacement est concaténé à la chaîne de caractères `itineraire`,

   – si le déplacement est vers la droite, alors `j` est incrémenté de 1, – si le déplacement est vers le bas, alors `i` est incrémenté de 1;

- il reste à terminer le chemin en complétant par des déplacements afin d’atteindre la cellule en bas à droite.

6. Écrire les lignes manquantes dans le code ci-dessous. Le nombre de lignes effacées dans le code n’est pas indicatif.

```python
from random import choice
def itineraire_aleatoire(m, n):
	itineraire =''
	i, j = 0, 0
	while i!= m and j!= n
		... # il y a plusieurs lignes
	if i == m:
		itineraire = itineraire +'D'*(n-j)
	if j == n:
		itineraire = itineraire +'B'*(m-i)
	return itineraire
```

Partie C – Calcul du nombre de chemins possibles

Soit 𝑚 et 𝑛 deux entiers naturels non nuls. On se place dans dans le contexte d’un itinéraire de longueur 𝑚 et de largeur 𝑛 de dimension 𝑚 × 𝑛. 

On note `N(m, n)` le nombre de chemins distincts respectant les contraintes de l’exercice.

7. Pour un itinéraire de dimension 1 × 𝑛,  justifier, éventuellement à l’aide d’un exemple, qu’il y a un seul chemin, c’est-à-dire que, quel que soit 𝑛 entier naturel, on a 𝑁(1, 𝑛) = 1.

De même, 𝑁(𝑚, 1) = 1.

8. Justifier que 𝑁(𝑚, 𝑛) = 𝑁(𝑚 − 1, 𝑛) + 𝑁(𝑚, 𝑛 − 1).
9. En utilisant les questions précédentes, écrire une fonction récursive `nombre_chemins(m, n)` qui renvoie le nombre de chemins possibles dans une grille rectangulaire de dimension 𝑚 × 𝑛.

### 