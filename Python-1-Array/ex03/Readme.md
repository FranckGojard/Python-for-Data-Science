# Exercice 03 - Zoom on me

## Sujet

Le but de cet exercice est d'ecrire un programme qui charge l'image
`animal.jpeg`, affiche des informations dessus, puis affiche une version
"zoomee" (recadree) de l'image.

Fichiers a rendre :

- `load_image.py` (identique a celui de `ex02`)
- `zoom.py`

Contrairement aux exercices precedents, il n'y a pas de prototype de fonction
impose ni de `tester.py` fourni par le sujet : c'est un petit programme libre.

Le programme doit afficher :

- la taille en pixels sur les axes X et Y
- le nombre de canaux
- le contenu des pixels
- l'image, zoomee, avec les axes gradues

Il doit gerer toutes les erreurs sans jamais planter.

## Sortie attendue (exemple du sujet)

```text
The shape of image is: (768, 1024, 3)
[[[120 111 132]
 [139 130 151]
 [155 146 167]
  ...
 [120 156 94]
 [119 154 90]
 [118 153 89]]]
New shape after slicing: (400, 400, 1) or (400, 400)
[[[167]
  [180]
  [194]
  ...
  [102]
  [104]
  [103]]]
```

Puis une fenetre s'ouvre avec l'image recadree, en niveaux de gris, axes
gradues.

Le sujet precise que l'image et la zone de zoom donnees en exemple (un raton
laveur) ne sont pas celles a reproduire : le programme travaille sur
`animal.jpeg`.

## Notions apprises

- Slicing sur plusieurs dimensions d'un tableau numpy en une seule fois, avec
  une virgule : `image[debut_ligne:fin_ligne, debut_colonne:fin_colonne]`.
  Different du slicing sur une liste de listes (`ex01`), qui ne decoupe que
  les lignes.
- Pour "zoomer au centre" : diviser la hauteur et la largeur par 2
  (`shape[0] // 2`, `shape[1] // 2`) pour trouver le centre, puis prendre la
  meme distance de chaque cote.
- Garder un seul canal sur les 3 (R, G ou B) avec un 3e slice :
  `image[..., ..., 0:1]`.
- `matplotlib.pyplot` affiche une image a l'ecran : `plt.imshow(tableau)`
  prepare l'affichage, `plt.show()` ouvre la fenetre. Les axes sont gradues
  par defaut.
- Avec un tableau a un seul canal, matplotlib applique par defaut une
  colormap arbitraire (pas du gris). Il faut preciser `cmap="gray"` a
  `imshow` pour avoir une image en niveaux de gris comme dans le sujet.
- Un programme qui execute du code (pas juste des `def`) a besoin d'un
  `main()` protege par `if __name__ == "__main__":`. Contrairement a
  `load_image.py` (qui ne contient qu'une fonction), `zoom.py` execute des
  appels directement, donc il en a besoin.
- En Python, contrairement au C, la valeur retournee par `main()` ne devient
  pas automatiquement le code de sortie du programme : `return` sert juste a
  arreter la fonction.
- `raise` ne retourne rien : il interrompt la fonction et saute au `except`
  le plus proche. C'est le `except` qui decide quoi faire ensuite.
- `return []` en cas d'erreur n'est pas une obligation du sujet, juste une
  convention de coherence entre les fonctions du projet. Ici, les fonctions
  qui renvoient un tableau numpy en cas de succes (contrairement a `list`
  dans `ex00`/`ex01`) ne renvoient rien de special en cas d'erreur : elles
  renvoient `None` implicitement (pas de `return` dans le `except`).
- Tester `None` avec `== None` sur un tableau numpy declenche une comparaison
  element par element, qui plante dans un `if` (`ValueError: the truth value
  of an array ... is ambiguous`). Il faut utiliser `is None`, qui compare
  l'identite de l'objet et pas son contenu.

## Gestion des erreurs

Aucune exception ne doit sortir du programme. En cas d'erreur, le message est
affiche avec `print`, et la fonction s'arrete sans retourner de tableau
(`None` implicite).

| Fonction | Cas | Erreur | Message |
|---|---|---|---|
| `ft_load` | `path` n'est pas une chaine | `TypeError` | `path must be a string` |
| `ft_load` | extension non supportee | `ValueError` | `file format not supported` |
| `ft_load` | fichier introuvable | `FileNotFoundError` | message par defaut de Python |
| `zoom` | `image` n'est pas un tableau numpy | `TypeError` | `image must be a ndarray` |

Dans `main()`, le resultat de `zoom()` est verifie avec `is None` avant de
continuer (afficher le shape, afficher l'image), pour eviter de planter si le
zoom a echoue.

## Regles a respecter

- gerer toute erreur sans que le programme ne s'arrete brutalement ;
- utiliser Python 3.10 et des imports explicites ;
- pas de variable globale ;
- ajouter une docstring a chaque fonction ;
- ne laisser aucune exception non attrapee ;
- respecter la norme avec `flake8`.

## Tests

Depuis le dossier `ex03`, avec le venv active :

```bash
python3 zoom.py
```

Tests d'erreurs :

```bash
python3 -c "from zoom import zoom; print(zoom('pas une image'))"
```

Chaque test d'erreur doit afficher un message, sans traceback.

## Verification des docstrings

```bash
python3 -c "from zoom import zoom, main; print(zoom.__doc__); print(main.__doc__)"
```
