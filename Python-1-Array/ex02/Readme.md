# Exercice 02 - Load my image

## Sujet

Le but de cet exercice est d'ecrire une fonction qui charge une image (jpg ou
jpeg) et renvoie son contenu sous forme de tableau de pixels.

Fichier a rendre :

- `load_image.py`

Prototype impose :

```python
def ft_load(path: str) -> array:
```

Le `array` du sujet est indicatif (pas un vrai type Python) : le sujet precise
que le type de retour exact est libre.

## Donnees de depart

Le fichier `tester.py` du sujet :

```python
from load_image import ft_load

print(ft_load("landscape.jpg"))
```

Resultat attendu :

```text
The shape of image is: (257, 450, 3)
[[[19 42 83]
  [23 42 84]
  [28 43 84]
   ...
  [ 0  0  0]
  [ 1  1  1]
  [ 1  1  1]]]
```

L'image `landscape.jpg` est dans `Python-1-Array/jpeg/`.

## Notions apprises

- Une image en couleur se charge comme un tableau a 3 dimensions :
  `(lignes, colonnes, canaux)`.
- Les 3 canaux sont Rouge, Vert, Bleu (RGB), chacun entre 0 et 255.
- `Image.open(path)` (bibliotheque Pillow) ouvre un fichier image.
- `np.array(...)` convertit l'image ouverte en tableau numpy.
- `.endswith(suffixe)` teste la fin d'une chaine. Pour tester plusieurs
  suffixes, il faut lui passer un **tuple** : `path.endswith((".jpg", ".jpeg"))`.
  Le 2e argument de `.endswith()` n'est pas un autre suffixe, mais un indice de
  depart.
- `Image.open()` leve lui-meme un `FileNotFoundError` si le fichier n'existe
  pas : ce n'est pas une regle a ecrire avec `if`/`raise`, juste une exception
  a capturer dans le `except`.
- Les chemins relatifs se calculent depuis le dossier ou la commande est
  lancee, pas depuis l'emplacement du script.

## Gestion des erreurs

Aucune exception ne doit sortir de la fonction. En cas d'erreur, le message
est affiche avec `print`, et la fonction s'arrete sans valeur de retour
explicite (elle renvoie `None`, comme toute fonction sans `return`). Le sujet
n'impose pas de valeur de retour precise en cas d'erreur, seulement qu'aucune
exception ne sorte et qu'un message clair soit affiche.

| Ordre | Cas | Erreur | Message |
|---|---|---|---|
| 1 | `path` n'est pas une chaine | `TypeError` | `path must be a string` |
| 2 | l'extension n'est pas `.jpg`/`.jpeg` | `ValueError` | `file format not supported` |
| 3 | le fichier n'existe pas | `FileNotFoundError` | message par defaut de Python |

Les deux premieres regles sont verifiees avant d'essayer d'ouvrir le fichier,
du plus general (le type) au plus precis (le format). La 3e est levee
automatiquement par Pillow au moment de `Image.open(path)`.

## Regles a respecter

- gerer au moins les formats jpg et jpeg ;
- utiliser Python 3.10 et des imports explicites (`import numpy as np`,
  `from PIL import Image`) ;
- pas de variable globale ;
- ajouter une docstring a la fonction ;
- ne laisser aucune exception non attrapee ;
- respecter la norme avec `flake8`.

## Tests

Depuis le dossier `ex02`, avec le venv active :

```bash
python3 tester.py
python3 test_errors.py
```

`test_errors.py` teste le cas valide et tous les cas d'erreur. Chaque erreur
doit afficher son message puis `None`, sans traceback.

## Verification de la docstring

```bash
python3 -c "from load_image import ft_load; print(ft_load.__doc__)"
```
