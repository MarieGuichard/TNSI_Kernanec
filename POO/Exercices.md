# Exercices: POO
#### Exercice 1 : 

On définit une classe gérant une adresse IPv4. On rappelle qu’une adresse IPv4 est une adresse de longueur 4 octets, notée en décimale à point, en séparant chacun des octets par un point. 

On considère un réseau privé avec une plage d’adresses IP de 192.168.0.0 à 192.168.0.255. 

On considère que les adresses IP saisies sont valides. 

Les adresses IP 192.168.0.0 et 192.168.0.255 sont des adresses réservées. 

Le code ci-dessous implémente la classe AdresseIP. 

```python
class AdresseIP():
    def __init__(self, adresse):
        self.adresse = ...........
        
    def liste_octet(self):
        '''renvoie une liste de nombre entiers,
        la liste des octets de l'adresse IP'''
        return [int(i) for i in self.adresse.split(".")]
    
    def est_reservee(self):
        ''' renvoie True si l'adresse IP est une adresse réservée,
        False sinon'''
        return ...... or .......
    
    def adresse_suivante(self):
        ''' renvoie un objet de AdresseIP avec l'adresse IP qui suit l'adresse self
        si elle existe, et False sinon '''
        if ..... <254:
            octet_nouveau = .... + .....
            return AdresseIP('192.168.0.'+ ....)
        else:
            return False
```


Vous trouverez le code dans le fichier adresseIP.py

Compléter le code ci-dessus et instancier trois objets : adresse1, adresse2, adresse3 avec respectivement les arguments suivants : '192.168.0.1', '192.168.0.2', '192.168.0.0' 



Vérifier que : 

\>>> adresse1.est_reservee() 

False 

\>>> adresse3.est_reservee() 

True

 \>>> adresse2.adresse_suivante().adresse 

'192.168.0.3'

####  Exercice 2 : 

Considérons le plan muni d'un repère orthonormé, chaque point est repéré par deux nombres que nous appelons abscisse et ordonnée. 

Nous 

1. Implémenter le type abstrait Point de trois façons différentes :

- par un tuple

- par un dictionnaire

- par une classe d'objets.  

2. Comparer le code nécessaire pour créer un nouveau point, changer l'une de ses coordonnées et calculer la distance entre deux points.


#### Exercice 3: 

1. Définir une classe Voiture ayant les attributs suivants, avec les valeurs par défaut, indiquées.

`marque = 'Ford', couleur = 'rouge', pilote='personne', vitesse = 0`. 

2. Ajouter une méthode choix_conducteur(nom) qui permettra de désigner (ou changer) le nom du conducteur.

3. Ajouter une méthode `accelerer(taux,duree)` qui permettra de faire varier la vitesse de la voiture. La variation de vitesse obtenue sera égale au produit : taux*duree.  

   Par exemple, si la voiture accélère aux taux de 1,3m/s pendant 20 secondes, son gain de vitesse doit être égal à 26 m/s. Des taux négatifs seront acceptés (ce qui permet de décélérer). La variation de vitesse ne sera pas autorisée si le conducteur est 'personne'.  

4. Ajouter une méthode `affiche_tout()` qui permettra de faire apparaître les propriétés présentes de la voiture.  



Exemples d'utilisation de cette classe :

![](/POO/img/utilisationvoiture.jpg)






#### Exercice 4 : 

1. Définir une classe Carte qui représente une carte à jouer, définie par sa valeur (1 à 13) et sa couleur (pique, cœur, carreau, trèfle).  

2.  Ajouter une méthode nom qui retourne le nom de la carte, par exemple « Dame de Pique ».  

3.  Définir une classe Paquet qui contient les cartes d'un jeu de 52 cartes.

4.  Dans la classe Paquet, ajouter une méthode tirer qui tire une carte au hasard et retourne son nom.  

   

#### Exercice 5: 

1. Définir une classe Personne avec pour attributs le nom et le prénom de la personne.  
2. Définir une Amis avec pour attributs deux personnes et une méthode ami qui prend une personne p en paramètre et retourne l'autre personne si p est l'un des deux amis, ou None sinon.  
3. Définir une classe Groupe avec deux attributs, une liste de personnes et une liste d'amis, et deux méthodes, l'une pour ajouter une personne et l'autre pour déclarer deux personnes amies. On s'assurera que les deux personnes font bien partis du groupe.
4. Ajouter une méthode qui permet de lister les amis d'une personne.  





### Exercice 6 type bac.

Cryptage selon le « Code de César »  

Dans cet exercice, on étudie une méthode de chiffrement de chaînes de caractères  alphabétiques. 

Pour des raisons historiques, cette méthode de chiffrement est appelée  "code de César". On considère que les messages ne contiennent que les lettres  capitales de l’alphabet "ABCDEFGHIJKLMNOPQRSTUVWXYZ" et la méthode de  chiffrement utilise un nombre entier fixé appelé la clé de chiffrement.  

1. Soit la classe `CodeCesar` définie ci-dessous :  

   ```
   class CodeCesar:  
   	def __init__(self, cle):  
   		self.cle = cle  
   		self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
   		
   	def decale(self, lettre):  
   		num1 = self.alphabet.find(lettre)  
   		num2 = num1+self.cle  
   		if num2 >= 26:  
   			num2 = num2-26  
   		if num2 < 0:  
   			num2 = num2+26  
   		nouvelle_lettre = self.alphabet[num2]  
   		return nouvelle_lettre   
   ```

   

   ​	On rappelle que la méthode `str.find(lettre)` renvoie l'indice (index) de la  `lettre` 		dans la chaîne de caractères `str`

    	Représenter le résultat d’exécution du code Python suivant : 

   ```
   code1 = CodeCesar(3)  
   print(code1.decale('A'))  
   print(code1.decale('X'))  
   ```

    

