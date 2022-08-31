# 使用者：姜海波
# 创建时间：2022/8/30  17:05
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #求长度
        n=len(nums)
        #排序方便后续
        nums.sort()
        #空list存放结果
        ans=list()
        #枚举
        for first in range(n):
            #排除first的重复,即可排除掉ans里可能出现的符合条件的结果
            if first>0 and nums[first]==nums[first-1]:
                continue
                #第三个数的指针从最后一名开始
            third = n-1
            target=-nums[first]
            #总体来说,second的循环是两数之和增大,所以在里面嵌套两数之和减少的语句
            for second in range(first+1,n):
                #防止second重复
                if second>first+1 and nums[second]==nums[second-1]:
                    continue
                #如果两数之和大于target,就缩小第三位
                while second <third and nums[second]+nums[third]>target:
                    third-=1
                #两数相等的情况下无结果
                if second==third:
                    break
                #条件符合的情况下存储结果
                if nums[second]+nums[third]==target:
                    ans.append([nums[first],nums[second],nums[third]])
        return ans
