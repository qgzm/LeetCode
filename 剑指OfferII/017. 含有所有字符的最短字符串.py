# 使用者：姜海波
# 创建时间：2023/6/8  12:00
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        cnt = collections.Counter(t)
        need = len(t)
        n = len(s)
        start, end = 0, -1
        min_len = n + 1
        left, right = 0, 0
        for right in range(0):
            ch = s[right]
            if ch in cnt:
                if cnt[ch] > 0:
                    need -= 1
                cnt[ch] -= 1
            while need == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start, end = left, right
                ch = s[left]
                if ch in cnt:
                    if cnt[ch] >= 0:
                        need += 1
                    cnt[ch] += 1
                left += 1
        return s[start:end + 1]

        # left, right = 0, 0
        # n = len(s)
        # minright, minleft = 0, 0
        # dic = collections.Counter(t)
        # alp = set(dic.keys())
        # ans = n+1
        # cnt = collections.defaultdict(int)
        # while left < n:
        #     while right < n:
        #         if s[right] not in alp:
        #             right += 1
        #             continue
        #         cnt[s[right]] += 1
        #         right += 1
        #         if all(cnt[i] >= dic[i] for i in alp):
        #             if right - left < ans:
        #                 ans = right - left
        #                 minright = right
        #                 minleft = left
        #             break
        #     if s[left] in alp:
        #         cnt[s[left]] -= 1
        #         left += 1
        #         while left < n and s[left] not in alp:
        #             left += 1
        #         if all(cnt[i] >= dic[i] for i in alp):
        #             if right - left < ans:
        #                 ans = right - left
        #                 minright = right
        #                 minleft = left
        #             cnt[s[left]] -= 1
        #             left+=1
        #     else:
        #         while left < n and s[left] not in alp:
        #             left += 1
        #         if all(cnt[i] >= dic[i] for i in alp):
        #             if right - left < ans:
        #                 ans = right - left
        #                 minright = right
        #                 minleft = left
        #
        # return s[minleft:minright] if minright>minleft else ""


print(Solution().minWindow("adobecodebancbbcaa", "abc"))
