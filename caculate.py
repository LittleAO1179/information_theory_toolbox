import math


def calculate_information_entropy(probability: float):
    return math.log2(1/probability)

# 将字符转换为浮点数


def covert_float(str_probability: str):
    # 分式形式
    if str.find(str_probability, '/') > 0:
        res = float(int(str_probability.split(
            '/')[0])/int(str_probability.split('/')[1]))
        if res >= 0 and res <= 1:
            return res
        return None
    # 小数形式
    else:
        try:
            res = float(str_probability)
        except ValueError:
            return None
        if res >= 0 and res <= 1:
            return res
        return None
