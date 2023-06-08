# 使用者：姜海波
# 创建时间：2023/6/6  14:42
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans=0
        cnt=0
        for i in s:
            if i == '0':
                cnt+=1
            elif cnt!=0:
                ans=max(ans+1,cnt)
        return ans
