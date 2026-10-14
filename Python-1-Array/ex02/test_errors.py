from load_image import ft_load


def main():
    """Run error cases for ft_load."""
    print("--- valid case ---")
    print(ft_load("../jpeg/landscape.jpg"))

    print("--- error cases ---")
    print("path not a string:", ft_load(42))
    print("wrong extension:", ft_load("photo.png"))
    print("file does not exist:", ft_load("inexistant.jpg"))


if __name__ == "__main__":
    main()
