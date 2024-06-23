# @Time : 2024/6/23 23:37
# @Author : 姜海波
# @Version：V 0.1
# @File : 482. 密钥格式化.py
# @desc :
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        arr = []
        cnt = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != '-':
                arr.append(s[i].upper())
                cnt += 1
                if cnt % k == 0:
                    arr.append('-')
        if arr and arr[-1] == '-':
            arr.pop()
        return ''.join(arr[::-1])
