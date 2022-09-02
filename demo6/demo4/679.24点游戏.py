# 使用者：姜海波
# 创建时间：2022/9/2  17:26
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        target = 24
        epsilon = 1e-6
        add, multiply, subtract, divide = 0, 1, 2, 3

        def solve(nums: List[float]) -> bool:
            # 四个数都循环完毕,若再次循环,则表明无合适结果
            if not nums:
                return False
            # num等于一的时候,就是最终结果了,判断是否相等
            if len(nums) == 1:
                return abs(nums[0] - target) < epsilon
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        # 当只有两个数的时候新数组不添加新元素
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        # 只计算前两个数的关系
                        for k in range(4):
                            # 当是+和*的时候,交换位置结果不变,所以直接去掉
                            if k < 2 and i > j:
                                continue
                            if k == add:
                                newNums.append(x + y)
                            elif k == multiply:
                                newNums.append(x * y)
                            elif k == subtract:
                                newNums.append(x - y)
                            elif k == divide:
                                if abs(y) < epsilon:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False  # 遍历所有结果后的答案
        return solve(nums)
