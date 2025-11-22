from numpy import array


def validate_input(height: list[int | float], weight: list[int | float])\
     -> bool:
    """入力の検証"""
    if len(height) != len(weight) or len(height) == 0 or len(weight) == 0:
        return False
    if not all(isinstance(h, (int, float)) for h in height):
        return False
    if not all(isinstance(w, (int, float)) for w in weight):
        return False
    return True


def give_bmi(height: list[int | float], weight: list[int | float])\
     -> list[int | float]:
    """
    BMI計算
    BMI = 体重kg ÷ (身長m)^2
    """
    try:
        if validate_input(height, weight) is False:
            raise ValueError("height and weight must be same and non-empty.")

        result = []
        for i in range(len(height)):
            result.append(weight[i] / (height[i] ** 2))

        return array(result).tolist()
    except ValueError as e:
        print("ValueError:", e)
    except Exception as e:
        print("Error:", e)

    return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """BMI制限の適用"""
    try:
        if limit <= 0:
            raise ValueError("Limit must be a positive integer.")

        return [value > limit for value in bmi]

    except ValueError as e:
        print("ValueError:", e)
    except Exception as e:
        print("Error:", e)

    return []


def main():
    """メイン関数"""
    # 以下エラーテスト
    # どちらかがemptyリストの場合
    print("----どちらかがemptyリストの場合----")
    empty_heights = []
    weights = [50]
    bmi = give_bmi(empty_heights, weights)
    height = [1.75]
    empty_weights = []
    bmi = give_bmi(height, empty_weights)

    # 長さが異なるリストの場合
    print("----長さが異なるリストの場合----")
    heights = [1.75, 1.80]
    weights = [70]
    bmi = give_bmi(heights, weights)
    height = [1.75]
    weights = [70, 80]
    bmi = give_bmi(height, weights)

    # int,float以外の型が含まれる場合
    print("----int float以外の型が含まれる場合----")
    heights = [1.75, "1.80"]
    weights = [70, 80]
    bmi = give_bmi(heights, weights)
    height = [1.75]
    weights = [70, None]
    bmi = give_bmi(height, weights)

    # limitが0以下の場合
    print("----limitが0以下の場合----")
    height = [1.75, 1.80]
    weight = [70, 80]
    bmi = give_bmi(height, weight)
    print(apply_limit(bmi, 26))
    print(apply_limit(bmi, 0))
    print(apply_limit(bmi, -5))


if __name__ == "__main__":
    main()
