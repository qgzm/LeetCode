# @Time : 2024/6/24 0:32
# @Author : 姜海波
# @Version：V 0.1
# @File : 2086. 喂食仓鼠的最小食物桶数.py
# @desc :
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters=hamsters.replace('H.H','1')
        hamsters=hamsters.replace('.H','1')
        hamsters=hamsters.replace('H.','1')
        res=0
        if 'H' in hamsters:
            return -1
        else:
            for i in hamsters:
                if i=='1':
                    res+=1
            return res


print(Solution().minimumBuckets("H..H"))
