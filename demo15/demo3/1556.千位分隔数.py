# 使用者：姜海波
# 创建时间：2022/9/4  17:15
class Solution:
    def thousandSeparator(self, n: int) -> str:
        # return format(n,',').replace(',','.')
        n=str(n)[::-1]
        new=''
        for i,num in enumerate(n):
            new+=num
            if (i+1)%3==0 and (i+1)!=len(n):
                new+='.'
        return new[::-1]

print(Solution().thousandSeparator(1341531))