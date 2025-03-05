from ft_filter import ft_filter
import sys


def main():
    """
    Fonction principale qui traite les arguments de la ligne de commande et filtre les mots dans une chaîne.

    Ce programme attend exactement deux arguments :
        1. Une chaîne de caractères (S) - la chaîne d'entrée contenant des mots à filtrer.
        2. Un entier (N) - la longueur minimale que doivent dépasser les mots pour être inclus dans le résultat.

    La fonction effectue les étapes suivantes :
    1. Elle vérifie si exactement deux arguments sont fournis. Si ce n'est pas le cas, une AssertionError est levée.
    2. Elle tente de convertir le deuxième argument en entier. Si cela échoue, une ValueError est capturée et un message d'erreur est affiché.
    3. Elle découpe la chaîne en une liste de mots.
    4. Elle filtre les mots en vérifiant si leur longueur est supérieure à la valeur de l'entier (N).
    5. La liste des mots filtrés est ensuite affichée.

    Le programme se termine avec un message d'erreur si les conditions ne sont pas remplies ou si une exception se produit.

    Exceptions levées :
        AssertionError : Si le nombre d'arguments est incorrect ou si le deuxième argument ne peut pas être converti en entier.
        ValueError : Si le deuxième argument n'est pas un entier valide.
    """
    ac: int = len(sys.argv)
    try:
        if ac != 3:
            raise AssertionError("Exactly two arguments \
                (string and integer) are required.")
        my_arg: tuple = (sys.argv[1], int(sys.argv[2]))
    except ValueError:
        print("AssertionError: the arguments are bad")
        exit(1)
    except AssertionError:
        print("AssertionError: the arguments are bad")
        exit(1)
    S = my_arg[0]
    N = my_arg[1]

    words: list = S.split()
    filtered = list(ft_filter(lambda word: len(word) > N, words))
    print(filtered)


if __name__ == "__main__":
    main()
