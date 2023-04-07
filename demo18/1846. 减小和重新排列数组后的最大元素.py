# 使用者：姜海波
# 创建时间：2023/4/7  13:13
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        index = 0
        for i in arr:
            if i > index:
                index += 1
        return index
