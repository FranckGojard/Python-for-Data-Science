import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of a 2D list and return it sliced from start to end."""
    try :
        if not isinstance(family, list):
            raise TypeError("family must be a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("start and end must be integers")
        for row in family:
            if not isinstance(row, list):
                raise TypeError("each row of family must be a list")
        for row in family:
            if len(row) != len(family[0]):
                raise ValueError("all rows must have the same length")
            for value in row:
                if not isinstance(value, (int, float)):
                    raise TypeError("family must contain only integers or floats")
        t = np.array(family)
        print("My shape is :", t.shape)
        sliced = t[start:end]
        print("My new shape is :", sliced.shape)
        return sliced.tolist()
    except (TypeError, ValueError) as error :
        print (error)
        return []