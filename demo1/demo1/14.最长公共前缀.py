# 使用者：姜海波
# 创建时间：2022/9/3  15:21
# st=['aretg']
# print(st[0][2])
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p=[]
        j=len(strs[0])
        for k in range(j):

            for i in strs:
                if k<len(i):
                    if i[k]==strs[0][k]:
                        continue
                    else:
                        return ''.join(p)
                else:
                    return ''.join(p)
            p.append(strs[0][k])
        return ''.join(p)