from numpy import array, sum
from matplotlib.pyplot import imshow, show
from load_image import ft_load


def show_img_info(array) -> None:
    """Displays the image array using matplotlib."""
    print(array)
    imshow(array)
    show()


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    try:
        inverted_array = 255 - array
        show_img_info(inverted_array)
        return inverted_array
    
    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


def ft_red(array) -> array:
    """Red the color of the image received."""
    try:
        red_array = array * [1, 0, 0]
        show_img_info(red_array)
        return red_array

    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


def ft_green(array) -> array:
    """Green the color of the image received."""
    try:
        green_array = array.copy()
        green_array[:, :, 0] = array[:, :, 0] - array[:, :, 0]
        green_array[:, :, 2] = array[:, :, 2] - array[:, :, 2]
        show_img_info(green_array)
        return green_array

    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


def ft_blue(array) -> array:
    """Blue the color of the image received."""
    try:
        blue_array = array.copy()
        blue_array[:, :, 0] = 0
        blue_array[:, :, 1] = 0
        show_img_info(blue_array)
        return blue_array

    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


def ft_grey(array) -> array:
    """Grey the color of the image received."""
    try:
        gray_val_array = sum(array, axis=2)
        gray_array = array.copy()

        gray_array[:, :, 0] = gray_val_array / 3
        gray_array[:, :, 1] = gray_val_array / 3
        gray_array[:, :, 2] = gray_val_array / 3

        show_img_info(gray_array)
        return gray_array

    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """メイン関数"""
    try:
        img_array = ft_load("landscape.jpeg")
        print(img_array)

        if img_array.size == 0:
            raise ValueError("Loaded image array is empty.")
        if img_array.shape[0] < 500 or img_array.shape[1] < 850:
            raise ValueError("Image is too small to zoom to 400x400 from the specified coordinates.")

        invert_img = ft_invert(img_array)
        imshow(invert_img, cmap='gray')
        show()
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
