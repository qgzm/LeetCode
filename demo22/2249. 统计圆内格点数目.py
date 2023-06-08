# 使用者：姜海波
# 创建时间：2023/6/8  1:05
from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        ans = 0
        circles.sort(key=lambda c: -c[2])  # 按半径从大到小排序，这样能更早遇到包含 (i,j) 的圆
        max_x = max(c[0] + c[2] for c in circles)
        max_y = max(c[1] + c[2] for c in circles)
        for i in range(max_x + 1):
            for j in range(max_y + 1):
                for x, y, r in circles:
                    if (x - i) * (x - i) + (y - j) * (y - j) <= r * r:
                        ans += 1
                        break
        return ans


