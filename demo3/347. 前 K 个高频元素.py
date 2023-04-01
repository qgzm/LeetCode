# 使用者：姜海波
# 创建时间：2023/4/1  18:03
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1

        res = []
        while k > 0:
            tmp = 0
            for num in dic:
                if dic[num] > tmp:
                    tmp = dic[num]
                    cur = num

            dic[cur] = -1
            res.append(cur)
            k -= 1
        return res