2. La méthode de chiffrement du « code César » consiste à décaler les lettres du  message dans l’alphabet d'un nombre de rangs fixé par la clé. Par exemple,  avec la clé 3, toutes les lettres sont décalées de 3 rangs vers la droite : le A  devient le D, le B devient le E, etc.   

       Ajouter une méthode `cryptage(self, texte)` dans la classe` CodeCesar` définie  à la question précédente, qui reçoit en paramètre une chaîne de caractères (le  message à crypter) et qui retourne une chaîne de caractères (le message  crypté).  

      Cette méthode `cryptage(self, texte)` doit crypter la chaîne texte avec la clé  de l'objet de la classe `CodeCesar` qui a été instancié. 

      Exemple :

      ```
      >>>code1 = CodeCesar(3)  
      >>> code1.cryptage("NSI")  
      'QVL'  
      ```

      

3. Ecrire un programme qui : 

      - demande de saisir la clé de chiffrement

      - crée un objet de classe ` CodeCesar` 

      -  demande de saisir le texte à chiffrer  

      -  affiche le texte chiffré en appelant la méthode `cryptage`

        

4. On ajoute la méthode ` transforme(texte)` à la classe ` CodeCesar` :  

      ```
      def transforme(self, texte):  
      	self.cle = -self.cle  
      	message = self.cryptage(texte)  
      	self.cle = -self.cle  
      	return message
      ```

      On exécute la ligne suivante : `print(CodeCesar(10).transforme("PSX"))`

       Que va-t-il s’afficher ? Expliquer votre réponse.

   ### Exercice 7 type bac:
La société LOCAVACANCES doit gérer la réservation de l’ensemble des chambres de 
ses gîtes. Chaque chambre d’un même complexe sera différenciée par son nom. 
Pour cela, d’un point de vue informatique, on a créé deux classes : Chambre et Gite
dont le code est donné ci-dessous. 
   ```python
class Chambre:

    def __init__(self, nom: str): 
       self._nom = nom 
       self._occupation = [False for i in range(365)]

    def get_nom(self): 
       return self._nom 
 
    def get_occupation(self): 
       return self._occupation 
 
    def reserver(self, date: int): 
       self._occupation[date - 1] = True 

class Gite:
    def __init__(self, nom: str): 
       self._nom = nom 
       self._chambres = [] 
 
    def __str__(self): 
       n = len(self._chambres) 
       if n == 0: 
          return "L'hôtel " + self._nom + " n’a aucune chambre."
       else: 
          return "L’hôtel " + self._nom + " a " + str(n) + " chambre(s)" 
 
    def get_chambres(self): 
          return self._chambres 
 
    def get_nchambres(self): 
          return [ch.get_nom() for ch in self._chambres] 
 
    def ajouter_chambres(self, nom_ch : str): 
          self._chambres.append(Chambre(nom_ch)) 
 
    def mystere(self, date): 
          l_ch = [] 
          for ch in self._chambres : 
               if ch.get_occupation()[date - 1] == False : 
                   l_ch.append(ch.get_nom()
           return(l_ch)
```
Partie A - Étude de la classe `Chambre` : 

1. Lister les attributs en donnant leur type. Préciser s’ils sont modifiables dans la
classe, en explicitant la méthode associée.
2. Écrire un `assert` dans la méthode reserver pour vérifier si le nombre date
passé en paramètre est bien compris entre 1 et 365 (on ne gère pas les années
bissextiles).
3. Écrire la méthode `AnnulerReserver(self, date : int`) qui annule la
réservation pour le jour `date`.

Partie B - Étude de la classe `Gite` : 

Le gîte « BonneNuit » a 5 chambres dénommées 
'Ch1', 'Ch2', 'Ch3', 'Ch4', 'Ch5'

On définit l’objet `GiteBN` par l’instruction : `GiteBN = Gite("BonneNuit")`. 

1. Méthode `ajouter_chambres()`
Écrire l’instruction Python pour ajouter 'Ch1' à l’objet `GiteBN`.

Dans les questions suivantes 2, 3 et 4, on considère que l’objet GiteBN contient toutes
les chambres du gite « BonneNuit ». 

2. La méthode `ajouter_chambres` permet d’enregistrer une nouvelle chambre,
mais elle ne teste pas si le nom de cette chambre existe déjà.
Modifier la méthode pour éviter cet éventuel doublon.

3. Étude des méthodes : `get_chambres()` et `get_nchambres()`

   a.  Parmi les 4 propositions ci-dessous, quel est le type renvoyé par l’instruction
Python : `GiteBN.get_chambres()`
   - String
   - Objet Chambre
   - Tableau de String
   - Tableau d'objet Chambre

   b. Qu'affiche la suite d'instructions suivante? 
   ```python
   Ch = BiteBN.get_chambres()[1]
   print(Ch.get_nom())
   ```
   c. Quelle différence existe-t-il entre les deux méthodes `get_nchambres()`et `get_chambres()`? 

4. Les chambres 'Ch1', 'Ch3', 'Ch5' sont réservées pour tout le mois de Janvier
2021. La méthode `mystère` étant précisée ci-dessus, répondre
aux questions suivantes :


   a. Que va renvoyer l’instruction `GiteBN.mystere(3)` ?
   
   b. Dans la méthode `mystère`, quel est type des variables en paramètre et en
sortie ?
   c. Quelles sont les méthodes ou attributs dont elle a besoin ?
