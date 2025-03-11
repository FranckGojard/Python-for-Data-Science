import sys


def checkString(element: str) -> bool:
    """
    La fonction prend une chaîne element et renvoie
    True si elle ne contient que des caractères
    alphanumériques, sinon False.
    """
    tmp: str = element
    tmp = tmp.replace(" ", "")
    return tmp.isalnum()


def dictMorse(argv: str) -> dict:
    """
    La fonction prend une chaîne argv
    et renvoie une chaîne traduite en Morse
    à partir de argv.
    """
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }
    result = ""
    txt = argv.upper()
    for c in txt:
        if c in morse_dict:
            result += morse_dict[c] + " "
    return result


def main():
    ac: int = len(sys.argv)
    try:
        if ac != 2:
            raise AssertionError("AssertionError: the arguments are bad")
        if not checkString(sys.argv[1]):
            raise AssertionError("AssertionError: the arguments are bad")
    except AssertionError as e:
        print(e)
        exit(1)
    result = ""
    result = dictMorse(sys.argv[1])
    print(result)


if __name__ == "__main__":
    main()
