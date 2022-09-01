# 使用者：姜海波
# 创建时间：2022/9/1  16:21

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res


# def divide( dividend: int, divisor: int) -> int:
#     sign = (dividend > 0) ^ (divisor > 0)
#     dividend = abs(dividend)
#     divisor = abs(divisor)
#     count = 0
#     while dividend >= divisor:
#         count += 1
#         divisor <<= 1
#     result = 0
#     while count > 0:
#         count -= 1
#         divisor >>= 1
#         if divisor <= dividend:
#             result += 1 << count
#             dividend -= divisor
#     if sign: result = -result
#     return result if -(1 << 31) <= result <= (1 << 31) - 1 else (1 << 31) - 1


# print(divide(1000, 7))
Solution().divide(12222,7)