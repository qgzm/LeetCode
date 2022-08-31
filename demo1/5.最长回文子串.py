# 使用者：姜海波
# 创建时间：2022/8/31  12:57
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    # n=len(s)
    # lis=[]
    # for i in range(n):
    #     j=0
    #     while i+j<n and i-j>=0 and s[i+j]==s[i-j]:
    #         j+=1
    #     lis.append(j)
    # na,ma=max(enumerate(lis))
    # return s[na-ma:na+ma]

    # 中心扩散法
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]
