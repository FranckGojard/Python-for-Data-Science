import matplotlib.pyplot as plt


def ft_invert(array):
    """Invert the color of the image received."""
    array = 255 - array
    plt.imshow(array)
    plt.show()
    return array


def ft_red(array):
    """Keep only the red channel of the image received."""
    array = array.copy()
    array[:, :, 1] = 0
    array[:, :, 2] = 0
    plt.imshow(array)
    plt.show()
    return array


def ft_green(array):
    """Keep only the green channel of the image received."""
    array = array.copy()
    array[:, :, 0] = 0
    array[:, :, 2] = 0
    plt.imshow(array)
    plt.show()
    return array


def ft_blue(array):
    """Keep only the blue channel of the image received."""
    array = array.copy()
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    plt.imshow(array)
    plt.show()
    return array


def ft_grey(array):
    """Convert the image to greyscale by averaging the 3 channels."""
    array = array.copy()
    grey = array.sum(axis=2) / 3
    array[:, :, 0] = grey
    array[:, :, 1] = grey
    array[:, :, 2] = grey
    plt.imshow(array)
    plt.show()
    return array
