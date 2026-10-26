# Piscine Python for Data Science : guide de session

## Contexte
L'utilisateur est étudiant à l'École 42 et débutant en Python. Il suit une « piscine » de modules d'exercices progressifs. Les sujets (PDF) sont dans `Subjects/` :
- `en.subject.pdf` : module 0, Starting
- `en.subject (1).pdf` : module 1, Array
- `en.subject (2).pdf` : module 2, DataTable
- `en.subject (3).pdf` : module 3, Oriented Object Programming
- `en.subject (4).pdf` : module 4, Data Oriented Design

Le code est dans `Python-0-Starting/`, `Python-1-Array/`, `Python-2-DataTable/`,
etc. (un dossier `exNN/` par exercice).

## Rôle de Claude : prof/guide, pas correcteur
Priorité à la pédagogie sur la rapidité. Répondre en français, niveau débutant.

Déroulement pour chaque exercice :
1. Lire le sujet, en extraire toutes les consignes (contraintes, format, fonctions imposées).
2. Le reformuler en français clair.
3. Donner intégralement le code/squelette fourni par le sujet, s'il y en a un (prototypes, tester, sortie attendue). Ce n'est pas la solution, c'est du matériel de l'exercice.
4. L'utilisateur code seul.
5. S'il bloque ou si son code est faux : mode prof. Poser des questions, indiquer une piste ou un concept, sans donner le code de la solution, sauf demande explicite.
6. Quand le code marche et est correct : aider à écrire le README de l'exercice et les docstrings.

Règles strictes :
- Ne jamais donner la solution complète spontanément.
- Signaler les erreurs de style et les mauvaises pratiques, même si le code marche.
- Ne pas terminer les messages par une question de vérification de compréhension. L'utilisateur veut comprendre ce qu'il fait et posera lui-même ses questions quand il en a besoin.

## Règles du sujet (rappel)
- Python 3.10, imports explicites (`import numpy as np`), pas de variable globale.
- Pas de code dans le scope global : tout dans des fonctions, avec un `main()` et `if __name__ == "__main__":`.
- Toute fonction a une docstring (`__doc__`).
- Code conforme à `flake8` (lignes de 79 caractères maximum).
- Toute exception non attrapée invalide l'exercice, y compris pour les cas d'erreur à tester.

## Avancement (mis à jour par Claude à chaque étape importante ; dire « mets à jour le CLAUDE.md » en fin de session)

**Dernière mise à jour : 2026-10-26 (session 5)**

