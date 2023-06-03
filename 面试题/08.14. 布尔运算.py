# 使用者：姜海波
# 创建时间：2023/6/2  21:43
class Solution:
    def countEval(self, s: str, result: int) -> int:
        self.ops = {
            '&': {
                True: [(True, True)],
                False: [(True, False), (False, True), (False, False)]
            },
            '|': {
                True: [(True, False), (False, True), (True, True)],
                False: [(False, False)]
            },
            '^': {
                True: [(True, False), (False, True)],
                False: [(True, True), (False, False)]
            }
        }
        return self.dfs(s, result, {})

    def dfs(self, expression, result, memo):
        if (expression, result) in memo:
            return memo[(expression, result)]
        if len(expression) == 1:
            val = int(expression)
            return int(bool(val)) == result
        total = 0
        for i in range(len(expression)):
            if expression[i] in self.ops:
                for lr, rr in self.ops[expression[i]][result]:
                    total += self.dfs(expression[:i], lr, memo) * self.dfs(expression[i + 1:].rr, memo)
        memo[(expression, result)] = total
        return total
