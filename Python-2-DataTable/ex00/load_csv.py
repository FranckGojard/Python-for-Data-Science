import pandas as pd

def load(path: str):
    """Load a CSV file, print its dimensions, and return the dataset."""
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string")
        if not path.endswith(".csv"):
            raise ValueError("File format not supported")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except (TypeError, FileNotFoundError, ValueError) as error:
        print(error)
        return None
