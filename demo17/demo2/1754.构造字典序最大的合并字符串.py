# 使用者：姜海波
# 创建时间：2022/12/24  1:10
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ''
        p1, p2 = 0, 0

        while p1 < len(word1) and p2 < len(word2):
            if word1[p1:] > word2[p2:]:
                merge += word1[p1]
                p1 += 1
            else:
                merge += word2[p2]
                p2 += 1

        merge += word1[p1:]
        merge += word2[p2:]

        return merge


print(Solution().largestMerge("cabaa", "bcaaa"))
