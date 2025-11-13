from ft_package import count_in_list

def main():
    """テスト用の関数"""
    ft_list = ["apple", "banana", "orange", "apple", "kiwi", "banana", "apple"]
    item_to_count = "apple"
    count = count_in_list(ft_list, item_to_count)
    print(f"'{item_to_count}': {count}")

if __name__ == "__main__":
    main()
