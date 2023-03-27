# 使用者：姜海波
# 创建时间：2023/3/27  1:17
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        size=int(n**0.5)
        sums=[0]*((n+size-1)//size)
        for i,num in enumerate(nums):
            sums[i//size]+=num
        self.nums=nums
        self.sums=sums
        self.size=size


    def update(self, index: int, val: int) -> None:
        self.sums[index//self.size]+=val-self.nums[index]
        self.nums[index]=val


    def sumRange(self, left: int, right: int) -> int:
        m=self.size
        b1,b2=left//m,right//m
        if b1==b2:
            return sum(self.nums[left:right+1])
        return sum(self.nums[left:(b1+1)*m])+sum(self.sums[b1+1:b2])+sum(self.nums[b2 * m:right + 1])