# 使用者：姜海波
# 创建时间：2023/4/6  21:09
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def transfer(x: int) -> int:
            return int("".join(str(mapping[int(digit)]) for digit in str(x)))

        num_pairs = [(transfer(num), num) for num in nums]
        num_pairs.sort(key=lambda pair: pair[0])

        ans = [num for (_, num) in num_pairs]
        return ans


print(Solution().sortJumbled([8,9,4,0,2,1,3,5,7,6],[991,338,38]))

