# 使用者：姜海波
# 创建时间：2023/3/31  12:24
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        # 会产生2n-1个回文中心
        for i in range(2 * n - 1):
            left = i // 2
            right = i // 2 + i % 2
            while left >= 0 and right < n and s[right] == s[left]:
                right += 1
                left -= 1
                ans += 1
        return ans
