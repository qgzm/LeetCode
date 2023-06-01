# 使用者：姜海波
# 创建时间：2023/4/29  20:13

import matplotlib.pyplot as plt
from typing import List


# location: [[a,b,c,d],[e,f,g]...]一共81个元素,共n个类,相同类的元素在同一个列表中,如a,b,c,d是一个类,e,f,g是另一个类
# indexphoto: 图片生产后的命名,"{{indexphoto}}.png"
def solution(location: List[List[int]], indexphoto: int) -> None:
    matrix = [[0] * 9 for _ in range(9)]
    # n = len(location)
    number = 0
    # 存放各元素坐标
    # alllocation = []
    # 存放聚类中心位置
    centerlocation = list()

    # 输入聚类中心,返回最近的想要的位置
    # 欧氏距离
    def bianli(center: list[int], number: int) -> list:
        x = center[0]
        y = center[1]
        min_distance = 81
        ans = [0, 0]
        for i in range(9):
            for j in range(9):
                if matrix[i][j] == 0:
                    if ((i - x) ** 2 + (j - y) ** 2) < min_distance:
                        min_distance = ((i - x) ** 2 + (j - y) ** 2)
                        ans = [i, j]
        matrix[ans[0]][ans[1]] = number
        return ans

    # 重新计算聚类中心
    def recount(sublocation: list[list[int]]) -> list:
        sumx, sumy = 0, 0
        for i in sublocation:
            sumx += i[0]
            sumy += i[1]
        newcenter = [sumx / len(sublocation), sumy / len(sublocation)]
        return newcenter

    # 寻找初始聚类中心
    def fundcenter() -> list[int]:
        for x in range(9):
            for y in range(9):
                if matrix[x][y] == 0:
                    center = [x, y]
                    sublocation.append(center)
                    matrix[x][y] = number
                    return center

    for i in location:
        number += 1
        center = [-1, -1]
        sublocation = list()
        for index, j in enumerate(i):
            # 在矩阵中随意找出一个未被占用的位置作为初始聚类中心
            if center == [-1, -1]:
                center = fundcenter()
                continue
            # 有了初始聚类中心后开始向其靠拢
            sublocation.append(bianli(center, number))
            center = recount(sublocation)
            if index == len(i) - 1:
                centerlocation.append(center)
                # alllocation.append(sublocation)

    # 查看矩阵
    # print("before")
    # for i in matrix:
    #     print(i)

    def find_more_near(x: int, y: int) -> int:
        for i in range(9):
            for j in range(9):
                comparecenter = centerlocation[matrix[i][j] - 1]
                if (i - comparecenter[0]) ** 2 + (j - comparecenter[1]) ** 2 + (
                        x - centerlocation[matrix[x][y] - 1][0]) ** 2 + (
                        y - centerlocation[matrix[x][y] - 1][1]) ** 2 > (x - comparecenter[0]) ** 2 + (
                        y - comparecenter[1]) ** 2 + (
                        i - centerlocation[matrix[x][y] - 1][0]) ** 2 + (
                        j - centerlocation[matrix[x][y] - 1][1]) ** 2:
                    matrix[i][j], matrix[x][y] = matrix[x][y], matrix[i][j]
                    return 1
        return 0

    def renewcenter():
        for index, k in enumerate(centerlocation):
            sumx = 0
            sumy = 0
            su = 0
            for i in range(9):
                for j in range(9):
                    if matrix[i][j] == index + 1:
                        su += 1
                        sumx += i
                        sumy += j
            centerlocation[index] = [sumx / su, sumy / su]

    # 半成品,仍需优化,如果出现更小的欧氏距离之和,就进行交换
    # mark: 交换的次数,可以修改
    # circulation: 防止出现死循环,强制circulation次后退出
    mark = 1000
    circulation = 10000
    while True:
        circulation -= 1
        for i in range(9):
            for j in range(9):
                mark -= find_more_near(i, j)
                # 更新聚类中心
                renewcenter()
        if mark < 0 or circulation < 0:
            break

    # print('after')
    # for i in matrix:
    #     print(i)

    plt.matshow(matrix, cmap=plt.get_cmap('binary'))  # , alpha=0.3
    plt.xticks([])  # 去掉x轴
    plt.yticks([])  # 去掉y轴
    plt.axis('off')  # 去掉坐标轴

    plt.savefig('./' + str(indexphoto) + '.png', bbox_inches='tight', dpi=30, pad_inches=0.0)

    # 看图片
    # plt.show()


if __name__ == '__main__':
    solution(
        [[1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1]], 2)


