# 使用者：姜海波
# 创建时间：2023/3/26  17:01
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # 默认x>=y
        first, second = 'a', 'b'
        if y > x:
            x, y = y, x
            first, second = second, first
        ans = 0
        stack = []
        for i in s:
            # 存在pop使得stack又为空
            if not stack:
                stack.append(i)
            else:
                if i==second and stack[-1]==first:
                    stack.pop()
                    ans+=x
                else:
                    stack.append(i)
        stack1=[]
        for i in stack:
            if not stack1:
                stack1.append(i)
            else:
                if i==first and stack1[-1]==second:
                    stack1.pop()
                    ans+=y
                else:
                    stack1.append(i)

        return ans


print(Solution().maximumGain("cdbcbbaaabab", 4, 5))