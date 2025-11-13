from sys import argv


def create_morse(string):
    """モールス信号の作成"""
    dict = {
        'A': '.-',    'B': '-...',  'C': '-.-.',
        'D': '-..',   'E': '.',     'F': '..-.',
        'G': '--.',   'H': '....',  'I': '..',
        'J': '.---',  'K': '-.-',   'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',
        'S': '...',   'T': '-',     'U': '..-',
        'V': '...-',  'W': '.--',   'X': '-..-',
        'Y': '-.--',  'Z': '--..',
    }
    return ' '.join(dict[char] for char in string.upper())


def validate(string):
    """入力値検証"""
    if not string or not string.isalpha():
        print("AssertionError: the arguments are bad")
        return False
    return True


def main(argv):
    """メイン・引数チェック"""
    if len(argv) != 2 or not validate(argv[1]):
        print("AssertionError: the arguments are bad")
        return

    print(create_morse(argv[1]))


if __name__ == "__main__":
    main(argv)
