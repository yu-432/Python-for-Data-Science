from ft_filter import ft_filter
from filterstring import filterstring


def test_with_lambda():
    """lambda関数を使ったテスト"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def func(x):
        return x % 2 == 0

    result_ft = ft_filter(func, numbers)
    result_builtin = list(filter(func, numbers))

    print(f"ft_filter result:  {result_ft}")
    print(f"filter result:     {result_builtin}")
    print(f"Match: {result_ft == result_builtin}")
    assert result_ft == result_builtin
    print("✓ test_with_lambda passed\n")


def test_with_none():
    """function=None の場合のテスト"""
    values = [0, 1, False, True, "", "hello", None, [], [1, 2]]

    result_ft = ft_filter(None, values)
    result_builtin = list(filter(None, values))

    print(f"ft_filter result:  {result_ft}")
    print(f"filter result:     {result_builtin}")
    print(f"Match: {result_ft == result_builtin}")
    assert result_ft == result_builtin
    print("✓ test_with_none passed\n")


def test_with_true():
    """True,Falseを使ったテスト"""
    numbers = [True, False, 1, 0, -1, 2, -2]

    result_ft = ft_filter(None, numbers)
    result_builtin = list(filter(None, numbers))

    print(f"ft_filter result:  {result_ft}")
    print(f"filter result:     {result_builtin}")
    print(f"Match: {result_ft == result_builtin}")
    assert result_ft == result_builtin
    print("✓ test_with_lambda passed\n")


def test_with_doc_string():
    """DocStringのテスト"""
    result_ft = print(ft_filter.__doc__)
    result_builtin = print(filter.__doc__)

    print(f"filterstring result:  {result_ft}")
    print(f"filter result:        {result_builtin}")
    print(f"Match: {result_ft == result_builtin}")
    assert result_ft == result_builtin
    print("✓ test_with_doc_string passed\n")


def test_with_strings():
    """文字列のフィルタリングのテスト"""
    words = ["Hello", "my", "name", "is", "Alice"]
    string = "Hello my name is Alice"

    def func(w):
        return len(w) > 3

    result_ft = filterstring(string, 3)
    result_builtin = list(filter(func, words))

    print(f"filterstring result:  {result_ft}")
    print(f"filter result:        {result_builtin}")
    print(f"Match: {result_ft == result_builtin}")
    assert result_ft == result_builtin
    print("✓ test_with_strings passed\n")


def test_empty_iterable():
    """空のイテラブルのテスト"""
    def func(x):
        return x > 0

    result_ft = filterstring("", 0)
    result_builtin = list(filter(func, []))

    print(f"filterstring result:  {result_ft}")
    print(f"filter result:        {result_builtin}")
    print(f"Match: {result_ft == result_builtin}")
    assert result_ft == result_builtin
    print("✓ test_empty_iterable passed\n")


def main():
    """全テストを実行"""
    print("=" * 60)
    print("ft_filter vs builtin filter comparison tests")
    print("=" * 60 + "\n")

    test_with_lambda()
    test_with_none()
    test_with_true()
    test_with_doc_string()
    print("=" * 60)
    print("filterstring vs builtin filter comparison tests")
    print("=" * 60 + "\n")
    test_with_strings()
    test_empty_iterable()


if __name__ == "__main__":
    main()
