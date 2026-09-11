import sys

number_of_argument = len(sys.argv)
if number_of_argument > 2:
    print("AssertionError: more than one argument is provided") 
elif number_of_argument == 2:
    arg = sys.argv[1]
    try:
        number = int(arg)
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")