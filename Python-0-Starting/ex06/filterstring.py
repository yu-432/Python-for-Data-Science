from ft_filter import ft_filter
from sys import argv


def filterstring(strings, size):
    """文字列stringsの中で、長さがsizeより大きい単語を抽出してリストで返す"""
    if type(strings) is not str or type(size) is not int:
        raise AssertionError("the arguments are bad")
    return ft_filter(lambda w: len(w) > size, strings.split(' '))


if __name__ == "__main__":
    if len(argv) != 3 or not argv[2].isdigit():
        raise AssertionError("the arguments are bad")

    print(filterstring(argv[1], int(argv[2])))
