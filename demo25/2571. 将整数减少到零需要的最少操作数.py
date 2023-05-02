# 使用者：姜海波
# 创建时间：2023/4/24  0:16
class Solution:
    def minOperations(self, n: int) -> int:
        # pass

        return (3 * n ^ n).bit_count()

