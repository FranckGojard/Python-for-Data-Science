# Exercice 05 - Pimp my image

## Sujet

Le but de cet exercice est d'ecrire 5 fonctions qui appliquent chacune un
filtre de couleur a une image, en gardant la meme forme (shape).

Fichiers a rendre :

- `load_image.py` (identique a celui de `ex02`/`ex03`/`ex04`)
- `pimp_image.py`

Prototype impose :

```python
def ft_invert(array) -> array:
def ft_red(array) -> array:
def ft_green(array) -> array:
def ft_blue(array) -> array:
def ft_grey(array) -> array:
```

⚠️ **Contrainte du sujet** : chaque fonction n'a le droit qu'a certains
operateurs (pas obligatoire de tous les utiliser, mais interdit d'en
utiliser d'autres) :

| Fonction | Operateurs autorises |
|---|---|
| `ft_invert` | `=`, `+`, `-`, `*` |
| `ft_red` | `=`, `*` |
| `ft_green` | `=`, `-` |
| `ft_blue` | `=` |
| `ft_grey` | `=`, `/` |

Le sujet precise aussi qu'il faut **afficher** chaque image transformee (pas
juste la retourner) : *"you must display the images transformed"*.

## Donnees de depart

Le `tester.py` du sujet :

```python
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

array = ft_load("landscape.jpg")

ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)

print(ft_invert.__doc__)
```

L'image utilisee est `landscape.jpg` (celle de `ex02`), pas `animal.jpeg`.

## Notions apprises

- **Cibler un canal sur toute l'image d'un coup** : `array[:, :, i] = valeur`
  modifie le canal `i` (0 = rouge, 1 = vert, 2 = bleu) pour tous les pixels en
  une seule instruction, sans boucle (comme vu en `ex03`/`ex04` pour le
  decoupage spatial, ici applique au 3e axe).
- **Contourner une contrainte d'operateur avec une fonction** : `ft_grey`
  n'autorise pas `+`, mais `array.sum(axis=2)` fait la somme des 3 canaux
  sans ecrire l'operateur `+` soi-meme (c'est une fonction, pas un operateur).
- **`axis=2`** : le 3e axe du tableau (0 = lignes, 1 = colonnes, 2 = canaux),
  numerote a partir de 0 comme `shape[0]`, `shape[1]`, `shape[2]`.
- **Modification en place vs copie** : passer un tableau numpy a une
  fonction ne passe pas une copie, mais une reference vers le **meme** objet
  en memoire. Modifier ce tableau dans une fonction (`array[:, :, 1] = 0`)
  modifie donc aussi l'original utilise par l'appelant. Comme `tester.py`
  appelle les 5 fonctions **a la suite sur le meme tableau**, chaque fonction
  continuait sur les degats de la precedente (ex: apres `ft_red`, il ne
  restait plus que le rouge, donc `ft_green` ecrasait aussi ce qui restait).
  La solution : `array = array.copy()` en debut de fonction, pour que chaque
  filtre reparte d'une version intacte de l'image.
- `255 - array` (pour l'inversion) ne modifie pas l'original : contrairement
  a `array[:, :, i] = ...`, cette expression cree un **nouveau** tableau,
  qui est ensuite stocke dans la variable locale `array` de la fonction.

## Gestion des erreurs

Non traitee dans cet exercice : contrairement aux precedents, le sujet de
`ex05` ne mentionne pas explicitement de cas d'erreur a gerer, seulement les
restrictions d'operateurs et l'affichage obligatoire.

## Regles a respecter

- respecter les operateurs autorises pour chaque fonction ;
- garder la meme forme (shape) apres transformation ;
- afficher chaque image transformee ;
- utiliser Python 3.10 et des imports explicites ;
- pas de variable globale ;
- ajouter une docstring a chaque fonction ;
- respecter la norme avec `flake8`.

## Tests

Depuis le dossier `ex05`, avec le venv active :

```bash
python3 tester.py
```

5 fenetres s'ouvrent l'une apres l'autre (fermer chacune pour passer a la
suivante) : invert, red, green, blue, grey.

`show_filters.py` affiche en plus les 6 versions (original + 5 filtres) dans
une seule fenetre, cote a cote, pour comparer facilement :

```bash
python3 show_filters.py
```

## Verification des docstrings

```bash
python3 -c "from pimp_image import ft_invert; print(ft_invert.__doc__)"
```
