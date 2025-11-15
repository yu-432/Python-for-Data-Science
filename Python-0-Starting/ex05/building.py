from sys import argv, stdin


def count_characters(text):
    """カウント"""
    upper_count = sum(map(str.isupper, text))
    lower_count = sum(map(str.islower, text))
    number_count = sum(map(str.isdigit, text))
    space_count = sum(map(str.isspace, text))
    punctuation_count = len(text) - (upper_count + lower_count +
                                     space_count + number_count)

    return {
        'total': len(text),
        'upper': upper_count,
        'lower': lower_count,
        'digits': number_count,
        'spaces': space_count,
        'punctuation': punctuation_count
    }


def print_statistics(stats):
    """出力"""
    print(f"The text contains {stats['total']} characters:")
    print(stats['upper'], "upper letters")
    print(stats['lower'], "lower letters")
    print(stats['punctuation'], "punctuation marks")
    print(stats['spaces'], "spaces")
    print(stats['digits'], "digits")


def main(argv):
    """メイン・引数チェック"""
    if len(argv) == 1:
        print("What is the text to count?")
        string = stdin.readline()
    elif len(argv) == 2:
        string = argv[1]
    else:
        raise AssertionError("Error: Please provide exactly one argument.")

    print_statistics(count_characters(string))


if __name__ == "__main__":
    main(argv)
