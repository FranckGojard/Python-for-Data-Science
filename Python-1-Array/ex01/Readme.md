# Exercice 01 - 2D array

## Sujet

Le but de cet exercice est d'ecrire une fonction qui recoit un tableau a deux
dimensions (une liste de listes), affiche sa forme, puis renvoie une version
coupee du tableau entre `start` et `end`.

Fichier a rendre :

- `array2D.py`

Prototype impose :

```python
def slice_me(family: list, start: int, end: int) -> list:
```

Le sujet impose d'utiliser le slicing et de gerer les cas d'erreur.

## Donnees de depart

Le fichier `tester.py` du sujet :

```python
from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
```

Resultat attendu :

```text
My shape is : (4, 2)
My new shape is : (2, 2)
[[1.8, 78.4], [2.15, 102.7]]
My shape is : (4, 2)
My new shape is : (1, 2)
[[2.15, 102.7]]
```

## Notions Apprises

- Une liste de listes represente un tableau a deux dimensions : chaque element
  est une ligne.
- La forme (`shape`) d'un tableau s'ecrit `(lignes, colonnes)`.
- `np.array(...)` transforme une liste en tableau numpy.
- `.shape` est une propriete (sans parentheses) qui donne la forme.
- Le slicing `liste[debut:fin]` garde les elements de `debut` jusqu'a `fin`
  **exclu**.
- Un indice negatif compte depuis la fin : `-1` est le dernier, `-2` l'avant-dernier.
- Le slicing ne plante pas si `fin` depasse la taille du tableau.
- `tableau[1]` donne une ligne, `tableau[1:2]` donne une liste contenant une
  ligne (deux crochets).
- `.tolist()` convertit un tableau numpy en liste Python.
- Numpy met tous les nombres du meme type : un melange d'`int` et de `float`
  donne des `float`.
- Une boucle imbriquee permet de parcourir les lignes, puis les valeurs de
  chaque ligne.

## Le slicing sur l'exemple

```text
family
ligne 0 : [1.80, 78.4]
ligne 1 : [2.15, 102.7]
ligne 2 : [2.10, 98.5]
ligne 3 : [1.88, 75.2]
```

- `slice_me(family, 0, 2)` garde les lignes 0 et 1. La forme passe de `(4, 2)`
  a `(2, 2)`.
- `slice_me(family, 1, -2)` garde de la ligne 1 jusqu'a l'avant-avant-derniere
  (`-2` correspond a la ligne 2, qui est exclue). Il reste la ligne 1 seule, la
  forme est `(1, 2)`.

## Gestion des erreurs

Aucune exception ne doit sortir de la fonction. En cas d'erreur, le message est
affiche avec `print`, et la fonction s'arrete sans valeur de retour explicite
(elle renvoie `None`, comme toute fonction sans `return`). Le sujet n'impose
pas de valeur de retour precise en cas d'erreur, seulement qu'aucune exception
ne sorte et qu'un message clair soit affiche.

Les verifications sont faites du plus general au plus precis, car chaque
verification suppose que la precedente est passee.

| Ordre | Cas | Erreur | Message |
|---|---|---|---|
| 1 | `family` n'est pas une liste | `TypeError` | `family must be a list` |
| 2 | `start` ou `end` n'est pas un entier | `TypeError` | `start and end must be integers` |
| 3 | une ligne n'est pas une liste | `TypeError` | `each row of family must be a list` |
| 4 | lignes de tailles differentes | `ValueError` | `all rows must have the same length` |
| 5 | valeur ni `int` ni `float` | `TypeError` | `family must contain only integers or floats` |

`TypeError` est utilisee quand le type est mauvais, `ValueError` quand le type
est bon mais que la valeur ne convient pas (ici, la taille d'une ligne).

## Cas limites

- `[]` (aucune ligne) et `[[]]` (une ligne vide) ne sont pas refuses : ils
  donnent une liste vide, avec une forme `(0,)` ou `(1, 0)`.
- `True` et `False` sont acceptes comme valeurs, car ce sont des `int` en
  Python.

## Regles a respecter

- utiliser le slicing ;
- utiliser Python 3.10 et des imports explicites (`import numpy as np`) ;
- pas de variable globale ;
- ajouter une docstring a la fonction ;
- ne laisser aucune exception non attrapee ;
- respecter la norme avec `flake8`.

## Tests

Depuis le dossier `ex01`, avec le venv active :

```bash
python3 tester.py
python3 test_errors.py
```

`test_errors.py` teste des cas valides, tous les cas d'erreur et les cas
limites. Chaque erreur doit afficher son message puis `None`, sans traceback.

## Verification de la docstring

```bash
python3 -c "from array2D import slice_me; print(slice_me.__doc__)"
```
