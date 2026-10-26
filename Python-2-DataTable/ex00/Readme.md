# Exercice 00 - Load my Dataset

## Sujet

Le but de cet exercice est d'ecrire une fonction qui charge un fichier CSV,
affiche ses dimensions, et le retourne.

Fichier a rendre :

- `load_csv.py`

Prototype impose :

```python
def load(path: str) -> Dataset:
    # your code here
```

`Dataset` est indicatif (comme `array` l'etait dans le module precedent) :
le type reel depend de la librairie utilisee.

Le sujet demande de gerer les cas d'erreur et de retourner `None` si le
chemin est mauvais ou le format incorrect.

## Donnees de depart

Le `tester.py` du sujet :

```python
from load_csv import load

print(load("life_expectancy_years.csv"))
```

Resultat attendu :

```text
Loading dataset of dimensions (195, 302)
country 1800 1801 1802 1803 ... 2096 2097 2098 2099 2100
Afghanistan 28.2 28.2 28.2 28.2 ... 76.2 76.4 76.5 76.6 76.8
...
```

Le sujet precise que l'affichage du dataset n'est pas strict, le format
donne n'est qu'un exemple.

Le fichier `life_expectancy_years.csv` vient de gapminder.org (licence
CC-BY) et est place dans `Python-2-DataTable/csv/`.

## Notions apprises

- **CSV** (*Comma-Separated Values*) : un format texte simple pour stocker un
  tableau, une ligne de fichier = une ligne de donnees, valeurs separees par
  des virgules.
- **pandas** : bibliotheque de manipulation de donnees tabulaires. Import
  explicite : `import pandas as pd`.
- **DataFrame** : le type concret de pandas pour un tableau 2D avec des
  lignes et colonnes nommees (contrairement a un tableau numpy, qui n'a que
  des indices). C'est ce que `pd.read_csv(path)` retourne.
- `pd.read_csv(path)` charge un fichier CSV directement dans un `DataFrame`.
- `.shape` sur un `DataFrame` fonctionne comme sur un tableau numpy :
  `(lignes, colonnes)`.
- Un `DataFrame` s'affiche automatiquement de façon lisible avec `print()`,
  pas besoin de coder l'affichage.
- Piege : `pd.read_csv` (sans parentheses) donne la fonction elle-meme, pas
  le resultat de son execution. Il faut l'appeler avec `pd.read_csv(path)`.
- `pd.read_csv()` leve automatiquement un `FileNotFoundError` si le fichier
  n'existe pas, comme `Image.open()` le faisait pour les images.

## Gestion des erreurs

Aucune exception ne doit sortir de la fonction. En cas d'erreur, le message
est affiche avec `print`, et la fonction retourne `None` (demande
explicitement par le sujet, contrairement au module precedent ou c'etait
une convention personnelle).

| Ordre | Cas | Erreur | Message |
|---|---|---|---|
| 1 | `path` n'est pas une chaine | `TypeError` | `Path must be a string` |
| 2 | extension differente de `.csv` | `ValueError` | `File format not supported` |
| 3 | fichier introuvable | `FileNotFoundError` | message par defaut de Python |

## Regles a respecter

- gerer les cas d'erreur, retourner `None` si le chemin est mauvais ou le
  format incorrect ;
- utiliser Python 3.10 et des imports explicites (`import pandas as pd`) ;
- pas de variable globale ;
- ajouter une docstring a la fonction ;
- ne laisser aucune exception non attrapee ;
- respecter la norme avec `flake8`.

## Tests

Depuis le dossier `ex00`, avec le venv active :

```bash
python3 tester.py
```

Tests d'erreurs :

```bash
python3 -c "from load_csv import load; print(load(42))"
python3 -c "from load_csv import load; print(load('image.png'))"
python3 -c "from load_csv import load; print(load('inexistant.csv'))"
```

Chaque test d'erreur doit afficher un message, puis `None`, sans traceback.

## Verification de la docstring

```bash
python3 -c "from load_csv import load; print(load.__doc__)"
```
