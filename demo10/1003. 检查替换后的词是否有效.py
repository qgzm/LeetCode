# 使用者：姜海波
# 创建时间：2023/5/3  12:20
class Solution:
    def isValid(self, s: str) -> bool:
        # 简单难度
        # while 'abc' in s:
        #     s=s.replace('abc','')
        # return s==''

        # 栈模式
        lis = []
        for char in s:
            lis.append(char)
            if ''.join(lis[-3:]) == 'abc':
                lis[-3:] = []
        return len(lis) == 0