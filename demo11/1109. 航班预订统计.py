# 使用者：姜海波
# 创建时间：2023/6/6  15:23
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        delta = [0] * 101
        offset = 1950
        for b, d in logs:
            delta[b - offset] += 1
            delta[d - offset] -= 1
        mx = 0
        res = 0
        curr = 0
        for i in range(101):
            curr += delta[i]
            if curr > mx:
                mx = curr
                res = i
        return res + offset