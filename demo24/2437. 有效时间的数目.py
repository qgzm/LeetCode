# 使用者：姜海波
# 创建时间：2023/5/9  12:44
class Solution:
    def countTime(self, time: str) -> int:
        countHour = 0
        countMinute = 0
        for i in range(24):
            hiHour = i // 10
            loHour = i % 10
            if ((time[0] == '?' or int(time[0]) == hiHour) and
                    (time[1] == '?' or int(time[1]) == loHour)):
                countHour += 1

        for i in range(60):
            hiMinute = i // 10
            loMinute = i % 10
            if ((time[3] == '?' or int(time[3]) == hiMinute) and
                    (time[4] == '?' or int(time[4]) == loMinute)):
                countMinute += 1

        return countHour * countMinute