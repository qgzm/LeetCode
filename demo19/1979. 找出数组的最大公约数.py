# 使用者：姜海波
# 创建时间：2023/4/6  21:04
import math
from typing import List


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(max(nums),min(nums))