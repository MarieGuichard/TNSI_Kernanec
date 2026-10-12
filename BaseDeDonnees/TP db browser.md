# Introduction  

## Objectifs  

Ce travaux pratiques ont pour objectif de vous faire découvrir les principales notions vues en cours autour des bases de données.
* modèle relationnel
* SGBD 

Ce TP se réalisera avec  DB Browser for SQLite (outil graphique)



## I. Préparation
- Téléchargez la base de données cinema_v1.sqlite.

- Ouvrir cette base de données avec le logiciel __DB Browser for SQLite__.
  Ce logiciel va vous permettre de gérer cette base de données au travers de 3 onglets :

  - __Structure de la base de données__ : Permet d’afficher et de modifier la structure des tables de la base de données . 

  - __Parcourir les données__ : Permet d’afficher et de modifier les données dans chacune des tables

  - __Exécuter le SQL__ : Permet d’exécuter une requête SQL et voir le résultat

     

## II. Schéma relationnel  
Voici le schéma relationnel de la base de données:
![base de donnees cinéma](/BaseDeDonnees/IMG/bdd_cine_1_annote.png)

a. Reconnaître et nommer les éléments du schéma relationnel : 

|Eléments|Description|
|:---:|:---:|
|1||
|2||
|3||
|4||
|5||
|6||
|7||

b. Ré-écrire le schéma relationnel ci-dessus dans une version textuelle.



##  III. Contraintes d’intégrité  

### Contraintes de domaine  

a. En utilisant le schéma relationnel et le logiciel DB Browser for SQLite, listez dans le tableau ci-dessous les contraintes de domaines de la table Films.  

1. onglet “Structure de la base de données”
2. sélectionner la table “Films”
3. cliquer sur le bouton “Modifier la table”
On s’intéressera notamment aux types utilisés ainsi qu’aux vérifications complémentaires (avec CHECK).

|Attribut|Type|Vérification|
|:---|:---:|:---:|
|idFilm|||
|idRealisateur|||
|titre|||
|genre|||
|annee|||

b. Pourquoi avoir choisi cette contrainte de domaine pour l’attribut “annee” ?  

c.  Dans le logiciel DB Browser for SQLite, essayez de modifier l’année du film “Arnaque, crime et botanique” avec une valeur impossible comme 1515.

1. choisir l’onglet “Parcourir les données”
2. sélectionner la table “Films” dans la liste déroulante
3. cliquer dans la case “annee” de l’enregistrement
4. modifier la valeur pour 1515  
Que se passe-t-il ?

d.  A votre tour modifiez la table Films pour y ajouter la contrainte de domaine
suivante pour le titre : type TEXT d’une longueur inférieure ou égale à 50.  

1. cliquer sur l’onglet “Structure de la base de données”
2. cliquer droit sur la table “Films” puis “Modifier une table”
3. cliquer sur la ligne “titre”, colonne “Vérifiier”
4. ajouter ce qu’il faut
5. cliquer sur le bouton “OK” pour enregistrer

Comme à l’étape précédente, testez de modifier un titre avec une longueur 
impossible.

### Contraintes de relation  

a.  Comment a-t-on assuré l’unicité de chaque enregistrement (ou n-uplet) de
la table “Films” ?

b.  Via l’onglet “Parcourir les données” tentez de modifier l’enregistrement “Into the Wild” avec idFilm=9. Que se passe-t-il ? Est-ce normal ?  



c.  Comment a-t-on assuré l’unicité de chaque enregistrement (ou n-uplet) de
la table “Jouer” ? Quelle critique pourrait-on faire à ce choix ?  



d.  Finalement on décide d’ajouter “role” à “idActeur” et “idFilm” pour constituer la clef primaire de la relation  
![jouer](/BaseDeDonnees/IMG/role.png)



### Contraintes de référence

a.  Essayez via l’onglet “Parcourir les données” de repérer qui a réalisé les films “Mystic River” et “L’armée des 12 singes”.  

b. Quel rôle a joué Bruce WILLIS dans l’armée des 12 singes ?

c.  Que se passe-t-il si vous essayez de supprimer Bruce WILLIS de la table “Personnes” ?
1. onglet “Parcourir les données”
2. sélectionner la ligne avec “Bruce WILLIS”
3. cliquer sur le bouton “Supprimer l’enregistrement”
Pourquoi obtient-on cette erreur et comment y remédier ?  



d.  Pour pouvoir supprimer l’enregistrement Bruce WILLIS de la table
Personnes, il faut au préalable supprimer toutes les références à cet
enregistrement dans les autres tables.

1. supprimer l’enregistrement (24, 7, ‘James Cole’) de la table Jouer
2. supprimer l’enregistrement (24, ‘Willis’, ‘Bruce’) de la table Personnes

e.  En observant les données de la table “Films“ , essayez de repérer une
redondance de données. Proposez une amélioration du modèle relationnel en
utilisant une contrainte de référence pour éviter cette redondance de
données.

f.  Finalement on décide de “sortir” le genre dans une nouvelle table “Genres”
et d’ajouter une clef étrangère Films.idGenre référençant la clef primaire
Genres.idGenre


![](/BaseDeDonnees/IMG/film_genre.png)

![](BaseDeDonnees/IMG/cont_ref.png)

## Relations entre les tables

a.  Précisez le type de chacune des relations ci-dessous (one-to-one, one-tomany
ou many-to-many) :

|Table| Type de relation|
|:---|:---|
|Films —?— Genres||
|Films —?— Cinemas||
|Films —?— Personnes (pour les réalisateurs)||
|Films —?— Personnes (pour les acteurs)||

b. En utilisant le logiciel DB Browser for SQLite, ajoutez votre film préféré dans cette base de données. Il faudra impérativement utiliser et modifier les
tables : Films, Jouer, Personnes et Projeter.

* source : cours NSI Lycée Saint André Niort  A MAROT D SALLÉ J SIMONNEAU  
