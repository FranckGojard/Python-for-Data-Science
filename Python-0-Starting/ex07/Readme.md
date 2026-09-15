# Exercice 07 - Dictionaries SoS

## Sujet

Le but de cet exercice est de creer un programme qui transforme une chaine de
caracteres en code Morse.

Fichier a rendre :

- `sos.py`

Le programme doit recevoir exactement une chaine en argument.

## Fonctionnement du code Morse

Chaque lettre ou chiffre correspond a une suite de points `.` et de tirets `-`.

Exemples :

```text
S -> ...
O -> ---
A -> .-
1 -> .----
```

Les codes Morse de caracteres differents sont separes par un espace.

```text
SOS -> ... --- ...
```

Un espace dans le texte original est represente par `/`.

```text
SOS 123 -> ... --- ... / .---- ..--- ...--
```

## Dictionnaire

Le programme doit utiliser un dictionnaire pour stocker la correspondance entre
un caractere et son code Morse.

Le dictionnaire contient :

- les lettres de `A` a `Z` ;
- les chiffres de `0` a `9` ;
- l'espace.

Le caractere recu peut etre en minuscule ou en majuscule. Le texte est donc
transforme en majuscules avant la recherche dans le dictionnaire.

## Notions utilisees

### `sys.argv`

Les arguments du terminal sont stockes dans `sys.argv`.

Quand on lance :

```bash
python3 sos.py sos
```

Python recoit notamment :

```python
["sos.py", "sos"]
```

- `sys.argv[0]` contient le nom du fichier ;
- `sys.argv[1]` contient la chaine a convertir.

Le sujet demande donc exactement un argument apres le nom du fichier.

### `upper()`

`upper()` transforme les lettres en majuscules :

```text
sos -> SOS
```

Les chaines Python ne sont pas modifiees directement. Il faut conserver le
resultat retourne par `upper()`.

### Comprehension de liste

La comprehension de liste parcourt chaque caractere et recupere son code dans le
dictionnaire.

```text
texte       : SOS
liste Morse : [..., ---, ...]
```

### `join()`

`join()` assemble les codes Morse de la liste avec un espace entre eux :

```text
["...", "---", "..."] -> "... --- ..."
```

## Erreurs

Si le nombre d'arguments est different de un, le programme doit afficher :

```text
AssertionError: the arguments are bad
```

Si la chaine contient un caractere qui n'est pas dans le dictionnaire, le meme
message doit etre affiche.

Les caracteres pris en charge sont les lettres, les chiffres et les espaces.
La ponctuation et les autres caracteres speciaux ne sont pas prevus par le
sujet.

## Regles a respecter

- utiliser un dictionnaire pour le code Morse ;
- ne pas mettre le dictionnaire en variable globale ;
- avoir une fonction `main()` ;
- proteger l'appel avec `if __name__ == "__main__":` ;
- ajouter une docstring a chaque fonction ;
- gerer les erreurs demandees sans laisser de traceback ;
- utiliser des imports explicites ;
- utiliser Python 3.10 ;
- respecter la norme avec `flake8`.

## Tests principaux

Depuis le dossier `ex07` :

```bash
python3 sos.py sos
python3 sos.py SOS
python3 sos.py aaa
python3 sos.py "sos 123"
python3 sos.py 'h$llo'
python3 sos.py
python3 sos.py sos test
```

Resultats attendus :

```text
... --- ...
... --- ...
.- .- .-
... --- ... / .---- ..--- ...--
AssertionError: the arguments are bad
AssertionError: the arguments are bad
AssertionError: the arguments are bad
```

## Verification de la docstring

```bash
python3 -c "import sos; print(sos.main.__doc__)"
```
