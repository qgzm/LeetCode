# 使用者：姜海波
# 创建时间：2023/3/29  13:56
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # dic = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        # for i in range(n):
        return (n+1)*(n+2)*(n+3)*(n+4)/24