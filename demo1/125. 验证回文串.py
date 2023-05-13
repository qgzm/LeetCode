# 使用者：姜海波
# 创建时间：2023/5/12  22:28
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        op=''
        while i<=j:
            if s[i].isdigit() or s[i].isalpha():
                op=op+s[i]
            i+=1
        op=op.lower()
        return op==op[::-1]
