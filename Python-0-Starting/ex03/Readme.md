# Ex03 - NULL Not Found

## Sujet

Le but de cet exercice est d'ecrire une fonction qui reconnait plusieurs valeurs
"nulles" ou "vides" en Python.

Fichier a rendre :

- `NULL_not_found.py`

Prototype demande :

```python
def NULL_not_found(object: any) -> int:
```

Valeurs testees :

- `None`
- `float("NaN")`
- `0`
- `''`
- `False`
- une valeur non reconnue

## Sortie Attendue

```text
Nothing: None <class 'NoneType'>
Cheese: nan <class 'float'>
Zero: 0 <class 'int'>
Empty: <class 'str'>
Fake: False <class 'bool'>
Type not Found
1
```

## Retours Attendus

- Retourner `0` si la valeur est reconnue.
- Retourner `1` si la valeur n'est pas reconnue.

## Notions Apprises

- `None` represente l'absence de valeur.
- `False` est un booleen.
- `''` est une chaine vide.
- `0` est un entier.
- `NaN` signifie `Not a Number`.
- `==` compare les valeurs.
- `is` compare l'identite de l'objet en memoire.

## Point Special Sur NaN

`NaN` est un cas particulier : il n'est egal a rien, meme pas a lui-meme.

Donc :

```python
nan == nan
```

donne `False`.

Et :

```python
nan != nan
```

donne `True`.

Cette particularite permet de detecter `NaN` sans import supplementaire.

## Difference Entre == Et is

`==` compare le contenu :

```python
[1, 2] == [1, 2]
```

donne `True`.

`is` compare si deux noms pointent vers exactement le meme objet.

On utilise souvent `is` pour les singletons Python :

```python
object is None
object is False
```

## Test

Depuis la racine du projet :

```bash
python3 Python-0-Starting/ex03/tester.py | cat -e
```

Verifier aussi que le fichier seul n'affiche rien :

```bash
python3 Python-0-Starting/ex03/NULL_not_found.py | cat -e
```
