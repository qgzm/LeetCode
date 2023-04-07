# 使用者：姜海波
# 创建时间：2023/4/7  15:05
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        elapsedTime = [0] * n
        elapsedTime[headID] = 0
        time_max = 0

        def addTime(id):
            if elapsedTime[id] == 0 and manager[id] >= 0:
                elapsedTime[id] = informTime[manager[id]] + addTime(manager[id])
            return elapsedTime[id]

        for i in range(n):
            if informTime[i] == 0:
                time_max = max(time_max, addTime(i))
        return time_max
