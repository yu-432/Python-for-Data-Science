from sys import argv


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
    if len(argv) != 2:
        print("Error: Please provide exactly one argument.")
        return

    print_statistics(count_characters(argv[1]))


if __name__ == "__main__":
    main(argv)