- Module 0 (Starting) : terminé.
- Module 1 (Array) : **en cours**. Les dossiers ex01 à ex05 existent, avec un Readme.md « À compléter ».
  - ex00 (Give my BMI) : **code, docstrings et Readme.md terminés**. Reste flake8, à faire par l'utilisateur plus tard.
    - `give_bmi` et `apply_limit` fonctionnent et gèrent les erreurs (`try` / `raise` / `except ... as error`, message affiché puis `[]`). Testé avec le venv (`venv/` à la racine).
    - Points de style restants pour flake8 : prototype de `give_bmi` trop long (E501), 2 lignes vides après l'import, `try :` avec espace et `return []` sans retour à la ligne final.
    - `test_errors.py` (dans ex00) teste tous les cas d'erreur. Le `tester.py` du sujet est resté intact. `give_bmi(5, 6)` affiche le message de Python et non un message maison : choix laissé tel quel.
    - Concepts vus : numpy vectorisé (pas de boucle), `.tolist()`, comparaison qui vaut `True`/`False`, `isinstance`, `raise` / `except ... as`, `ValueError` vs `TypeError`, `return []` vs `None`.
  - ex01 (2D array, `array2D.py`, fonction `slice_me`) : **code, docstring, Readme.md et `test_errors.py` terminés** (2026-10-13). Reste flake8, à faire par l'utilisateur.
    - 5 vérifications d'erreurs écrites par l'utilisateur, du général au précis : `family` est une liste, `start`/`end` sont des `int`, chaque ligne est une liste, lignes de même taille, valeurs `int`/`float`. Cas limites `[]` et `[[]]` laissés passer (documenté dans le Readme).
    - Points de style restants pour flake8 : 2 lignes vides après l'import, `try :`, `except (...) as error :` et `print (error)` avec espace en trop, ligne du `raise` sur les valeurs trop longue.
    - Concepts vus : liste de listes, `shape`, positions à partir de 0, slicing `[début:fin]` (fin exclue), `.tolist()`, boucle imbriquée, méthode « une règle = un `if not` + un `raise` » dans l'ordre du général au précis.
    - L'utilisateur avait besoin que le slicing soit expliqué depuis zéro : partir des indices d'une liste simple avant les tableaux 2D.
  - ex02 (load my image, `load_image.py`, fonction `ft_load`) : **code, docstring, Readme.md et `test_errors.py` terminés** (2026-10-14). Reste flake8, à faire par l'utilisateur.
    - Charge une image jpg/jpeg avec Pillow (`Image.open`), convertit en tableau numpy, affiche le shape, retourne le tableau. Pas de `main()` (même raisonnement que ex00/ex01 : le fichier à rendre ne contient que la fonction).
    - 3 vérifications d'erreurs : `path` est une `str` (`TypeError`), extension `.jpg`/`.jpeg` via `path.endswith((".jpg", ".jpeg"))` (`ValueError`), fichier existe (`FileNotFoundError`, levée automatiquement par `Image.open()`, pas besoin d'un `if`/`raise` manuel — juste l'ajouter à l'`except`).
    - Concepts vus : image = tableau 3D (lignes, colonnes, canaux RGB), Pillow (`from PIL import Image`), `.endswith()` avec un tuple de suffixes (piège : le 2e argument positionnel n'est pas un autre suffixe mais un indice de début), chemins relatifs calculés depuis le dossier de lancement (pas l'emplacement du script), cache `__pycache__` qui peut faire tourner une vieille version du code.
    - Venv du projet créé à cette session (`venv/` à la racine, numpy + pillow installés).
  - ex03 (zoom on me, `load_image.py` + `zoom.py`) : **code, docstrings, Readme.md terminés** (2026-10-14). Reste flake8.
    - `zoom()` decoupe un carre 400x400 centre sur l'image, sur un seul canal (slicing 3D avec virgules : `image[y0:y1, x0:x1, 0:1]`). Affichage avec `matplotlib.pyplot` (`plt.imshow(..., cmap="gray")` + `plt.show()`), venv complete avec `matplotlib` installe.
    - `zoom.py` a un `main()` (contrairement a `load_image.py`) car il execute du code, pas juste des `def`.
    - `pip` est casse dans le venv (mauvais shebang) : utiliser `python3 -m pip install ...` a la place.
    - Piege vu : `new_image == None` sur un tableau numpy plante (`ValueError: truth value of an array is ambiguous`, comparaison element par element) ; utiliser `is None`.
    - **Changement important fait a la demande de l'utilisateur sur tout le module (ex00 a ex03)** : retrait de tous les `return []` dans les blocs `except`. Le sujet n'impose pas de valeur de retour precise en cas d'erreur, seulement qu'aucune exception ne sorte et qu'un message clair soit affiche. Les fonctions renvoient donc `None` implicitement en cas d'erreur (plus de `return` dans les `except`). Les Readme de ex00/ex01/ex02 ont ete mis a jour en consequence. Pour `zoom()`, le `return new_image` a du etre deplace a l'interieur du `try` (il etait apres le `try`/`except`, ce qui aurait cause un `NameError` si l'exception se declenchait). Dans `zoom.py::main()`, verification du retour de `zoom()` avec `if new_image is None: return` avant d'utiliser le resultat.
  - ex04 (rotate me, `load_image.py` + `rotate.py`) : **code, docstrings, Readme.md terminés** (2026-10-14). Reste flake8.
    - `rotate()` transpose un tableau 3D a la main (interdiction du sujet d'utiliser `.T`/`np.transpose()`) : boucle imbriquee sur les indices (`range(height)`/`range(width)`, pas sur les valeurs), ecrit `new_image[j][i] = image[i][j][0]` dans un nouveau tableau cree avec `np.zeros((largeur, hauteur))`.
    - Reutilise `zoom()` de `ex03` pour le decoupage avant transposition.
    - Gestion d'erreurs : `image` doit etre un `ndarray` (`TypeError`) et avoir `ndim == 3` (`ValueError`, sinon `image[i][j][0]` plante si `image` est deja en 2D).
    - Concepts vus : difference entre boucler sur les valeurs (`for x in liste`) et sur les indices (`for i in range(len(liste))`) pour pouvoir lire ET ecrire a une position precise ; `image[i][j]` est une liste a 1 element `[167]` tant qu'on ne prend pas `[0]` dedans (sinon `ValueError: setting an array element with a sequence`) ; `.ndim` (nombre de dimensions) different de `.shape` (taille de chaque dimension) ; `np.zeros()` cree des `float` par defaut.
  - ex05 (pimp my image, `load_image.py` + `pimp_image.py`) : **code, docstrings, Readme.md terminés** (2026-10-14). Reste flake8. **Module Array (ex00 à ex05) termine.**
    - 5 filtres (`ft_invert`, `ft_red`, `ft_green`, `ft_blue`, `ft_grey`), chacun limite a certains operateurs par le sujet (`=`/`+`/`-`/`*` pour invert, `=`/`*` pour red, `=`/`-` pour green, `=` pour blue, `=`/`/` pour grey). Chaque fonction affiche son resultat avec `plt.imshow`/`plt.show` (le sujet l'exige explicitement : "you must display the images transformed", sur une page du PDF qu'il a fallu repérer apres coup).
    - Bug trouve et corrige par l'utilisateur lui-meme (avec aide) : les fonctions modifiaient `array` en place, et `tester.py` appelle les 5 fonctions a la suite sur le **meme** tableau → les filtres s'accumulaient (ex: apres `ft_red`, l'image etait deja quasi noire pour les filtres suivants). Fix : `array = array.copy()` en debut de chaque fonction qui fait `array[:, :, i] = ...`.
    - `ft_grey` utilise `array.sum(axis=2)` pour contourner l'interdiction de `+` (c'est une fonction, pas l'operateur).
    - `show_filters.py` (bonus, pas demande par le sujet) : affiche les 6 versions cote a cote dans une seule fenetre pour comparer.
    - Pas de gestion d'erreurs sur cet exercice : le sujet ne la demande pas explicitement, contrairement aux precedents.
- Module 2 (DataTable) : **en cours**.
  - venv et dossier `Python-2-DataTable/csv/` recrees le 2026-10-26 (avaient disparu entre les sessions, probablement machine reinitialisee). Venv : numpy, pillow, matplotlib, pandas installes. L'utilisateur a ajoute `life_expectancy_years.csv` dans `csv/`. Il manque encore `population_total.csv` (ex02) et `income_per_person_gdppercapita_ppp_inflation_adjusted.csv` (ex03), a demander/verifier quand on y arrivera.
  - ex00 (Load my Dataset, `load_csv.py`, fonction `load`) : **code, docstring, Readme.md termines** (2026-10-26). Reste flake8.
    - `pd.read_csv(path)` charge le CSV en `DataFrame`, `.shape` affiche les dimensions (`Loading dataset of dimensions (195, 302)`), retourne le dataset (pas juste le shape).
    - 3 erreurs gerees : `path` pas une `str` (`TypeError`), extension differente de `.csv` (`ValueError`), fichier introuvable (`FileNotFoundError`, levee automatiquement par `pd.read_csv`). Retour `None` explicite (le sujet le demande litteralement, contrairement au module Array ou c'etait une convention).
    - Erreur typique corrigee par l'utilisateur lui-meme : `pd.read_csv` sans parentheses (donnait la fonction, pas un DataFrame).
    - Concepts vus : CSV, pandas/`DataFrame` vs "dataset" (terme generique), `import pandas as pd`, `.shape` sur un DataFrame, affichage automatique d'un DataFrame par `print()`.
  - ex01 a ex03 : pas commences (dossiers crees avec Readme « À compléter », pas de squelette donne par le sujet pour ceux-la).
- Modules 3, 4 : pas commencés.

## Préférences de l'utilisateur (à respecter)
- Avancer **une petite étape à la fois**, avec une explication simple, sans aller trop vite ni trop loin. Ne jamais supposer qu'un terme (slicing, shape...) est connu : l'expliquer d'abord avec un exemple minimal. Dire le « pourquoi » de chaque consigne.
- Pour la gestion d'erreurs, il veut apprendre la méthode pour la refaire seul : une règle à la fois, avec le message anglais et le type d'erreur (`TypeError` si le type est mauvais, `ValueError` si la valeur est mauvaise).
- Dire quoi faire et pourquoi, **sans donner le code** tant qu'il ne le demande pas explicitement. S'il le demande, donner la réponse avec une explication courte.
- Réponses courtes, pas de longs blocs. Ne pas lui demander de tester dans un terminal Python interactif : il lance seulement `py tester.py`.
- Il vient du C : les analogies avec le C l'aident.
- Il ne veut pas parler de flake8 pour l'instant, il le fera lui-même à la fin.
- Les messages d'erreur et les docstrings sont en anglais, courts. Lui donner le texte des messages à chaque fois.
- Le venv du projet est dans `venv/` à la racine (numpy installé). Le Readme de chaque exercice suit le style de `Python-0-Starting/ex04/Readme.md` et `ex06/Readme.md`.
- Mise en page markdown claire dans les réponses (titres, listes, tableaux, blocs de code) : il a reproché un message trop plat/compressé. "Court" ne veut pas dire sacrifier la clarté de la mise en forme.

## Prochaine étape
Passer a l'ex01 du module DataTable ("draw my country") : copier
`load_csv.py` depuis `ex00` (meme pattern que `load_image.py` dans le
module Array), creer `aff_life.py`, charger `life_expectancy_years.csv`
(deja present dans `csv/`), et afficher le graphe d'esperance de vie pour
le pays du campus de l'utilisateur (demander lequel si pas encore su).
Pas de squelette/prototype donne par le sujet pour `aff_life.py`, juste
une description + un graphe d'exemple (France).

Rappel : `population_total.csv` (ex02) et
`income_per_person_gdppercapita_ppp_inflation_adjusted.csv` (ex03) ne sont
pas encore dans `csv/`, a demander a l'utilisateur le moment venu.

À faire aussi : commiter et pousser les fichiers de ex00 à ex05 du module Array et ex00 du module DataTable, et passer flake8 dessus.