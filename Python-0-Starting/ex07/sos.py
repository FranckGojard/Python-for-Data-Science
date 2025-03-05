import sys


def checkString(element: str) -> bool:
    tmp: str = element
    tmp = tmp.replace(" ", "")
    return tmp.isalnum()


def dictMorse() -> dict:
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
    return morse_dict


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

    morse_dict = dictMorse()
    print(ac)


if __name__ == "__main__":
    main()
