# 使用者：姜海波
# 创建时间：2023/1/17  1:52
class Solution:
    def validPalindrome(self, s: str) -> bool:
        opportunity, i, j = 1, 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if opportunity:
                    opportunity -= 1
                    res1 = s[:i]+s[i+1:]
                    if res1 == res1[::-1]:
                        return True
                    if j<len(s)-1:
                        res2 = s[:j]+s[j+1:]
                    else:
                        res2=s[:-1]
                    if res2 == res2[::-1]:
                        return True
                    return False
                return False
        return True


print(Solution().validPalindrome("cdbeeeabddddbaeedebdc"))
