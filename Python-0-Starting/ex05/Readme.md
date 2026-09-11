 # Exercice 05 - Building

 ## Objectif

 Creer un programme qui recoit un texte et compte ses caracteres :

 - lettres majuscules ;
 - lettres minuscules ;
 - signes de ponctuation ;
 - chiffres ;
 - espaces ;
 - nombre total de caracteres.

 ## Arguments

 Le programme accepte au maximum un texte en argument :

 ```bash
 python3 building.py "Hello World!"
 ```

 `sys.argv` contient les arguments du terminal. Le nom du fichier est toujours
 present dans `sys.argv[0]`. Le texte fourni par l'utilisateur se trouve donc
 dans `sys.argv[1]`.

 Si aucun argument n'est fourni, le programme demande le texte avec `input()` :

 ```text
 What is the text to count?
 ```

 Si plusieurs arguments sont fournis, le programme affiche une erreur.

 ## Comptage

 Il faut parcourir le texte caractere par caractere avec une boucle. Chaque
 compteur commence a `0` et augmente de `1` lorsqu'un caractere correspond a sa
 categorie.

 Methodes utiles pour les chaines :

 - `isupper()` : verifie si le caractere est une majuscule ;
 - `islower()` : verifie si le caractere est une minuscule ;
 - `isdigit()` : verifie si le caractere est un chiffre ;
 - `isspace()` : verifie si le caractere est un espace.

 `len()` permet de compter le nombre total de caracteres.

 ## Structure demandee

 A partir de cet exercice, le programme doit contenir une fonction `main()` et
 ne doit pas executer sa logique directement dans le scope global.

 ```python
 def main():
	 """Description de la fonction."""
	 pass


 if __name__ == "__main__":
	 main()
 ```

 Chaque fonction doit avoir une docstring. Les erreurs demandees par le sujet
 doivent etre gerees, notamment avec `raise` et `try/except` pour le cas de
 plusieurs arguments.

 ## Tests

 Depuis le dossier `ex05` :

 ```bash
 python3 building.py "Hello World!"
 python3 building.py
 python3 building.py "Hello" "World"
 ```
