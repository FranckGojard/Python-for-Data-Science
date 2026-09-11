import sys


def main():
    """Count the character categories in the input text."""
    try:
        upper_count = 0
        lower_count = 0
        punctuation_count = 0
        digit_count = 0
        space_count = 0
        number_of_arg = len(sys.argv)
        if number_of_arg > 2:
            raise AssertionError()
        else:
            if number_of_arg == 1:
                arg = input("What is the text to count?\n")
            else:
                arg = sys.argv[1]
            len_of_str = len(arg)
            for char in arg:
                if char.islower():
                    lower_count += 1
                elif char.isdigit():
                    digit_count += 1
                elif char.isupper():
                    upper_count += 1
                elif char.isspace():
                    space_count += 1
                else:
                    punctuation_count += 1
            print(f"The text contains {len_of_str} characters:\n"
                  f"{upper_count} upper letters\n"
                  f"{lower_count} lower letters\n"
                  f"{punctuation_count} punctuation marks\n"
                  f"{space_count} spaces\n"
                  f"{digit_count} digits")
    except AssertionError:
        print("AssertionError: more than one argument is provided")


if __name__ == "__main__":
    main()
