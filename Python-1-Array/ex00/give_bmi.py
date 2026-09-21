import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    a = np.array(weight)
    b = np.array(height)
    result = (a / b**2)
    return result.tolist()

# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#     # your code here

