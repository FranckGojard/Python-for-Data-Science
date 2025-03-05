import sys


def countText(av1: str, my_dict: dict) -> dict:
    """
    Compte différents types de caractères dans une chaîne donnée et met à jour le dictionnaire fourni.

    Paramètres :
    av1 (str) : La chaîne à analyser.
    my_dict (dict) : Un dictionnaire contenant les comptages de différents types de caractères.

    Retour :
    dict : Dictionnaire mis à jour avec les comptages des lettres majuscules, lettres minuscules,
           chiffres, ponctuation, espaces et le nombre total de caractères.
    """
    for c in av1:
        my_dict["nbAll"] += 1
        if c.islower():
            my_dict["nbLowerCase"] += 1
        elif c.isdigit():
            my_dict["nbDigits"] += 1
        elif c.isupper():
            my_dict["nbUpperCase"] += 1
        elif c in ".,;:!?-()[]":
            my_dict["nbPonctuation"] += 1
        elif c == ' ':
            my_dict["nbSpace"] += 1
    return (my_dict)


def printResult(my_dict: dict):
    """
    Affiche les résultats de l'analyse du texte stockés dans le dictionnaire fourni.

    Paramètres :
    my_dict (dict) : Un dictionnaire contenant le comptage des différents types de caractères
                     tels que les lettres majuscules, lettres minuscules, ponctuation, etc.
    """
    print(f"The text contains {my_dict['nbAll']} characters:")
    print(f"{my_dict['nbUpperCase']} upper letters")
    print(f"{my_dict['nbLowerCase']} lower letters")
    print(f"{my_dict['nbPonctuation']} punctuation marks")
    print(f"{my_dict['nbSpace']} spaces")
    print(f"{my_dict['nbDigits']} digits")


def main():
    """
    Fonction principale qui gère les entrées, appelle les fonctions countText et printResult,
    et affiche l'analyse du texte fourni.

    Elle gère les arguments en ligne de commande et utilise un texte saisi par l'utilisateur
    si aucun argument n'est fourni.
    """
    ac: int = len(sys.argv)
    my_dict = {
        "nbAll": 0,
        "nbUpperCase": 0,
        "nbLowerCase": 0,
        "nbPonctuation": 0,
        "nbSpace": 0,
        "nbDigits": 0
    }
    if ac > 2 :
        print("AssertionError: more than one argument is provided")
        return 1
    else:
        if ac == 2:
            av1: str = sys.argv[1]
        else:
            av1 = input("What is the text to count?\n")
        my_dict = countText(av1, my_dict)
        printResult(my_dict)


if __name__ == "__main__":
    main()
