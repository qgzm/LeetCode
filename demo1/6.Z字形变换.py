# 使用者：姜海波
# 创建时间：2022/8/31  12:22
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # n=len(s)
        # p=""
        # for i in range(numRows):
        #     num=i
        #     j=numRows*2-2-2*i
        #     if j<0:
        #         j=numRows-(numRows-i)*2
        #     k=numRows*2-2-j
        #     while num<n:
        #         p+=s[j]
        #
        #     print(s)

        if numRows<2:return s
        res = ["" for _ in range(numRows)]
        i,flag=0,-1
        for c in s:
            res[i]+=c
            if i==0 or i==numRows-1:
                flag=-flag
            i+=flag
        return "".join(res)



if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 3))


