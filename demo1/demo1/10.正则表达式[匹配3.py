# # 使用者：姜海波
# # 创建时间：2022/8/31  23:06
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         i, j = 0, 0
#         j = len(s)
#         k = len(p)
#         d = -1
#         for c in s:
#             d += 1
#             if i < k and (c == p[i] or p[i] == '.'):
#                 i += 1
#             elif i < k and p[-1] == '*':
#                 return True
#             elif i < k - 1 and p[i] == '*' and p[i + 1] != s[d + 1]:
#                 continue
#             elif i < k - 1 and p[i] == '*' and p[i + 1] == s[d + 1]:
#                 i+=1
#             elif i < k - 1 and p[i] == '*' and (p[i + 1] == c or p[i + 1] == '.'):
#                 i += 1
#             elif i < k - 1 and p[i] != c and p[i + 1] == '*':
#                 i += 2
#             elif i == j:
#                 return True
#
#             else:
#                 return False
#         return True
#
#
# if __name__ == "__main__":
#     s = "mississippi"
#     p = "mis*is*ip*."
#     print(Solution().isMatch(s, p))
