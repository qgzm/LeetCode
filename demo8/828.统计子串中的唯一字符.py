# 使用者：姜海波
# 创建时间：2022/9/6  15:31
import collections


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # def find(str):
        #     a=set()
        #     for i in st:
        #         if i not in a:
        #             a.add(i)
        #     return len(a)
        #
        # n=len(s)
        # num=0
        # for i in range(n):
        #     for j in range(i,n):
        #         st=s[i:j+1:]
        #         num+=find(st)
        # return num

        index = collections.defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)
        res = 0
        for arr in index.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res
