# 使用者：姜海波
# 创建时间：2022/9/1  21:48

# 核心思想,将B拼成一个单词,最终判断一次即可
class Solution(object):
    # 统计每个单词中每个字母出现的频率
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        # 存放合并后每个单词出现频率的max
        bmax = [0] * 26
        for b in B:
            # 对返回的的数组拆分成元组,对应的值比较大小
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)
        # ans存放符合条件的单词
        ans = []
        # 对每个单词进行判断,存放
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans
