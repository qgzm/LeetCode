# 使用者：姜海波
# 创建时间：2022/8/31  11:30
class Solution:
    def reverse(self, x: int) -> int:
        sel = 0
        if x < 0:
            x = -x
            sel = 1
        num = 0
        while x != 0:
            s = x % 10
            num = num * 10 + s
            x //= 10
        if sel == 1:
            num = -num
        return num

    def reverse_better(self, x: int) -> int:
        y, res = abs(x), 0
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res


"""
考虑溢出,而Python不需要考虑
public int reverse(int x) {
        long n = 0;
        while(x != 0) {
            n = n*10 + x%10;
            x = x/10;
        }
        return (int)n==n? (int)n:0;
    }"""

if __name__ == "__main__":
    print(Solution().reverse(-123))
    print(Solution().reverse_better(99999999999))
