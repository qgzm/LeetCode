# 使用者：姜海波
# 创建时间：2023/4/13  23:01
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic=collections.Counter(nums)
        ma=-1
        ans=-1
        for index,key in dic.items():
            if index%2==0:
                if key>ma:
                    ans=index
                    ma=key
                elif key==ma:
                    if index<ans:
                        ans=index
        return ans