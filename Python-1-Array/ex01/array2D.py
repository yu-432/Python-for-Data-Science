from numpy import array


def slice_me(family: list, start: int, end: int) -> list:
    """2D配列の大きさを表示して、スライスを返す"""
    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list.")

        try:
            new_family: tuple = array(family)
        except ValueError:
            raise ValueError("Sliced result is jagged array.")

        print("My shape is :", new_family.shape)

        if new_family.ndim != 2:
            raise ValueError("Sliced result is not a 2D array.")

        res_famili = new_family[start:end]
        print("My new shape is :", res_famili.shape)

        return res_famili.tolist()

    except TypeError as e:
        print("TypeError:", e)
    except ValueError as e:
        print("ValueError:", e)

    return []


def main():
    """メイン関数"""
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
    print("----index -4, 3----")
    print(slice_me(family, -4, 3))
    print("----index -3, -1----")
    print(slice_me(family, -3, -1))
    print("----index 1, -2----")
    print(slice_me(family, 1, -2))
    print("----index 2, -2----")
    print(slice_me(family, 2, -2))
    print("----index 100, 110----")
    print(slice_me(family, 100, 110))
    print("----index -100, 110----")
    print(slice_me(family, -100, 110))
    print("----index 100, -110----")
    print(slice_me(family, 100, -110))

    jagged_family = [[1.80, 78.4], [2.15], [2.10, 98.5], [1.88, 75.2]]
    print("----jagged array test----")
    print(slice_me(jagged_family, 0, 2))


if __name__ == "__main__":
    main()
