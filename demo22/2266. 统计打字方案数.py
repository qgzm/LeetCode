# 使用者：姜海波
# 创建时间：2023/6/5  20:06
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 10 ** 9 + 7
        dp3 = [1, 1, 2, 4]
        dp4 = [1, 1, 2, 4]
        n = len(pressedKeys)
        for i in range(4, n + 1):
            dp3.append((dp3[i - 1] + dp3[i - 2] + dp3[i - 3]) % m)
            dp4.append((dp4[i - 1] + dp4[i - 2] + dp4[i - 3] + dp4[i - 4]) % m)

        res = 1
        cnt = 1
        for i in range(1, n):
            if pressedKeys[i] == pressedKeys[i - 1]:
                cnt += 1
            else:
                if pressedKeys[i - 1] in "79":
                    res *= dp4[cnt]
                else:
                    res *= dp3[cnt]
                    res %= mod
                    cnt = 1
        if pressedKeys[-1] in "79":
            res *= dp4[cnt]
        else:
            res *= dp3[cnt]
        return res%mod
