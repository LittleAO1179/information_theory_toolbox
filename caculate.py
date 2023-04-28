import math


def calculate_information_entropy(probability: float):
    return math.log2(1/probability)


def covert_float(str_probability: str):
    # 分式形式
    if str.find(str_probability, '/') > 0:
        res = float(int(str_probability.split(
            '/')[0])/int(str_probability.split('/')[1]))
        return res
    elif float(str_probability) > 0:
        return float(str_probability)
    return None
