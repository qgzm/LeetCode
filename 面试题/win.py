# @Time : 2024/8/6 15:48
# @Author : 姜海波
# @Version：V 0.1
# @File : win.py
# @desc :
from typing import List
def Func(games):
    ans = [[], []]
    # 请在此补充代码
    zd = {}
    n = len(games)
    for i in range(n):
        if games[i][0] not in zd:
            zd[games[i][0]] = 0
        # lose
        if games[i][1] not in zd:
            zd[games[i][1]] = 1
        else:
            zd[games[i][1]] += 1
    for key in zd:
        if zd[key] == 0:
            ans[0].append(key)
        if zd[key] == 1:
            ans[1].append(key)

    return ans
print(Func([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
