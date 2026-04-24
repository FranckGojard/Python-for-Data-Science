# Ex01 - First Use Of Package

## Sujet

Le but de cet exercice est d'afficher le temps actuel dans un format precis.

Fichier a rendre :

- `format_ft_time.py`

Le programme doit afficher deux lignes :

```text
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation
Oct 21 2022
```

Les valeurs changent selon le moment ou le programme est lance.

## Notions Apprises

- Un module est du code Python deja ecrit que l'on peut importer.
- `time()` permet de recuperer le nombre de secondes depuis le 1 janvier 1970.
- Cette date de reference s'appelle l'Epoch Unix.
- `datetime.now()` permet de recuperer la date et l'heure actuelles.
- Une f-string permet d'inserer et de formatter des variables dans une chaine.
- `strftime` permet de formatter une date.

## Formats Utiles

Dans une f-string :

```python
{value:,}
```

Affiche un nombre avec des separateurs de milliers.

```python
{value:.2e}
```

Affiche un nombre en notation scientifique avec deux chiffres apres le point.

Avec `strftime` :

```python
%b
```

Affiche le mois abrege, par exemple `Jan`, `Feb`, `Mar`, `Apr`.

## Points Importants

La notation scientifique permet d'ecrire un tres grand nombre de maniere plus
compacte.

Exemple :

```text
1.67e+09 = 1.67 * 10^9
```

`==` et les classes ne sont pas encore le sujet ici : pour cet exercice, il faut
surtout savoir importer les bons outils et formatter l'affichage.

## Test

Depuis la racine du projet :

```bash
python3 Python-0-Starting/ex01/format_ft_time.py | cat -e
```
