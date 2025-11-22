from numpy import array, mean
from matplotlib.pyplot import imshow, show
from load_image import ft_load


def zoom_img(img_array: array) -> array:
    """画像配列を400x400にズームする"""
    new_img = img_array[100: 500, 450: 850]

    return new_img.reshape((400, 400, 1))


def rgb_to_gray(img_array: array) -> array:
    """RGB画像配列をグレースケールに変換する"""
    return mean(img_array, axis=2).astype(int)


def main():
    """メイン関数"""
    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)

        if img_array.size == 0:
            raise ValueError("Loaded image array is empty.")
        if img_array.shape[0] < 500 or img_array.shape[1] < 850:
            raise ValueError("Image is too small to zoom to 400x400\
                from the specified coordinates.")

        gray_img = zoom_img(rgb_to_gray(img_array))

        print("New shape after slicing:", gray_img.shape)
        print(gray_img)

        imshow(gray_img, cmap='gray')
        show()

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyboardInterrupt:
        print("Process interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
