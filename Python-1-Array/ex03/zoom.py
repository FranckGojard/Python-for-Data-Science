from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

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
    """Load animal.jpeg, print its info, and display a zoomed version."""
    image = ft_load("../jpeg/animal.jpeg")
    print(image)
    new_image = zoom(image)
    if new_image is None:
        return
    print(f"The new shape of image is: {new_image.shape} or ({new_image.shape[0]}, {new_image.shape[1]})")
    print(new_image)
    plt.imshow(new_image, cmap="gray")
    plt.show()

if __name__ == "__main__":
    main()