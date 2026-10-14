import numpy as np
from PIL import Image

def ft_load(path: str):
    """Load a jpg/jpeg image file and return its pixels as a numpy array."""
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        if not path.endswith((".jpg", ".jpeg")):
            raise ValueError("file format not supported")
        land = Image.open(path)
        land_array = np.array(land)
        print("The shape of image is:", land_array.shape)
        return land_array
    except (TypeError, ValueError, FileNotFoundError) as error:
        print(error)