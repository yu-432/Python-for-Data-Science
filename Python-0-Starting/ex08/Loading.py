from os import get_terminal_size


def ft_tqdm(lst: range) -> None:
    """進捗状況を表示しながらイテレートするジェネレーター"""
    length = len(lst)
    count = 0
    terminal_width = get_terminal_size().columns

    for item in lst:
        count += 1
        percent = int(count / length * 100)
        max_width = terminal_width - 40
        filled_length = int(max_width * percent // 100)
        bar = '██' * (filled_length // 2) + '  '\
            * ((max_width - filled_length) // 2)
        print(f"{percent:3d}%|{bar}| {count}/{length}\r", end="")
        yield item
    print("")
