# 使用者：姜海波
# 创建时间：2023/6/4  18:45
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour*30+30*minutes/60) % 360
        m = minutes*6
        x = abs(h-m)
        return min(x, 360-x)