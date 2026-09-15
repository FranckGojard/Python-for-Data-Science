import sys
from ft_filter import ft_filter

def main():
    """Read the arguments and display words longer than the given number."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError
        n = int(sys.argv[2])
        words = sys.argv[1]
        words_split = words.split()
        condition = lambda arg : len(arg) > n
        result = ft_filter(condition, words_split)
        print(list(result))

    except (AssertionError, ValueError):
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()