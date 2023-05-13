# 使用者：姜海波
# 创建时间：2023/5/12  22:33
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
        op = ''.join(ch.lower() for ch in s if ch.isalnum())
        return op == op[::-1]
