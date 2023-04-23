# 使用者：姜海波
# 创建时间：2023/4/19  22:19
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        d = [0] * (n + 1)
        for i in range(1, n + 1):
            maxValue = arr[i - 1]
            for j in range(i - 1, max(-1, i - k - 1), -1):
                d[i] = max(d[i], d[j] + maxValue * (i - j))
                if j > 0:
                    maxValue = max(maxValue, arr[j - 1])
        return d[n]
