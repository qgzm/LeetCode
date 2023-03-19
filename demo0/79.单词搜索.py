# 使用者：姜海波
# 创建时间：2023/3/7  23:35
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 遍历该数组来保证每个相邻的地方都能被遍历
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 判断是否合适
        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            # 是否是最后一个
            if k == len(word) - 1:
                return True
            # visited数组保存已经遍历过并合适的位置
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            # 如果接下来的并不合适,说明该位置需要暂时被抛弃
            visited.remove((i, j))
            return result


        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False

