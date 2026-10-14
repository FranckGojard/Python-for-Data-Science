from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def rotate(image: np.ndarray):
    """Transpose a 3D image array by hand, without any library function."""
    try:
        if not isinstance(image, np.ndarray):
            raise TypeError("image must be a ndarray")
        if image.ndim != 3:
            raise ValueError("image must have 3 dimensions")
        height = image.shape[0]
        width = image.shape[1]
        new_image = np.zeros((width, height))
        for i in range(height):
            for j in range(width):
                new_image[j][i] = image[i][j][0]
        return new_image
    except (TypeError, ValueError) as error:
        print(error)

def zoom(image: np.ndarray):
    """Crop a 400x400 area at the center of the image, keeping one channel."""
    try:
        if not isinstance(image, np.ndarray):
            raise TypeError("image must be a ndarray")
        center_y = image.shape[0] // 2
        center_x = image.shape[1] // 2
        new_image = image[center_y - 200:center_y + 200,
                        center_x - 200:center_x + 200, 0:1]
        return new_image
    except TypeError as error:
        print(error)

def main():
    """Load animal.jpeg, crop and transpose it, then display the result."""
    image = ft_load("../jpeg/animal.jpeg")
    print(image)
    new_image = zoom(image)
    if new_image is None:
        return
    new_image_transpose = rotate(new_image)
    if new_image_transpose is None:
        return
    print("New shape after Transpose:", new_image_transpose.shape)
    print(new_image_transpose)
    plt.imshow(new_image_transpose, cmap="gray")
    plt.show()

if __name__ == "__main__":
    main()