# 使用者：姜海波
# 创建时间：2023/3/17  8:50
class Solution:
    def reverseWords(self, s: str) -> str:
        # res=s.strip().split()
        #
        # res.reverse()
        # return str(" ".join(res))

        return " ".join(reversed(s.split()))


print(Solution().reverseWords("  a good   example "))