# 使用者：姜海波
# 创建时间：2023/3/9  23:24
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = inf
        cnt = 0
        for i, ch in enumerate(blocks):
            if ch == 'W':
                cnt += 1
            if i >= k and blocks[i-k] == 'W':
                cnt -= 1
            if i >= k - 1:
                ans = min(ans, cnt)
        return ans
