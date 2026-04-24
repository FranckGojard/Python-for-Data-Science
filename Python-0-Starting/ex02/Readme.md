# Ex02 - First Function Python

## Sujet

Le but de cet exercice est d'ecrire une fonction qui affiche le type d'un objet
et retourne toujours `42`.

Fichier a rendre :

- `find_ft_type.py`

Prototype demande :

```python
def all_thing_is_obj(object: any) -> int:
```

Le fichier `tester.py` appelle cette fonction avec plusieurs objets :

- une liste
- un tuple
- un set
- un dictionnaire
- des chaines de caracteres
- un entier

## Sortie Attendue

```text
List : <class 'list'>
Tuple : <class 'tuple'>
Set : <class 'set'>
Dict : <class 'dict'>
Brian is in the kitchen : <class 'str'>
Toto is in the kitchen : <class 'str'>
Type not found
42
```

## Notions Apprises

- `def` sert a definir une fonction.
- Un parametre est une valeur recue par une fonction.
- `print` affiche dans le terminal.
- `return` renvoie une valeur a celui qui appelle la fonction.
- Si une fonction ne retourne rien explicitement, Python retourne `None`.
- `type(...)` permet de connaitre le type d'un objet.
- `if`, `elif`, `else` permettent de gerer plusieurs cas.

## Point Important

Le fichier `find_ft_type.py` ne doit rien afficher quand il est lance seul.

La fonction affiche les messages uniquement quand elle est appelee par le
`tester.py`.

## Test

Depuis la racine du projet :

```bash
python3 Python-0-Starting/ex02/tester.py | cat -e
```

Verifier aussi que le fichier seul n'affiche rien :

```bash
python3 Python-0-Starting/ex02/find_ft_type.py | cat -e
```
