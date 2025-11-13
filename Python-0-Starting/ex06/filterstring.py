from ft_filter import ft_filter


def filterstring(strings, size):
    """文字列stringsの中で、長さがsizeより大きい単語を抽出してリストで返す"""
    if type(strings) is not str or type(size) is not int:
        print("AssertionError: the arguments are bad")
        return
    return ft_filter(lambda w: len(w) > size, strings.split(' '))
