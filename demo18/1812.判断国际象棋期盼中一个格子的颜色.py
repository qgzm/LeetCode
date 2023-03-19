# 使用者：姜海波
# 创建时间：2022/12/8  22:50
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # lis = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        # m = int(lis[coordinates[0]])
        # n = int(coordinates[1])
        # num = n * m
        # if (m % 2 == 1 and n % 2 == 1) or (m % 2 == 0 and n % 2 == 0):
        #     return False
        # else:
        #     return True
        return (ord(coordinates[0]) + ord(coordinates[1])) % 2 == 1


print(Solution().squareIsWhite('c7'))
