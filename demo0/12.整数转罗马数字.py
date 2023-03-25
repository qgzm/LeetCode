# 使用者：姜海波
# 创建时间：2023/3/25  10:58
class Solution:
    def intToRoman(self, num: int) -> str:
        arr=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        numb=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans=''
        for i in range(len(numb)):
            while num>=numb[i]:
                ans+=arr[i]
                num-=numb[i]

        return ans

