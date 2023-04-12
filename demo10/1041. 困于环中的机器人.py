# 使用者：姜海波
# 创建时间：2023/4/11  10:15
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direcIndex = 0
        x, y = 0, 0
        for instruction in instructions:
            if instruction == 'G':
                x += direc[direcIndex][0]
                y += direc[direcIndex][1]
            elif instruction == 'L':
                direcIndex -= 1
                direcIndex %= 4
            else:
                direcIndex += 1
                direcIndex %= 4

        return direcIndex != 0 or (x == 0 and y == 0)
