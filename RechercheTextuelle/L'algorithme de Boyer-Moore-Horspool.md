# L'algorithme de Boyer-Moore-Horspool. 

Nous verrons ici l'algorithme de Boyer-Moore-Horspool qui est une simplification (moins efficace) de l'algorithme de Boyer-Moore, mais qui est beaucoup plus aisé à coder. 

En effet, l'algorithme de Boyer Moore utilise deux tables de décalage, alors que celui de Horspool  n'en utilise qu'une seule. 

Prenons un exemple: 

Considérons la chaine TATBADGEABCTAGAAGTGATAG et le motif TAG. 

La première étape de l'algorithme de  Horspool consiste à établir une table de décalage. 

Pour notre exemple, la première étape consiste à aligner les deux chaines et à regarder ce qui se passe pour la dernière lettre

```
TATBADGEABCTAGAAGTGATAG
TAG
```

La lettre T ne corrrespond pas à la lettre G, il faut maintenant décaler. 

Comme le T est dans le motif, il s'agit de décaler pour aligner les T. Le décalage est de 2

```
TATBADGEABCTAGAAGTGATAG
  TAG
```

La lettre A ne correspond pas à la lettre G, il faut maintenant décaler. 

Comme le A est dans le motif, il s'agit de décaler pour aligner les A. Le décalage est de 1. 

```
TATBADGEABCTAGAAGTGATAG
   TAG
```



1. Etablir le dictionnaire correspondant aux décalages du motif "STOP". Appeler votre enseignante. 

2. Compléter de la fonction `decalage(motif)`dans le fichier Horspoole.py

3. Compléter la fonction `horspool(chaine,motif)`. 

   Vous utiliserez la méthode `get()`qui renvoie une valeur par défaut dans le cas où la clé recherchée dans un dictionnaire est absente. 

4. Pour aller plus loin:

   1. Modifiez la fonction `horspool(mot, chaine, debut)` pour pouvoir reprendre la recherche à partir d'une position `debut` quelconque.

   ```python
   chaine = "TCTAGCAGTAGACT"
   mot = "TAG"
   >>> horspool(mot, chaine, 0)
   2
   >>> horspool(mot, chaine, 3)
   8
   >>> horspool(mot, chaine, 9)
   -1
   ```

   

   1. Créez une fonction `getPositions(mot, chaine)` qui renvoie la liste de toutes les positions de la chaîne mot dans la chaîne de caractères chaine, en utilisant la fonction horspool().

   ```python
   >>> getPositions("TAG", "TAGCTAGCAGTAGACT")
   [0, 4, 10]
   >>> getPositions("X", "X-XX-X")
   [0, 2, 3, 5]
   >>> getPositions("abcd", "abcecbcdadabc")
   []
   ```




