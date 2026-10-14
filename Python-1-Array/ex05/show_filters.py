from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def main():
    """Display the original image next to each of the 5 filters."""
    array = ft_load("../jpeg/landscape.jpg")

    filters = [
        ("original", array.copy()),
        ("invert", ft_invert(array.copy())),
        ("red", ft_red(array.copy())),
        ("green", ft_green(array.copy())),
        ("blue", ft_blue(array.copy())),
        ("grey", ft_grey(array.copy())),
    ]

    _, axes = plt.subplots(2, 3, figsize=(10, 6))
    for ax, (title, image) in zip(axes.flat, filters):
        ax.imshow(image)
        ax.set_title(title)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
