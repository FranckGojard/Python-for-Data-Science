# Exercice 06 - Recode filter

## Sujet

L'exercice comporte deux parties :

- recreer la fonction integree `filter` dans `ft_filter.py` ;
- utiliser cette fonction dans `filterstring.py`.

Les fichiers a rendre sont :

- `ft_filter.py` ;
- `filterstring.py`.

## Partie 1 : ft_filter

La fonction `ft_filter` recoit :

- une fonction de condition ;
- un iterable, par exemple une liste.

Elle parcourt les elements et garde ceux pour lesquels la condition renvoie
`True`.

Une comprehension de liste est demandee par le sujet.

La fonction doit se comporter comme la fonction Python `filter`. Elle retourne
un iterable. Pour afficher son contenu sous forme de liste, on peut utiliser
`list(...)`.

### Exemple de fonctionnement

```text
condition : garder les mots de plus de 4 caracteres
liste     : ["Hi", "Hello", "Python"]
resultat  : ["Hello", "Python"]
```

Le cas `None` est aussi un comportement du vrai `filter`. Quand la condition
vaut `None`, les elements consideres comme vrais sont conserves.

```python
filter(None, [0, 1, "", "Hello"])
```

Le resultat contient `1` et `"Hello"`, car `0` et `""` sont consideres comme
faux dans une condition Python.

## Partie 2 : filterstring.py

Le programme recoit deux arguments :

1. une chaine de caracteres `S` ;
2. un entier `N`.

Il affiche les mots de `S` dont la longueur est strictement superieure a `N`.
Les mots sont separes par des espaces.

Le programme doit contenir :

- une list comprehension ;
- une `lambda` ;
- une verification du nombre d'arguments ;
- une verification de la conversion de `N` en entier ;
- un appel a `ft_filter`.

Le sujet precise que les chaines de test ne contiennent pas de ponctuation ni
de caracteres invisibles particuliers.

## Arguments du terminal

Quand on lance :

```bash
python3 filterstring.py "Hello the World" 4
```

Python recoit notamment :

```python
["filterstring.py", "Hello the World", "4"]
```

Les arguments du terminal sont d'abord des chaines de caracteres. Le deuxieme
argument doit donc etre converti en entier avant de comparer les longueurs.

La methode `split()` transforme la phrase en liste de mots :

```text
"Hello the World" -> ["Hello", "the", "World"]
```

La `lambda` sert de condition. Elle recoit un mot et renvoie `True` si sa
longueur est superieure a `N`.

## Erreurs

Si le nombre d'arguments est different de deux, ou si `N` n'est pas un entier,
le programme doit afficher :

```text
AssertionError: the arguments are bad
```

## Regles a respecter

- ne pas utiliser la fonction integree `filter` dans `ft_filter.py` ;
- utiliser au moins une list comprehension ;
- utiliser au moins une `lambda` ;
- utiliser Python 3.10 ;
- avoir une fonction `main()` dans le programme ;
- proteger l'appel avec `if __name__ == "__main__":` ;
- ajouter une docstring a chaque fonction ;
- ne pas laisser une exception demandee par le sujet provoquer un traceback ;
- utiliser des imports explicites ;
- respecter la norme avec `flake8`.

## Tests de filterstring.py

Depuis le dossier `ex06` :

```bash
python3 filterstring.py "Hello the World" 4
python3 filterstring.py "Hello the World" 99
python3 filterstring.py
python3 filterstring.py 3 "Hello the World"
python3 filterstring.py "Hello the World" abc
python3 filterstring.py "Hello the World" 4 5
```

Resultats attendus :

```text
['Hello', 'World']
[]
AssertionError: the arguments are bad
AssertionError: the arguments are bad
AssertionError: the arguments are bad
AssertionError: the arguments are bad
```

## Tests de ft_filter.py

Ces tests permettent de verifier le comportement de la fonction seule :

```bash
python3 -c "from ft_filter import ft_filter; print(list(ft_filter(lambda word: len(word) > 4, ['Hi', 'Hello', 'Python'])))"
python3 -c "from ft_filter import ft_filter; print(list(ft_filter(None, [0, 1, '', 'Hello'])))"
```

Resultats attendus :

```text
['Hello', 'Python']
[1, 'Hello']
```

## Verification des docstrings

```bash
python3 -c "from ft_filter import ft_filter; print(ft_filter.__doc__)"
python3 -c "import filterstring; print(filterstring.main.__doc__)"
```