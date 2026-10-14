# Exercice 04 - Rotate me

## Sujet

Le but de cet exercice est d'ecrire un programme qui charge l'image
`animal.jpeg`, decoupe une partie carree (comme `ex03`), puis la **transpose**
(echange lignes et colonnes) avant de l'afficher.

Fichiers a rendre :

- `load_image.py` (identique a celui de `ex02`/`ex03`)
- `rotate.py`

⚠️ **Contrainte du sujet** : la transposition doit etre codee a la main,
**aucune librairie n'est autorisee pour ca** (interdit d'utiliser `.T` ou
`np.transpose()`).

## Sortie attendue (exemple du sujet)

```text
$> python rotate.py
The shape of image is: (400, 400, 1) or (400, 400)
[[[167]
  [180]
  [194]
  ...
  [102]
  [104]
  [103]]]
New shape after Transpose: (400, 400)
[[167 180 194 ... 64 50 72]
  ...
 [115 116 119 ... 102 104 103]]
```

Puis une fenetre s'ouvre avec l'image transposee. Le sujet precise que le
tableau et l'image peuvent etre differents du tien.

## Notions apprises

- **Ce qu'est une transposition** : l'element a la position `[i][j]` passe a
  la position `[j][i]`. Sur une matrice carree, la diagonale ne bouge pas,
  tout le reste est echange en miroir.
- **Boucler sur les indices plutot que sur les valeurs** : `for x in liste`
  donne directement les valeurs (on perd la position), alors que
  `for i in range(len(liste))` donne les indices, ce qui permet d'aller lire
  **et** ecrire a une position precise.
- **Pourquoi un nouveau tableau** : modifier le tableau pendant qu'on le
  parcourt risquerait d'ecraser des valeurs dont on a encore besoin. On cree
  donc un tableau vide avec `np.zeros((largeur, hauteur))`, et on le remplit
  au fur et a mesure.
- **Le `[0]` pour sortir du canal** : `image[i][j]` est une petite liste a 1
  element (`[167]`), pas un nombre seul, car il reste la dimension du canal
  (`ex03`). `image[i][j][0]` recupere le nombre a l'interieur. Sans ce `[0]`,
  l'affectation dans un tableau 2D plante
  (`ValueError: setting an array element with a sequence`).
- `.ndim` donne le nombre de dimensions d'un tableau numpy (different de
  `.shape`, qui donne la taille de chaque dimension).
- `np.zeros((shape))` cree un tableau rempli de 0 (en `float` par defaut, ce
  qui explique les `.0` dans les valeurs affichees, contrairement a
  l'exemple du sujet qui a des entiers).

## Gestion des erreurs

Aucune exception ne doit sortir du programme. En cas d'erreur, le message est
affiche avec `print`, et la fonction s'arrete sans retourner de tableau
(`None` implicite). Le sujet n'impose pas de valeur de retour precise,
seulement qu'aucune exception ne sorte et qu'un message clair soit affiche.

| Fonction | Cas | Erreur | Message |
|---|---|---|---|
| `zoom` | `image` n'est pas un tableau numpy | `TypeError` | `image must be a ndarray` |
| `rotate` | `image` n'est pas un tableau numpy | `TypeError` | `image must be a ndarray` |
| `rotate` | `image` n'a pas 3 dimensions | `ValueError` | `image must have 3 dimensions` |

Dans `main()`, chaque resultat (`zoom()` puis `rotate()`) est verifie avec
`is None` avant de continuer, pour eviter de planter en cascade si une etape
a echoue.

## Regles a respecter

- coder la transposition soi-meme, sans fonction de librairie pour ca ;
- gerer toute erreur sans que le programme ne s'arrete brutalement ;
- utiliser Python 3.10 et des imports explicites ;
- pas de variable globale ;
- ajouter une docstring a chaque fonction ;
- ne laisser aucune exception non attrapee ;
- respecter la norme avec `flake8`.

## Tests

Depuis le dossier `ex04`, avec le venv active :

```bash
python3 rotate.py
```

Tests d'erreurs :

```bash
python3 -c "from rotate import rotate; print(rotate('pas une image'))"
python3 -c "import numpy as np; from rotate import rotate; print(rotate(np.zeros((5, 5))))"
```

Chaque test d'erreur doit afficher un message, sans traceback.

## Verification des docstrings

```bash
python3 -c "from rotate import rotate, main; print(rotate.__doc__); print(main.__doc__)"
```
