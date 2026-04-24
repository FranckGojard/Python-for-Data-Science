# Ex00 - First Python Script

## Sujet

Le but de cet exercice est de modifier quatre objets Python pour afficher les
salutations demandées par le sujet.

Fichier a rendre :

- `Hello.py`

Objets de depart :

```python
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
```

Sortie attendue :

```text
['Hello', 'World!']
('Hello', 'France!')
{'Hello', 'Paris!'}
{'Hello': '42Paris!'}
```

## Notions Apprises

- Une `list` est modifiable.
- Un `tuple` est immuable : on ne modifie pas directement ses elements.
- Un `set` n'a pas d'ordre garanti et ne s'utilise pas avec des index.
- Un `dict` fonctionne avec des paires cle/valeur.
- Python commence les index a `0`.
- `print` ajoute un retour a la ligne par defaut.

## Points Importants

Pour modifier le deuxieme element d'une liste, on utilise l'index `1`.

Un `tuple` ne peut pas etre modifie element par element. Pour changer son
contenu, on remplace l'objet par un nouveau tuple.

Un `set` peut s'afficher dans un ordre different selon les executions. Ce n'est
pas forcement une erreur.

Pour modifier une valeur dans un dictionnaire, on utilise sa cle.

## Test

Depuis la racine du projet :

```bash
python3 Python-0-Starting/ex00/Hello.py | cat -e
```

`cat -e` permet de voir les fins de ligne avec `$` et de reperer les espaces
en trop.
