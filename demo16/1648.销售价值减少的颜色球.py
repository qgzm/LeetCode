# 使用者：姜海波
# 创建时间：2023/3/24  15:11
from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10 ** 9 + 7

        def range_sum(x, y):
            return (x + y) * (y - x + 1) // 2

        # inventory.sort()
        # maxIn=max(inventory)
        # sumIn=0
        # index=0
        # lis=[]
        # length=0
        # while sumIn<orders:
        #     lis.append(inventory[0])
        #     # remove() 函数用于移除列表中某个值的第一个匹配项。
        #     inventory.remove(maxIn)
        #     maxIn=max(inventory)
        #     length+=1
        # 检查ceil,如果num-ceil的和大于orders,说明选取的ceil过小
        def check(ceil):
            cnt = 0
            for num in inventory:
                if num > ceil:
                    cnt += num - ceil
            return cnt >= orders

        low = 0
        high = max(inventory)
        # 当找到中间值的时候停止循环
        while low < high - 1:
            mid = low + (high - low) // 2
            if check(mid):
                low = mid
            else:
                high = mid
        # high可能等于low也可能大于low的一
        # 确保rest的值为刚好超过
        rest = high if check(high) else low

        rest += 1

        # 使用等差数列求和公式按照剩余的最大数量进行卖球
        count = 0
        ans = 0
        for num in inventory:
            if num > rest:
                cur = num - rest
                count += cur
                ans += cur * (2 * rest + cur + 1) // 2
                ans %= MOD

        # 若还不够数量则加上这部分价值
        ans += (orders - count) * rest
        ans %= MOD
        return ans
