# Les bases de données relationnelles. 



Une base de données est un ensemble structuré de fichiers regroupant des informations ayant certains caractères en commun. *D' après le petit Larousse*

Un système de gestion de base de données (SGBD) est le logiciel qui permet à un ordinateur de stocker, récupérer, ajouter, supprimer et modifier des données. Un SGBD gère tous les aspects primaires d'une base de données, y compris la gestion de la manipulation des données, comme l'authentification des utilisateurs, ainsi que l'insertion ou l'extraction des données. Un SGBD définit ce qu'on appelle le schéma de données ou la structure dans laquelle les données sont stockées.



## I. Le modèle relationnel. 

### a. Une problématique actuelle.

Les données et la gestion de ces données sont devenues des enjeux très importants. La quantité de données est gigantesque. Il faut les stocker et les organiser au mieux pour les rendre disponibles. 

En classe de première, nous avions travaillé sur des données structurées stockées dans des fichiers CSV. Cette technique a l'avantage d'être simple et pratique mais présente des limites:

- sécurité et confidentialité inexistantes,
- difficultés pour partager le fichier entre plusieurs utilisateurs en lecture et écriture;
- difficultés à lier plusieurs tables csv entre elles. 

Depuis plusieurs années, l'utilisation de tables de données relationnelles est la solution. Toutefois, la recherche travaille sur des concepts encore plus innovants. 

