import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Return the BMI of each person from height (m) and weight (kg)."""
    try :
        if len(height) != len(weight):
            raise ValueError("height and weight must have the same length")
        for value in height + weight:
            if not isinstance(value, (int, float)):
                raise TypeError("height and weight must contain only integers or floats")
            if value <= 0:
                raise ValueError("height and weight must be greater than 0")
        a = np.array(weight)
        b = np.array(height)
        result = (a / b**2)
        return result.tolist()
    except (ValueError, TypeError) as error:
        print(error)
        return[]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a list of booleans: True if the BMI is above the limit."""
    try:
        if not isinstance(bmi, list):
            raise TypeError("bmi must be a list")
        if not isinstance(limit, int):
            raise TypeError("limit must be only integers")
        for value in bmi:
            if not isinstance(value, (int, float)):
                raise TypeError("bmi must contain only integers or floats")
        imc = np.array(bmi)
        result = imc > limit
        return result.tolist()
    except TypeError as error:
        print(error)
        return []
