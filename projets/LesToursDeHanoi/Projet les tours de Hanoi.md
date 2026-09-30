# Projet: les tours de Hanoi. 



**Les tours de Hanoï** sont un jeu de réflexion imaginé par le mathématicien français Edouard Lucas  consistant à déplacer des disques de diamètres différents d'une tour de « départ » à une tour d'« arrivée » en passant par une tour « intermédiaire », et ceci en un minimum de coups, tout en respectant les règles suivantes :

- on ne peut déplacer plus d'un disque à la fois ;
- on ne peut placer un disque que sur un autre disque plus grand que lui ou sur un emplacement vide.

On suppose que cette dernière règle est également respectée dans la configuration de départ.

![](/projets/LesToursDeHanoi/IMG/imagetourdehanoi.jpg)



1. Aller résoudre le casse-tête des tours de Hanoi avec 3,4 et 5 disques. 

   [les tours de Hanoi](http://championmath.free.fr/tourhanoi.htm)

L'objectif de ce projet est de coder une résolution du casse-tête des tours de Hanoi. 

2. Nous utiliserons un algorithme récursif pour déplacer les n tours de la tour de départ, vers la tour de destination en utilisant la tour intermédiaire. 

   Considérons une situation où la tour de départ compte n disques à déplacer vers la tour de destination. 

   ![](/projets/LesToursDeHanoi/IMG/algorec.jpg)

​	a. Quelle est la situation de base ? 

​	b. Dans le cas où l'on n'est pas dans la situation de base, quels sont les mouvements à effectuer? 

​	c. Ecrire l'algorithme permettant la résolution du probléme et **appeler votre professeur**. 

3. Implémentation des tours de Hanoi. 

   Nous travaillerons avec une classe Hanoi qui prendra pour attribut `nb_disques`le nombre de disques sur la tour de départ et un attribut représentant les tours. 

   a. Quelle structure de données semble la plus pertinente pour représenter une tour? Expliquer pourquoi et **appeler votre professeur**. 

   b. Implémenter la classe `Hanoi`. Celle-ci, en plus de la méthode `init`, devra avoir une méthode permettant d'afficher le contenu des tours de la façon suivante: 

![](/projets/LesToursDeHanoi/IMG/affichagetours.jpg)

4. Résolution du problème. 

   a. Implémenter la fonction `deplacer(mestours,nb_disques,depart,destination,intermediaire)`où `mestours`est un objet type `Hanoi`, `nb_disques`est le nombre de disques à déplacer, `depart`indique la tour où se trouvent les disques à déplacer, `destination`indique la tour où doivent se trouver les disques à la fin, et `intermediaire`la tour intermédiaire. 

   b. Implémenter la fonction `afficher_coup(mestours,depart,destination)`permettant une affichage du type:

   ![](/projets/LesToursDeHanoi/IMG/affichagetour.jpg)

​	c. Implémenter la fonction `resoudre(nb_disques)`permettant d'initialiser la situation de départ et de 		lancer la résolution en générant un affichage. 

5. Pour aller plus loin, vous pouvez....

   a. Proposer une résolution manuelle (en indiquant au joueur lorsqu'il ne déplace pas correctement un disque). 

   b. Faire une jolie interface graphique en utilisant `pygame`ou `tkinter`.


**Evidemment, vous n'oublierez ni les docstrings, ni les commentaires**





