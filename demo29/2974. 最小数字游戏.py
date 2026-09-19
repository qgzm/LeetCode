# @Time : 2024/7/12 23:40
# @Author : 姜海波
# @Version：V 0.1
# @File : 2974. 最小数字游戏.py
# @desc :
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
