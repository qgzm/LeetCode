# 使用者：姜海波
# 创建时间：2022/9/1  14:50
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        lis = []
        n = len(prices)
        for i in range(n):
            m = 0
            if i < n - 1:
                j = i + 1
            else:
                lis.append(prices[i])
                break
            while j < n:
                if prices[j] <= prices[i]:
                    lis.append(prices[i] - prices[j])
                    m = 1
                    break
                else:
                    j += 1
            if m == 0:
                lis.append(prices[i])
        return lis


if __name__ == "__main__":
    print(Solution().finalPrices([ 10, 1]))
