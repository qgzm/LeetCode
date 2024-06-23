# @Time : 2024/6/23 23:54
# @Author : 姜海波
# @Version：V 0.1
# @File : 1295. 统计位数为偶数的数字.py
# @desc :

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            arr = str(i)
            l = len(arr)
            if l % 2 == 0:
                res += 1
        return res
