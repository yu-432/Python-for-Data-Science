from numpy import array
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> array:
    """画像を読み込み、numpy配列として返す"""
    try:
        with Image.open(path) as img:
            img = img.convert("RGB")
            np_array = array(img)
            print("The shape of image is:", np_array.shape)

            return np_array

    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for file '{path}'.")
    except OSError:
        print(f"Error: Cannot open file '{path}'.\
            It may not be a valid image.")
    except UnidentifiedImageError:
        print(f"Error: The image file '{path}'\
            is corrupted or in an unsupported format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return array([])


def main():
    """メイン関数"""
    img_array = ft_load("animal.jpeg")
    print(img_array)
    img_array = ft_load("no_exist.jpg")
    print(img_array)


if __name__ == "__main__":
    main()
