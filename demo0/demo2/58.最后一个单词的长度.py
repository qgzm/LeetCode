# 使用者：姜海波
# 创建时间：2022/9/5  15:21
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lis = s.split(' ')
        i = -1
        while lis[i] == "":
            i -= 1

        return len(lis[i])


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
