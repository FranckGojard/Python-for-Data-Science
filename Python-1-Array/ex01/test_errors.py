from array2D import slice_me


def main():
    """Run error cases for slice_me."""
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]

    print("--- valid cases ---")
    print("0 to 2:", slice_me(family, 0, 2))
    print("1 to -2:", slice_me(family, 1, -2))
    print("end after the last row:", slice_me(family, 2, 99))

    print("--- error cases ---")
    print("family not a list:", slice_me(5, 0, 1))
    print("start is text:", slice_me(family, 'a', 1))
    print("end is a float:", slice_me(family, 0, 1.5))
    print("1D list:", slice_me([1, 2, 3], 0, 1))
    print("row not a list:", slice_me([[1, 2], 3], 0, 1))
    print("rows of different sizes:", slice_me([[1, 2], [3]], 0, 1))
    print("text in a row:", slice_me([['a', 'b']], 0, 1))
    print("None in a row:", slice_me([[None, 2]], 0, 1))

    print("--- edge cases ---")
    print("empty list:", slice_me([], 0, 1))
    print("empty row:", slice_me([[]], 0, 1))


if __name__ == "__main__":
    main()
