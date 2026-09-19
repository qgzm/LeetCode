# @Time : 2024/6/27 0:55
# @Author : 姜海波
# @Version：V 0.1
# @File : 2734. 执行子串操作后的字典序最小字符串.py
# @desc :
class Solution:
    def smallestString(self, s: str) -> str:
        t = list(s)
        for i, c in enumerate(t):
            if c == 'a':
                continue
            # 继续向后遍历
            for j in range(i, len(t)):
                if t[j] == 'a':
                    break
                t[j] = chr(ord(t[j]) - 1)
            return ''.join(t)
        # 所有字母均为 a
        t[-1] = 'z'
        return ''.join(t)

