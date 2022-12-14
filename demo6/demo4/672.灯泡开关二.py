# 使用者：姜海波
# 创建时间：2022/9/15  13:41
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        seen = set()
        for i in range(2 ** 4):
            pressArr = [(i >> j) & 1 for j in range(4)]
            # pressArr表示四个按钮的按动情况
            # 整数status表示四组灯泡亮灭的状态
            if sum(pressArr) % 2 == presses % 2 and sum(pressArr) <= presses:
                status = pressArr[0] ^ pressArr[1] ^ pressArr[3]
                if n >= 2:
                    status |= (pressArr[0] ^ pressArr[1]) << 1
                if n >= 3:
                    status |= (pressArr[0] ^ pressArr[2]) << 2
                if n >= 4:
                    status |= (pressArr[0] ^ pressArr[1] ^ pressArr[3]) << 3
                seen.add(status)
        return len(seen)


Solution().flipLights(4, 3)
