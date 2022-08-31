# 使用者：姜海波
# 创建时间：2022/8/30  13:41
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n = len(s)
        # num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # for i in range(n):
        #     j = i + 1
        #     num[i] = 1
        #     for j in range(j, n):
        #         if j < n and s[j] != s[i]:
        #             num[i] += 1
        #         else:
        #             break
        # return max(num)

        #和自己写的代码比,最突出不一样的是运用哈希表来排除字符串中重复值,上述代码也可以运用哈希表进行修改
        #哈希集合,记录每个字符是否出现过
        occ=set()
        n=len(s)
        #右指针,初始值为-1,相当于我们在字符串的左边界的左侧,还没开始移动
        rk,ans=-1,0
        for i in range(n):
            #i是左指针
            if i !=0:
                occ.remove(s[i-1])
            while rk+1<n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk+=1
            ans=max(ans,rk-i+1)
        return ans


if __name__ == "__main__":
    stri = "asdhiusaheo"
    print(Solution().lengthOfLongestSubstring(stri))
