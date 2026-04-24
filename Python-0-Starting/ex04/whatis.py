import sys

try:
    av = sys.argv
    if len(av) < 2:
        exit()
    elif len(av) > 2:
        print("AssertionError: more than one argument is provided")
        exit()
    nb = int(av[1])
    if nb % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer")
