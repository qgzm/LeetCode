# 使用者：姜海波
# 创建时间：2023/2/14  21:05
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        # 大于8小时计1分 小于等于8小时计-1分
        score = [0] * n
        for i in range(n):
            if hours[i] > 8:
                score[i] = 1
            else:
                score[i] = -1
# 前缀和
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + score[i - 1]
        ans=0
        stack=[]
        for i in range(n+1):
            if not stack or presum[stack[-1]]>presum[i]:
                stack.append(i)
        i=n
        while i>ans:
            while stack and presum[stack[-1]]<presum[i]:
                ans=max(ans,i-stack[-1])
                stack.pop()
            i-=1
        return ans






