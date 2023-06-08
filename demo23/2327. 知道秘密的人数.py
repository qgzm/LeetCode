# 使用者：姜海波
# 创建时间：2023/6/6  20:08
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        if delay > forget:
            return 0
        dp=[0]*n
        dp[0]=1
        cnt=0
        for i,v in enumerate(dp):
            if i+delay>=n:
                cnt+=v
            for j in range(i+delay,min(i+forget,n)):
                dp[j]=(dp[j]+v)%1000000007
        return (dp[-1]+cnt)%1000000007

print(Solution().peopleAwareOfSecret(n=6, delay=2, forget=4))
