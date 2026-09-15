import sys

def main():
    """Convert a string into Morse code."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError
        morse_dict = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..",
    "9": "----.",
    " ": "/"}
        code = sys.argv[1]
        code = code.upper()
        morse = [morse_dict[element] for element in code]
        result = " ".join(morse)
        print(result)
    except (AssertionError, KeyError):
        print("AssertionError: the arguments are bad")

if __name__ == "__main__":
    main()