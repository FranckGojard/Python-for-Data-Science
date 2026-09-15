# Exercice 08 - Loading

## Sujet

Le but de cet exercice est de creer une fonction `ft_tqdm` qui reproduit le
fonctionnement principal de `tqdm`.

Fichier a rendre :

- `Loading.py`

La fonction doit etre utilisable dans une boucle :

```python
for element in ft_tqdm(range(333)):
    ...
```

## Objectif

La fonction doit :

- recevoir un iterable, par exemple un `range` ;
- parcourir ses elements ;
- afficher une progression ;
- renvoyer les elements un par un avec `yield`.

## Notion importante : yield

`yield` renvoie un element puis met la fonction en pause.

Au tour suivant de la boucle, la fonction reprend la ou elle s'etait arretee.
Cela permet de produire les elements un par un sans construire toute une liste
avant de commencer.

```text
yield element 0 -> pause
yield element 1 -> pause
yield element 2 -> pause
```

C'est ce comportement qui permet d'utiliser `ft_tqdm` dans une boucle `for`.

## Calcul de la progression

Le nombre total d'elements est obtenu avec `len`.

`enumerate` permet d'obtenir deux informations pendant la boucle :

- `position` : la position actuelle, qui commence a `0` ;
- `element` : la valeur actuelle.

Le nombre d'elements deja parcourus est donc `position + 1`.

Le pourcentage est calcule avec :

```text
nombre deja parcouru / nombre total * 100
```

La barre est construite en repetant le caractere `=` selon le pourcentage.

## Affichage sur une seule ligne

Le caractere `\r` revient au debut de la ligne actuelle.
Il permet de remplacer l'ancien affichage par la nouvelle progression.

`end=""` evite que `print` ajoute une nouvelle ligne a chaque iteration.

Le test ajoute un `sleep` pour ralentir la boucle et rendre les changements
visibles. Le `sleep` ne doit pas etre ajoute dans `Loading.py`.

## Regles du sujet

- utiliser une fonction appelee `ft_tqdm` ;
- utiliser `yield` ;
- ne pas utiliser la vraie fonction `tqdm` dans `Loading.py` ;
- ne pas utiliser `sleep` dans `Loading.py` ;
- ne pas ajouter de test qui s'execute automatiquement dans `Loading.py` ;
- ajouter une docstring a la fonction ;
- utiliser Python 3.10.

## Fichier de test

Le sujet fournit un exemple de test. Tu peux creer temporairement un fichier
`tester.py` dans le dossier `ex08`. Ce fichier sert uniquement a comparer ta
fonction avec la vraie fonction `tqdm` et n'est pas le fichier a rendre.

```python
from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for element in ft_tqdm(range(333)):
    sleep(0.005)

print()

for element in tqdm(range(333)):
    sleep(0.005)

print()
```

Pour lancer le test :

```bash
python3 tester.py
```

Si la bibliotheque `tqdm` n'est pas installee, le test peut afficher une erreur
`ModuleNotFoundError`. Dans ce cas, installer la bibliotheque avec :

```bash
python3 -m pip install tqdm
```

## Petit test rapide

Depuis le dossier `ex08` :

```bash
python3 -c "from Loading import ft_tqdm; [element for element in ft_tqdm(range(3))]; print()"
```

Ce test verifie que la fonction parcourt bien les valeurs `0`, `1` et `2`.
