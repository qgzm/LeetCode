# @Time : 2024/8/5 19:22
# @Author : 姜海波
# @Version：V 0.1
# @File : winlose.py
# @desc :
from typing import List

# 给你一个整数数组games其中games[i] = [winner, loser]
# 表示在一场游戏中winner击败了loser 。返回一个长度为2的列表answer ：
# answer[0] 是所有没有输掉任何游戏的玩家列表。answer[1]是所有恰好输掉一场游戏的玩家列表。两个列表中的值都应该按递增顺序返回。
#
# 注意：
# 只考虑那些参与至少一场游戏的玩家。
# 生成的测试用例保证不存在两场游戏结果相同。
#
# 示例1：
# 输入：games = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
# 输出：[[1, 2, 10], [4, 5, 7, 8]]
# 解释：玩家1、2和10都没有输掉任何游戏。玩家4、5、7和8每个都输掉一场游戏。
# 玩家3、6和9每个都输掉两场游戏。
# 因此，answer[0] = [1, 2, 10]和answer[1] = [4, 5, 7, 8] 。
#
# 示例
# 2：
# 输入：games = [[2, 3], [1, 3], [5, 4], [6, 4]]
# 输出：[[1, 2, 5, 6], []]
# 解释：玩家1、2、5和6都没有输掉任何游戏。
# 玩家3和4每个都输掉两场游戏。因此，answer[0] = [1, 2, 5, 6]和answer[1] = [] 。
#
#
# 提示：
# 1 <= games.length <= 10 ^ 5
# games[i].length == 2
# 1 <= winneri, loseri <= 10 ^ 5
# winner != loser
# 所有
# games[i]
# 互不相同
#
# ————————————————
# 请在下方作答：
#
# python
def testFunc(games):
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
            zd[games[i][0]] = zd[games[i][0]] + 1
    for key in zd:
        if zd[key] == 0:
            ans[0].append(key)
        if zd[key] == 1:
            ans[1].append(key)

    return ans


#
# ————————————————
# 测试用例1：
# 输入[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
# 输出[[1, 2, 10], [4, 5, 7, 8]]
#
# 测试用例2：
# 输入[[2, 3], [1, 3], [5, 4], [6, 4]]
# 输出[[1, 2, 5, 6], []]

print(testFunc([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
print(abs(45))