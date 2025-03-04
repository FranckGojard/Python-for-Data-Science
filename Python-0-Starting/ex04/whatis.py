import sys

argc = len(sys.argv)
if argc == 2:
    try:
        arg1 = int(sys.argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        sys.exit()
    if arg1 % 2 == 0:
        print("I'm Even.")
    else :
        print("I'm Odd.")
else :
    if argc > 2 :
        print("AssertionError: more than one argument is provided")