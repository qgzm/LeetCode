# 使用者：姜海波
# 创建时间：2023/4/3  23:49
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        lis = str(num)
        m = len(lis)
        res = 0
        for i in range(m - k + 1):
            inte = int(lis[i:i+k])
            if inte != 0 and num % inte == 0:
                res += 1
            else:
                continue
        return res


print(Solution().divisorSubstrings(num=430043, k=2))
