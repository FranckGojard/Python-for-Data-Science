# Exercice 00 - Give my BMI

## Sujet

Le but de cet exercice est de calculer l'indice de masse corporelle (BMI, ou
IMC) a partir de deux listes : les tailles et les poids.

Fichier a rendre :

- `give_bmi.py`

Le module contient deux fonctions :

- `give_bmi(height, weight)` : renvoie la liste des BMI ;
- `apply_limit(bmi, limit)` : renvoie une liste de booleens.

## Donnees de depart

```python
height = [2.71, 1.15]
weight = [165.3, 38.4]
```

Le fichier `tester.py` du sujet :

```python
from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
```

Resultat attendu :

```text
[22.507863455018317, 29.0359168241966] <class 'list'>
[False, True]
```

## Partie 1 : give_bmi

La fonction recoit deux listes de nombres (`int` ou `float`) et renvoie une
liste avec le BMI de chaque personne.

Formule :

```text
BMI = poids / taille ** 2
```

Les listes sont converties en tableaux numpy avec `np.array(...)`. Numpy
applique ensuite le calcul a tous les elements en une seule ligne, position par
position, sans boucle `for` a ecrire.

Le resultat est converti en vraie liste Python avec `.tolist()`, car le sujet
attend `<class 'list'>`.

## Partie 2 : apply_limit

La fonction recoit une liste de BMI et une limite. Elle renvoie une liste de
booleens : `True` si le BMI est strictement au-dessus de la limite, sinon
`False`.

```text
bmi   : [22.5, 29.0]
limit : 26
sortie: [False, True]
```

Une comparaison produit deja un `True` ou un `False`. Avec un tableau numpy, la
comparaison est faite pour tous les elements d'un coup :

```python
imc > limit
```

Un BMI egal a la limite donne `False`, car il n'est pas au-dessus.

## Notions apprises

- numpy fait des operations sur tous les elements d'un tableau sans boucle
  (operation vectorisee).
- Numpy associe les elements par position : les deux listes doivent avoir la
  meme taille. Sinon, numpy peut diffuser une liste de taille 1 sur l'autre
  sans lever d'erreur.
- `.tolist()` convertit un tableau numpy en liste Python.
- Une comparaison est une expression qui vaut `True` ou `False`.
- `isinstance(valeur, (int, float))` teste le type d'une valeur.
- `True` et `False` sont consideres comme des `int` en Python.
- `raise` leve une exception, `try` / `except ... as error` l'attrape.
- `ValueError` : le type est bon mais la valeur ne convient pas.
- `TypeError` : le type n'est pas le bon.
- Une fonction sans `return` renvoie `None`.

## Gestion des erreurs

Aucune exception ne doit sortir de la fonction. En cas d'erreur, le message est
affiche avec `print` et la fonction renvoie une liste vide `[]`.

Cas geres par `give_bmi` :

| Cas | Message |
|---|---|
| listes de tailles differentes | `height and weight must have the same length` |
| element ni `int` ni `float` | `height and weight must contain only integers or floats` |
| valeur inferieure ou egale a 0 | `height and weight must be greater than 0` |

Cas geres par `apply_limit` :

| Cas | Message |
|---|---|
| `bmi` n'est pas une liste | `bmi must be a list` |
| `limit` n'est pas un entier | `limit must be only integers` |
| element de `bmi` ni `int` ni `float` | `bmi must contain only integers or floats` |

L'ordre des verifications est important : le type est verifie avant la valeur,
sinon comparer du texte avec `0` provoquerait une erreur.

## Regles a respecter

- utiliser Python 3.10 ;
- utiliser des imports explicites (`import numpy as np`) ;
- pas de variable globale ;
- ajouter une docstring a chaque fonction ;
- ne laisser aucune exception non attrapee ;
- respecter la norme avec `flake8`.

## Tests

Depuis le dossier `ex00`, avec le venv active :

```bash
python3 tester.py
```

Tests d'erreurs :

```bash
python3 -c "from give_bmi import give_bmi; print(give_bmi([1.7], [60, 70]))"
python3 -c "from give_bmi import give_bmi; print(give_bmi(['a'], [60]))"
python3 -c "from give_bmi import give_bmi; print(give_bmi([0], [60]))"
python3 -c "from give_bmi import apply_limit; print(apply_limit([22.5], 'abc'))"
python3 -c "from give_bmi import apply_limit; print(apply_limit(5, 26))"
```

Chaque test doit afficher un message d'erreur puis `[]`, sans traceback.

## Verification des docstrings

```bash
python3 -c "from give_bmi import give_bmi; print(give_bmi.__doc__)"
python3 -c "from give_bmi import apply_limit; print(apply_limit.__doc__)"
```
