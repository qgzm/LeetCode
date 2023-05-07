# 使用者：姜海波
# 创建时间：2023/5/5  17:15
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        arr = list([[0,0]])
        start = [0, 0]
        for i in path:
            if i == 'N':
                start[1] += 1
            elif i == 'S':
                start[1] -= 1
            elif i == 'E':
                start[0] += 1
            elif i == 'W':
                start[0] -= 1
            if start in arr:
                return True
            else:
                arr.append(start.copy())
        return False


print(Solution().isPathCrossing("NESWW"))