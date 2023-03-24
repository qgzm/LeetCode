# 使用者：姜海波
# 创建时间：2023/3/25  0:26
from typing import List

# 满足三个条件
# arr[0]∼arr[i] 非递减
# arr[j]∼arr[n−1] 非递减
# arr[i]≤arr[j]
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        j = n - 1
        while j > 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if j == 0:
            return 0
        res = j
        for i in range(n):
            # 可能存在左边的非递减最大值小于右边,可以选择右边回退,比较效果一样,但是左边还未遍历完
            # 如果是左边回退比右边回退效果好,则由于range遍历过存了下来,所以不需考虑
            while j < n and arr[j] < arr[i]:
                j += 1
                # res代表后面的非递减,j-i-1代表中间删除的部分,而删中间的时候可以顺便把删前面给包括了,因为是从最左端开始的
            res = min(res, j - i - 1)
            if i + 1 < n and arr[i] > arr[i + 1]:
                break
        return res


Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5])
