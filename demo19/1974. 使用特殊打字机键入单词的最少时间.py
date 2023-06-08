# 使用者：姜海波
# 创建时间：2023/6/6  17:21
class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = 0
        res = 0   # 当前位置
        for ch in word:
            # 计算键入每个字符的最小耗时并更新当前位置
            curr = ord(ch) - ord('a')
            res += 1 + min(abs(curr - prev), 26 - abs(curr - prev))
            prev = curr
        return res
