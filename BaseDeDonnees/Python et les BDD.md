# Python et les BDD

Le module `sqlite3` permet comme sur dbrowser de travailler sur les bases de données. 

Nous allons travailler avec la base de données cinema_v2.sqlite que vous avez déjà téléchargé. 

```python
import sqlite3

conn = sqlite3.connect('cinema_v2.sqlite')

cursor = conn.cursor()
cursor.execute("SELECT * FROM Films ")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
```

Ouvrez Thonny, copier-coller ce code et enregistrer au même endroit que la base de données cinema_v2.sqlite.

Exécutez le code. Que se passe-t-il ? 



Explication du code : 

- Connexion à la base de données: `conn = sqlite3.connect('cinema_v2.sqlite')`. 

  Cette ligne ouvre une connexion à la base de données SQLite. Si la base de données n'existe pas, un nouveau fichier de base de données sera créé. 

- Créer un curseur :` cursor = conn.cursor()`

​	Un curseur est utilisé pour exécuter des commandes SQL dans la base de données.

- Exécuter une requête SQL: `cursor.execute("SELECT * FROM Films ")`

  Cette ligne exécute une requête SQL. 

- Récupérer les résultats : `rows = cursor.fetchall()`

  `fetchall()`récupère toutes les lignes de résultats de la requête les stocke dans `rows`. 

- Fermer la connexion: `conn.close()`

  Il est important de fermer la connexion à la base de données une fois que vous avez terminé pour libérer les ressources.

Quelques remarques:

- pour modifier de manière définitive une table de données, il faut utiliser `conn.commit()`

- Pour faire une sélection avec un paramètre, il possible d'utiliser un paramètre extérieur à la requête:

  ```python
  donnees=(1,)
  cursor.execute("SELECT * FROM Films WHERE idFilm = ? ", donnees)
  ```

- Par défaut, les bases de données SQLite ne gèrent pas les contraintes d'intégrité référentielle (foreign key). Pour activer cette fonctionnalité **pour la connexion courante**, vous devez exécuter `PRAGMA foreign_keys = ON` :

  ```python
  conn.execute('PRAGMA foreign_keys = ON')
  ```

A vous de jouer: Pour chaque proposition, écrire la requête SQL correspondante: 

R1 - Listez les titres de film et leurs années de sortie  
R2 - Listez les noms et prénoms des personnes par ordre alphabétique  

R3 - Déterminez l’année et le titre du film le plus récent  
R4 - Calculez le nombre de salles moyen des cinémas  

R5 - Ajoutez le cinéma "Mon salon" avec l'id 4, votre adresse personnelle, 1 salle et 4 fauteuils  

R6 - Supprimez le cinéma “Mon salon” ajouté précédemment ?  

R7 - Déterminez dans quel cinéma (nom et adresse) et à quelle date puis-je visionner le film “Seven”  
R8 - Listez les films (titre, date et genre) proposés par le “CGR Niort” 