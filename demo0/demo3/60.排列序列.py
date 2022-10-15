# 使用者：姜海波
# 创建时间：2022/10/15  12:45
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # number = 1
        # io=0
        # while n - 1 != 0:
        #     for i in range(1, n ):
        #         number *= i
        #     io = io*10+(k-1) // number + 1
        #     n = n - 1
        #     k=(k-1)%number+1
        #
        # return str(io)
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                # valid里面存的是0和1,用来对应1到n是否被用过,若用过改为0,那么order在减的时候就会使得后移
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)


print(Solution().getPermutation(4, 9))