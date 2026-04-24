# Ex04 - The Even And The Odd

## Sujet

Le but de cet exercice est de creer un script qui prend un nombre en argument et
affiche s'il est pair ou impair.

Fichier a rendre :

- `whatis.py`

Exemples attendus :

```text
python3 whatis.py 14    -> I'm Even.
python3 whatis.py -5    -> I'm Odd.
python3 whatis.py       -> n'affiche rien
python3 whatis.py 0     -> I'm Even.
python3 whatis.py Hi!   -> AssertionError: argument is not an integer
python3 whatis.py 13 5  -> AssertionError: more than one argument is provided
```

## Notions Apprises

- `sys.argv` contient les arguments donnes au script.
- `sys.argv[0]` correspond au nom du script.
- Les arguments recus depuis le terminal sont des chaines de caracteres.
- `int(...)` convertit une chaine en entier quand c'est possible.
- `%` donne le reste d'une division.
- Un nombre est pair si `nombre % 2 == 0`.
- `try` / `except` permet de gerer une erreur sans faire crasher le programme.

## Arguments

Quand on lance :

```bash
python3 whatis.py 14
```

Python recoit une liste de ce genre :

```python
["whatis.py", "14"]
```

Le `14` est donc d'abord du texte. Pour faire un calcul dessus, il faut le
convertir avec `int(...)`.

## try / except

La conversion suivante fonctionne :

```python
int("42")
```

Mais celle-ci declenche une `ValueError` :

```python
int("Hi!")
```

On utilise donc :

```python
try:
    ...
except ValueError:
    ...
```

pour afficher le message demande au lieu de laisser Python afficher un traceback.

## exit() Et sys.exit()

`exit()` fonctionne souvent, mais c'est surtout un helper prevu pour
l'interpreteur interactif Python.

Dans un script, la forme standard est :

```python
sys.exit()
```

La difference n'est pas une question de performance ou de memoire. La difference
principale est que `sys.exit()` est l'API explicite du module `sys`, alors que
`exit()` depend d'un helper charge automatiquement dans la plupart des contextes.

## Test

Depuis la racine du projet :

```bash
python3 Python-0-Starting/ex04/whatis.py | cat -e
python3 Python-0-Starting/ex04/whatis.py 14 | cat -e
python3 Python-0-Starting/ex04/whatis.py -5 | cat -e
python3 Python-0-Starting/ex04/whatis.py 0 | cat -e
python3 Python-0-Starting/ex04/whatis.py Hi! | cat -e
python3 Python-0-Starting/ex04/whatis.py 13 5 | cat -e
```
