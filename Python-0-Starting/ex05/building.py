import sys

def main():
    try:
        lenArg = len(sys.argv)
        if lenArg == 1:
            av = input("One argument requiered :")
        elif lenArg > 2:
            raise AssertionError("more than one argument is provided")
        else:
            av = sys.argv[1]
    except AssertionError as e:
        print(f"AssertionError: {e}")

    
        
    
    
if __name__ == "__main__":
    main()
