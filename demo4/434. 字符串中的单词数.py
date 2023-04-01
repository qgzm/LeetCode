# 使用者：姜海波
# 创建时间：2023/4/1  17:25
class Solution:
    def countSegments(self, s: str) -> int:
        l=s.split(' ')
        print(l)
        ans=0
        for i in l:
            if i:
                ans+=1
        return ans


print(Solution().countSegments(""))