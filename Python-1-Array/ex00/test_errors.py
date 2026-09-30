from give_bmi import give_bmi, apply_limit


def main():
    """Run error cases for give_bmi and apply_limit."""
    print("--- give_bmi ---")
    print("different lengths:", give_bmi([1.7], [60, 70]))
    print("text in height:", give_bmi(['a'], [60]))
    print("text in weight:", give_bmi([1.7], ['b']))
    print("height is 0:", give_bmi([0], [60]))
    print("weight is 0:", give_bmi([1.7], [0]))
    print("negative height:", give_bmi([-1.7], [60]))
    print("not a list:", give_bmi(5, 6))
    print("empty lists:", give_bmi([], []))

    print("--- apply_limit ---")
    print("bmi not a list:", apply_limit(5, 26))
    print("limit not an int:", apply_limit([22.5], 'abc'))
    print("text in bmi:", apply_limit(['a', 22], 26))
    print("bmi equal to limit:", apply_limit([26], 26))


if __name__ == "__main__":
    main()
