# 使用者：姜海波
# 创建时间：2022/8/31  22:12
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]  # 初始化
        dp[0][0] = True  # 空串匹配

        for j in range(1, n + 1):  # 初始化 p与空串的匹配，s不会以'*'打头，所以省略了一些，下同。
            dp[0][j] = dp[0][j - 2] if p[j - 1] == '*' else False  # 开头加了一位，则p中当前字符下标都要-1，s同。

        for i in range(1, m + 1):  # 开始填表
            for j in range(1, n + 1):
                if p[j - 1] in {s[i - 1], '.'}:  # p当前字符能匹配且不为*
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':  # p当前字符为 *
                    if dp[i][j - 2]:  # ‘*’匹配 0 次，看倒着数2位的位置
                        dp[i][j] = True
                    elif p[j - 2] in {s[i - 1], '.'}:  # ‘*’匹配一次或多次，看倒着数一位的位置
                        dp[i][j] = dp[i - 1][j]
        return dp[m][n]

if __name__ == "__main__":
    s = "aaa"
    p = "a.."
    print(Solution().isMatch(s, p))