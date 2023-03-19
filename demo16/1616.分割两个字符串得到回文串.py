# 使用者：姜海波
# 创建时间：2023/3/18  21:41
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.checkConcatenation(a,b) or self.checkConcatenation(b,a)

    def checkConcatenation(self,a:str,b:str)->bool:
        n=len(a)
        left,right=0,n-1
        while left<right and a[left]==b[right]:
            left+=1
            right-=1
        if left>=right:
            return True
        return self.checkSelfPalindrome(a,left,right) or self.checkSelfPalindrome(b,left,right)

    def checkSelfPalindrome(self,a:str,left:int,right:int)->bool:
        while left<right and a[left]==a[right]:
            left+=1
            right-=1
        return left>=right