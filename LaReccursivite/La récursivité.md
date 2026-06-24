### La récursivité. 



### I. Un exemple.



Une fonction récursive est une fonction qui s'appelle elle-même. 



Voici un exemple classique :

```python
def expo(a,n):
	if n == 0:
		return 1
	else:
		return a*expo(a,n-1)
```



Faisons tourner avec les valeurs a=2 et n=4. 

expo(2,4) = 2 * expo(2,3) = 2* 2 * expo(2,2)=2 * 2 * 2 * expo(2,1)=2 * 2 * 2 * 2 *1=16. 



Cette fonction implémente, de façon récursive, le calcul de $a^{n}$ en utilisant le fait que $a \times a^{n-1}=a^{n}$ et $a^0=1$



On remarque que la fonction commence par une condition d'arrêt qui traite le cas de base. 



### II. Pile d’exécution.

  

Lors de l'appel d'une fonction récursive, on utilise, en interne, une structure de pile (nous reverrons ce concept un peu plus tard). 



Une pile fonctionne comme un empilement d'objets (une pile d'assiettes par exemple) : on peut empiler un objet en haut de la pile et enlever  le sommet de la pile (on parle alors de dépiler), mais on ne peut pas accéder à un objet qui n'est pas en haut de la pile. 



La pile utilisée, appelée pile d'exécution, est de taille limitée. Au delà d'un certain nombre d'appels récursifs, 1000 par défaut avec Python, il y a une erreur de dépassement de taille  (stack overflow). 

Cette pile contient une trace de tous les appels de fonction qui ne sont pas encore terminés.



Écrivons cette pile d’exécution pour notre exemple :

- étape 1 : empiler.  

  expo(2,4)

- étape 2 : empiler.  

  expo(2,3)

  expo(2,4)

- étape 3 :  empiler.  

  expo(2,2)

  expo(2,3)

  expo(2,4)

- étape 4 :  empiler.  

  expo(2,1)

  expo(2,2)

  expo(2,3)

  expo(2,4)

- étape 5 :  empiler.  

  expo(2,0)=1

  expo(2,1)

  expo(2,2)

  expo(2,3)

  expo(2,4)

- étape 6 : dépiler

  expo(2,1) = 2

  expo(2,2)

  expo(2,3)

  expo(2,4)

- étape 7 :dépiler

  expo(2,2) =4

  expo(2,3)

  expo(2,4)

- étape 8 :dépiler

  expo(2,3) =8

  expo(2,4)

- étape 9 :dépiler

  expo(2,4)=16



### III. Écriture.

​	Une fonction récursive simple s'écrit sous la forme :

```python
def fonction(arguments):
	if condition d'arrêt:
    	return valeur
    else: 
        appel récursif
```

​	Pour écrire une fonction récursive, on doit :

- déterminer le type de données à renvoyer,
- déterminer pour quelle(s) valeur(s) de l'argument le problème est résolu et on écrit la condition d'arrêt,
- déterminer de quelle manière la taille du problème est réduite (argument entier qui 	décroît strictement, liste dont la taille diminue, …)
- écrire l'appel récursif en prenant garde à ce que le type de données qu'il 	renvoie soit cohérent avec celui renvoyé par la condition d'arrêt.  	



​	La méthode récursive est plus élégante et lisible et elle évite d'utiliser de nombreuses 	structures itératives. De plus, elle est également utile pour concevoir des algorithmes sur des 	structures de données complexes comme les listes, les arbres ou les graphes. 



​	Toutefois, elle est très gourmande en ressource mémoire. 



