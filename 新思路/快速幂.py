# 使用者：姜海波
# 创建时间：2022/10/17  20:12
def fastPower(base, power) -> int:
    result = 0
    while power > 0:
        if power & 1:
            result = result * base % 1000
        power >>= 1
        base = (base * base) % 1000
    return result
