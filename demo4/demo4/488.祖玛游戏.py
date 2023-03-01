# 使用者：姜海波
# 创建时间：2023/3/1  12:45
from collections import deque
from itertools import product
from typing import re


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s):
            n = 1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s

        # 初始化队列
        hand = "".join(sorted(hand))
        queue = deque([(board, hand, 0)])
        visited = {(board, hand)}

        while queue:
            cur_board, cur_hand, step = queue.popleft()
            # 相当于双重for循环
            for i, j in product(range(len(cur_board) + 1), range(len(cur_hand))):
                # 当前的球和上一个球的颜色相同
                if j > 0 and cur_hand[j] == cur_hand[j - 1]:
                    continue
                # 只需要在连续相同颜色的球的开头位置插入新球
                if i > 0 and cur_board[i - 1] == cur_hand[j]:
                    continue
                # 只在以下两种情况放置新球
                choose = False
                # 当前球的颜色与后面的球的颜色相同
                if i < len(cur_board) and cur_board[i] == cur_hand[j]:
                    choose = True
                # 当前后颜色相同且与当前颜色不同时候放置球
                if 0 < i < len(cur_board) and cur_board[i - 1] == cur_board[i] and cur_board[i - 1] != cur_hand[j]:
                    choose = True

                if choose:
                    new_board = clean(cur_board[:i] + cur_hand[j] + cur_board[i:])
                    new_hand = cur_hand[:j] + cur_hand[j + 1:]
                    # 空则输出
                    if not new_board:
                        return step + 1

                    if (new_board, new_hand) not in visited:
                        queue.append((new_board, new_hand, step + 1))
                        visited.add((new_board, new_hand))
                        print(visited)
                        print(queue)
        return -1


Solution().findMinStep("WRRBBW", "RB")
