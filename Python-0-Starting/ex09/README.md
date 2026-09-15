 # ft_package

## Objectif

`ft_package` est un petit package Python qui contient la fonction
`count_in_list`.

Cette fonction compte le nombre d'apparitions d'un element dans une liste.

## Utilisation

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

Resultat :

```text
2
0
```

## Structure du projet

```text
ex09/
├── LICENSE
├── Readme.md
├── pyproject.toml
├── ft_package/
│   └── __init__.py
└── dist/
	├── ft_package-0.0.1.tar.gz
	└── ft_package-0.0.1-py3-none-any.whl
```

## Installation depuis les sources

Depuis le dossier `ex09`, le package peut etre installe avec :

```bash
python3 -m pip install .
```

## Installation depuis les archives

Le sujet demande que les deux archives puissent etre installees :

```bash
python3 -m pip install ./dist/ft_package-0.0.1.tar.gz
python3 -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

- `.tar.gz` est une archive source ;
- `.whl` est une archive prete a installer.

## Construction du package

Pour construire les archives dans `dist/` :

```bash
python3 -m build
```

Le fichier `pyproject.toml` contient le nom, la version, la description et les
informations necessaires a la construction du package.

## Verification de l'installation

Pour afficher les informations du package installe :

```bash
python3 -m pip show ft_package
```

Pour tester la fonction :

```bash
python3 -c "from ft_package import count_in_list; print(count_in_list(['toto', 'tata', 'toto'], 'toto')); print(count_in_list(['toto', 'tata', 'toto'], 'tutu'))"
```

Resultat attendu :

```text
2
0
```
