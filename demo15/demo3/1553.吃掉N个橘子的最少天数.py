# 使用者：姜海波
# 创建时间：2022/9/4  17:49
class Solution:
    # 缓存机制
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return min(n % 2 + 1 + self.minDays(n // 2), n % 3 + 1 + self.minDays(n // 3))