En 1970, [Edgar Frank Codd]([Edgar Frank Codd — Wikipédia (wikipedia.org)](https://fr.wikipedia.org/wiki/Edgar_Frank_Codd)), surnommé Ted Codd, qui travaillait au laboratoire IBM, propose un modèle logique pour gérer le partage de gros volumes de données. A la base de son modèle se trouvent des notions mathématiques comme le langage ensembliste, les relations et la logique. Le premier système voit le jour dix ans plus tard avec la société Oracle. Edgar Frank Codd a reçu le prix Turing en 1981. 

Le principe est de modéliser des relations entre plusieurs informations et de les ordonner entre elles. 

### b. Les relations. 

Une **base de donnée relationnelle ** est une base de données où l'information est organisée dans des tableaux à deux dimensions appelés de relations ou tables. 

Les lignes de ces relations sont appelées des **enregistrements** (ou n-uplets). 

*Attention, chaque enregistrement est unique: il est interdit d'avoir, dans une relation, deux fois la même ligne.*

Les colonnes sont appelées des **attributs**. 

Chaque case est une **entrée**, aussi appelée valeurs.

Le tableau de la relation a une particularité: on peut intervertir les lignes entre elles ou les colonnes entre elles sans que cela ne change quoi que ce soit à la relation. 

Prenons un exemple: imaginons la base de données relatives à une bibliothèque. 

Soit une table, appelée Livres, répertoriant les livres disponibles à l'emprunt dans cette bibliothèque.

 Chaque livre possède une référence qui lui sert d'identifiant. 

 

| Référence | Titre                                                        | Nom de l'auteur | Prénom de l'auteur | Identifiant_Auteur | Editeur              | Emprunt | Date de retour |
| --------- | ------------------------------------------------------------ | --------------- | ------------------ | ------------------ | -------------------- | ------- | -------------- |
| 1         | Les jours de ton absence                                     | Walsh           | Rosie              | 45                 | Les escales éditions |         |                |
| 2         | Temps glaciaires                                             | Vargas          | Fred               | 174                | Flammarion           | 16      | 02/03/23       |
| 3         | Ce qui reste de nos vies                                     | Shalev          | Zeruya             | 289                | Gallimard            | 23      | 14/05/23       |
| 4         | Culotttes. Des femmes qui ne font que ce qu'elles veulent (Tome 2) | Bagieu          | Pénéloppe          | 2213               | Gallimard BD         |         |                |
| 5         | Le beau mystère                                              | Penny           | Louise             | 458                | Actes Sud            | 453     | 23/04/23       |
| 6         | Une famille délicieuse                                       | Marsh           | Willa              | 1045               | Autrement            |         |                |
| 7         | La beauté des jours                                          | Gallay          | Claudie            | 467                | Actes Sud            | 74      | 14/06/23       |
| 8         | Ne pars pas avant moi                                        | Rouart          | Jean-Marie         | 485                | Gallimard            | 41      | 12/02/23       |
| 9         | L'heure qui les sépare                                       | Matar           | Hisham             | 13                 | Gallimard            |         |                |

Nous avons, dans cet exemple, modélisé les objets livres en identifiant plusieurs attributs qui sont : la référence, le titre, le nom de l'auteur, le prénom de l'auteur,l'identifiant de l'auteur, l'éditeur ainsi que l'identifiant de l'adhérent ayant emprunté ce livre. 

Nous pourrions imaginer d'autres objets à modéliser tel que les adhérents, les DVD, les périodiques, les auteurs de livres....

Les objets disposent d'une multitude de liens entre eux. 

Par exemple, un livre peut être en lien avec un auteur ainsi qu'avec, éventuellement, un adhérent ayant emprunté le livre. 



Modéliser une donnée de façon relationnel revient à penser les données de son application sous forme d’une **multitude d’objets** qui disposent de **relations** permettant de les **lier** ensemble. La modélisation de la base de données amène à la génération d’un **schéma** de la base de données. 

### c. Domaine ###

Chaque attribut prend ses valeurs dans un ensemble appelé **domaine**. 

Un **domaine** peut être:

- les chaînes de caractères: CHAR (chaînes de caractères à taille fixe) oui VARCHAR (chaînes de caractères à taille variable). 
- l'ensemble des nombres entiers ou une partie d'entre eux. Il y a d'ailleurs différents types d'entiers: INT, TINYINT, SMALLINT, LONGINT, ....
- L'ensemble des nombres flottants ou une partie d'entre eux: FLOAT, DECIMAL, REAL..
- Les booléens: BOOL 
- Les champs de type DATE ou TIME pour mesurer le temps. 



Le choix du type conditionne la taille de la base de données. C'est pourquoi les types disponibles sont nombreux. Ils permettent d'optimiser la place nécessaire au stockage. Il n'est pas besoin, par exemple, d'utiliser le type LONGINT pour stocker les numéros des départements français. 

De plus, le choix de domaine doit limiter autant que possible la saisie des valeurs illégales ou mal formées. 

Reprenons notre exempe précédent:

Le domaine de Référence est un entier. 

Le domaine de Titre est une chaîne de caractères. 



### d. Clé primaire (ou Primary Key in english).

Dans une relation, une clé primaire est un attribut, ou un groupe d'attribut, qui identifie de manière unique les valeurs des autres attributs. Elle ne doit pas être NULL (vide), peut être composée d'une ou plusieurs colonnes. 

L'existence d'une clé primaire est une contrainte d'unicité qui permet de vérifier qu'il n'existe pas deux enregistrements identiques dans la base, ce qui est interdit. 

Reprenons notre exemple précédent:

Référence est une clé primaire. C'est la seule possible. 

### e. Clé étrangère  (ou Foreign Key). 

Un attribut d'une relation peut prendre pour valeurs les valeurs d'un attribut, ou d'un groupe d'attributs qui constitue une clé primaire d'une autre relation. Un tel attribut est appelé **clé étrangère**. 

Une clé étrangère fait le lien avec une clé primaire d'une autre table. Ses valeurs doivent pré-exister dans la table qu'elle référence. Elle relie deux tables de manière cohérente. 

Reprenons notre exemple précédent:

Identifiant_Auteur est une clé étrangère. Elle fait référence à l'identifiant de l'auteur du livre. 

Emprunt est une clé étrangère. Elle fait référence à l'identifiant des abonnés de la bibliothèque. 

### f. Schéma relationnel. 

Un **schéma de relation ** précise le nom, les attributs et leurs domaines, la clé primaire et éventuellement la (ou les ) clé (s) étrangère(s) d'une relation. 

Ainsi le schéma de relation de Livres est:

Livres (Référence(PK):INT,  Titre: VARCHAR,  Nom de l'auteur: VARCHAR , Prénom de l'auteur : VARCHAR,Identifiant_Auteur(FK):INT, Editeur: VARCHAR,  Emprunt(FK):INT,   Date de retour: DATE)

Construisons les schéma de relation de Adhérents et de Auteur. 

Adhérents(Identifiant(PK):INT,Nom: VARCHAR,Prenom:VARCHAR,Date de naissance:DATE,Adresse mail: VARCHAR)

Auteur(Identifiant(PK):INT,Nom: VARCHAR, Prenom:VARCHAR)

On appelle **schéma relationnel**  l'ensemble de tous les schémas de relation d'une base de données. 

Graphiquement, on peut représenter le schéma relationnel de notre base ainsi:

![](/BaseDeDonnees/IMG/schéma_relationnel.jpg)



## II. Système de Gestion de Bases de Données.  



Pour accéder à une base de données, on utilise un SGBD, un système de gestion de base de données.  

Un SGBD peut être:

- un logiciel, comme MySQL, fonctionnant avec un serveur. 
- un composant logiciel, comme SQLite qui est une bibliothèque, avec une interface directement intégrable dans un programme.

### a. Fonctionnalités. 

Un SGBD permet d'enregistrer des données, puis de les rechercher, de les modifier et de créer automatiquement des comptes rendus (anglais *report*) du contenu de la base de données. Il permet de spécifier les types de données, la structure des données contenues dans la base de données, ainsi que des règles de cohérence telles que l'absence de redondance. 

Les caractéristiques des données enregistrées dans la base de données, ainsi que les relations, les règles de cohérence et les listes de contrôle d'accès sont enregistrées dans un catalogue qui se trouve à l'intérieur de la base de données et manipulé par le SGBD. 

Les opérations de recherche et de manipulation des données, ainsi que la définition de leurs caractéristiques, des règles de cohérence et des autorisations d'accès peuvent être exprimées sous forme de *requêtes* (anglais *query*) dans un langage informatique reconnu par le SGBD. 

**SQL** est le langage informatique le plus populaire, c'est un langage normalisé de manipulation des bases de données.  Il existe de nombreux autres langages comme le [Databasic](https://fr.wikipedia.org/wiki/Databasic) de [Charles Bachman](https://fr.wikipedia.org/wiki/Charles_Bachman)[9](https://fr.wikipedia.org/wiki/Système_de_gestion_de_base_de_données#cite_note-9), Dataflex, dBase ou xBaseScript, etc.

Les bases de données peuvent être d'une taille de plusieurs téraoctets ; une taille supérieure à la place disponible dans la mémoire centrale de l'ordinateur. Les bases de données sont enregistrées sur disque dur, ces derniers ont une capacité supérieure, mais sont moins rapides, et le SGBD est équipé de mécanismes visant à accélérer les opérations.  Les SGBD contemporains enregistrent non seulement les données, mais également leur description, des formulaires, la définition des comptes rendus, les règles de cohérence, de procédures; ils permettent le stockage de vidéos et d'images. Le SGBD manipule les structures complexes nécessaire à la conservation de ces informations.

Les SGBD sont équipés de mécanismes qui effectuent des vérifications à l'insu de l'utilisateur, en vue d'assurer la réussite des transactions, éviter des problèmes dus aux accès concurrents et assurer la sécurité des données. 



### b. Objectifs. 

- Le système doit assurer la persistance des données. Ceci consiste à garder en mémoire des versions antérieures lorsque des modifications sont effectuées.  
- Le système doit gérer des accès concurrents et la sécurité. Il gère les droits et privilèges d'un utilisateur ou d'un groupe d'utilisateurs sur un ensemble d'objets. 
- Le système doit fournir un accès aux données efficace. Pour cela, il faut disposer d'algorithmes performants. 



## III. Le langage SQL.

SQL ou  » Structured Query Language  » est un langage de programmation permettant de **manipuler les données et les systèmes de bases de données relationnelles**. Ce langage permet principalement de communiquer avec les bases de données afin de gérer les données qu’elles contiennent.

Il permet notamment de stocker, de manipuler et de retrouver ces données. Il est aussi possible **d’effectuer des requêtes**, de mettre à jour les données, de les réorganiser, ou encore de créer et de modifier le schéma et la structure d’un système de base de données et de contrôler l’accès à ses données.

### a. Support.

Nous utiliserons deux supports. 

#### 1. mysql

**MySQL**est un système de gestion de bases de données relationnelles (SGBDR). Il est distribué sous une double licence  GPL et propriétaire. Il fait partie des logiciels de gestion de base de données les plus utilisés au monde autant par le grand public (applications web principalement) que par des professionnels, en concurrence avec Oracle, PostgreSQL et Microsoft SQL Server. 

Pour y accéder au lycée, on utilisera la console MySQL. 

Pour la faire apparaître, il suffit de saisir la commande `mysql`sur votre terminal. 

Cela devrait afficher quelques lignes, mais la dernière doit être:

```
mysql >
```

C'est l'invite de commande mySQL, vous êtes prêt à travailler. 

#### 2. Db browser for SQLite. 

***SQLite***  est une  bibliothèque écrite en langage C qui propose un moteur de base de données relationnelle  accessible par le langage SQL. 

Contrairement aux serveurs de bases de données traditionnels, comme MySQL, sa particularité est de ne pas reproduire le schéma habituel client-serveur mais d'être directement intégrée aux programmes. L'intégralité de la base de données (déclarations, tables, index et données) est stockée dans un fichier indépendant de la plateforme. 

DB Browser for SQLite est un logiciel gratuit et libre permettant de créer et de manipluer des bases de données sans avoir besoin d'un serveur. 

Pour le télécharger chez vous, vous pouvez utiliser le lien suivant: https://sqlitebrowser.org

#### 3. le module sqlite3 en python. 

Le module `sqlite3` permet de travailler avec les bases de données et le langage SQL en passant par python. 

### b. Les requêtes en écriture. 

Afin de mettre à jour la base de données on peut réaliser des **requêtes**.

#### Requête INSERT INTO

L’**ajout de nouvelles données** dans une table s’effectue avec une requête `INSERT INTO` dont voici le modèle :

```sql
------------------------------------------------------
INSERT INTO TableName (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
------------------------------------------------------
```

Exemples :

```sql
-- Ajout en fournissant toutes les données
INSERT INTO Clients
VALUES (7, 'SHOWKANAPE', 'Ophélie', 23, 'Niort');
-- Ajout en sélectionnant les colonnes concernées
INSERT INTO Clients (nom, prenom)
VALUES ('SHOWKANAPE', 'Ophélie');
```

Remarque : la clef primaire est rarement renseignée car elle est très souvent configurée pour s’auto-incrémenter automatiquement

#### Requête UPDATE

La **mise à jour** de données existantes dans une table s’effectue avec une requête UPDATE dont voici le modèle :

```sql
--------------------------------------------
UPDATE TableName
SET column1 = value1, column2 = value2, ...
WHERE condition;
--------------------------------------------
```

Exemples :

```sql
-- Modification de l'âge
UPDATE Clients
SET age = 25
WHERE id_client = 7;
-- Modification de l'âge et du prénom
UPDATE Clients
SET age = 25, prenom = 'Ofely'
WHERE id_client = 7;
```

#### Requête DELETE

La **suppression de données existantes** dans une table s’effectue avec une requête DELETE dont voici le modèle :

```sql
----------------------
DELETE FROM TableName
WHERE condition;
----------------------
```

Exemples :

```sql
-- Suppression d'un client
DELETE FROM Clients
WHERE id_client = 7;
```

### c. Les requêtes d’interrogation (SELECT, FROM, WHERE)

> définition : La **sélection des données **dans une table s’effectue avec une requête `SELECT` dont voici le modèle. La clause WHERE est optionnelle.

```sql
----------------------------
SELECT column1, column2, ...
FROM TableName
WHERE condition;
----------------------------
```

Exemples :

```sql
-- Sélection des noms et prénoms de tous les clients
SELECT nom, prenom
FROM Clients;
-- Sélection de tous les attributs de tous les clients
SELECT *
FROM Clients;
-- Sélection du nom de tous les clients niortais
SELECT nom
FROM Clients
WHERE ville = 'Niort';
-- Sélection du nom et age des "jeunes" clients niortais
SELECT nom, age
FROM Clients
WHERE ville = 'Niort'
AND age < 30;
```



Parfois une colonne peut contenir des valeurs identiques qu’on pourra filtrer en ajoutant le mot clef `DISTINCT` juste après `SELECT` :

```sql
-- On ne sélectionne que les villes distinctes
SELECT DISTINCT ville
FROM Clients;
```

Souvent, on souhaite récupérer les données d’une table classées selon un certain ordre. Le mot clef `ORDER BY` pourra alors être ajouté à la fin de la requête `SELECT` :

```sql
-- Sélection des clients du plus vieux plus jeune
SELECT nom, prenom, age
FROM Clients
ORDER BY age DESC;
-- Sélection des clients par ordre alphabétique
SELECT nom, prenom, age
FROM Clients
ORDER BY nom ASC;
```

Il existe également des fonctions d’agrégation (**AVG, MIN, MAX, SUM, COUNT**) permettant d’effectuer différents calculs statistiques sur un ensemble d’enregistrements :

```sql
-- Calcul de l'âge moyen de tous les clients
SELECT AVG(age)
FROM Clients;
-- Qui est le plus jeune client ?
SELECT nom, prenom, MIN(age)
FROM Clients;
-- Où habite le plus vieux client ?
SELECT ville, MAX(age)
FROM Clients;
-- Quel est l'âge cumulé de tous les clients ?
SELECT SUM(age)
FROM Clients;
-- Combien y a-t-il de clients à Niort ?
SELECT COUNT(id_client)
FROM Clients
WHERE ville = 'Niort';
```

 *Remarque* : il vaut mieux sous-traiter les calculs au SGBD plutôt que les faire soit même en Python, c’est plus simple et le SGBD le fait en général plus efficacement.

Quand on souhaite limiter le nombre de lignes dans les résultats, on peut utiliser `LIMIT` comme ici :

```sql
-- On limite à 3 lignes les résultats
SELECT nom, prenom
FROM Clients
LIMIT 3;
```

Les recherches impliquant des chaînes de caractères sont plus aisées avec `LIKE` car on peut lui associer des filtres

```sql
-- Recherche des noms comme Axxxxx
SELECT nom
FROM Clients
WHERE nom LIKE 'A%';
-- Recherche des noms comme xDxxxxxx
SELECT nom
FROM Clients
WHERE nom LIKE '_D%';
```

 *Remarque* : on peut également utiliser l’opérateur OR et les parenthèses pour construire des clauses WHERE plus sophistiquées

### d. Requêtes avec jointures (JOIN)

> définition : Les **jointures** comme le nom l’indique permettent de joindre les données issues de 2 tables différentes.
>  Les jointures utilisent les **clefs primaires et étrangères** pour réaliser la relation entre les 2 tables.

```sql
---------------------------------------------------
SELECT TableName1.column3, TableName2.column5, ...
FROM TableName1
INNER JOIN TableName2
ON TableName1.column2 = TableName2.column1;
---------------------------------------------------
Exemple :
-- Affiche qui a emprunté quoi
SELECT Clients.nom, Clients.prenom, Livres.nom
FROM Clients
INNER JOIN Livres
ON Clients.id_client = Livres.id_client_fk;
-- Affiche les livres empruntés par BIJOBA Jo
SELECT Livres.nom
FROM Clients
INNER JOIN Livres
ON Clients.id_client = Livres.id_client_fk
WHERE Clients.nom = 'BIJOBA';
```

 *Remarque1* : 

- pour éviter les conflits de nom de colonne, il est préférable d’ajouter en *préfixe le nom de la table*.

- les mots `WHERE`, `DISTINCT`, `AVG`, `MIN`, `MAX`, `SUM`, `COUNT`, `LIMIT` et `LIKE` sont utilisables également avec les jointures.

- il existe plusieurs types de jointures INNER, LEFT, RIGHT, FULL... mais c’est la jointure INNER qui est la plus utilisée et au programme en NSI.

  ![](/BaseDeDonnees/IMG/inner.png)

### e. Contraintes d’intégrité. 

Nous avons évoqué les contraintes d’intégrité que l’on pouvait ajouter pour rendre les données plus cohérentes et robustes. Ces contraintes peuvent être ajoutées lors de la création des tables. La plupart des outils graphiques proposent une méthode simple pour le faire. Dans ce qui suit, on observera comment cela est possible avec le langage SQL.

#### 1. Contrainte de domaine

Ce premier exemple propose une création de table avec le choix pour chaque attribut d’un domaine ou type particulier ainsi que de vérifications plus spécifiques avec le mot clef `CHECK`

```sql
-- Choix des domaines pour les attributs de la table Clients
CREATE TABLE "Clients" (
"nom" TEXT,
"prenom" TEXT,
"age" INTEGER,
"ville" TEXT
);
```

On peut aussi y ajouter des vérifications plus spécifiques avec le mot clef `CHECK` et des **conditions** :

```sql
-- Choix des domaines pour les attributs de la table Clients
CREATE TABLE "Clients" (
"nom" TEXT,
"prenom" TEXT CHECK(length(prenom) <= 30),
"age" INTEGER CHECK(age>0 AND age<200),
"ville" TEXT CHECK(ville IN ('Niort', 'Aiffres'))
);
---
```

📝 A noter que les domaines/types proposés varient d’un SGBD à l’autre. Se référer à la documentation technique du SGBD pour en connaître les détails.

#### 2. Contrainte de relation

Afin de rendre chaque enregistrement unique, on ajoute une **clef primaire** id_client de type `INTEGER` avec les mots-clefs `PRIMARY KEY`.

Le paramétrage `AUTOINCREMENT` permet d’auto-incrémenter la valeur de chaque enregistrement à chaque requête `INSERT INTO` sans avoir à se soucier des valeurs déjà dans la table.

```sql
CREATE TABLE "Clients" (
"id_client" INTEGER PRIMARY KEY AUTOINCREMENT,
"nom" TEXT,
"prenom" TEXT,
"age" INTEGER CHECK(age>0 AND age<200),
"ville" TEXT CHECK(ville IN ('Niort','Aiffres'))
);
```

#### 3. Contrainte de référence

La contrainte de référence se fera en ajoutant une **clef étrangère** dans la table Livres référençant la clef primaire de la table Clients. Les mots-clefs FOREIGN KEY et REFERENCES sont alors utilisés :

```sql
-- Table Livres avec tous ses attributs
CREATE TABLE "Livres" (
"id_livre" INTEGER PRIMARY KEY AUTOINCREMENT,
"nom" TEXT,
"prix" REAL,
"id_client_fk" INTEGER,
FOREIGN KEY("id_client_fk") REFERENCES "Clients"("id_client")
);
```
