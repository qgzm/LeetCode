# 使用者：姜海波
# 创建时间：2023/3/23  23:47
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = list()
        for left, right in zip(l, r):
            minv = min(nums[left:right + 1])
            maxv = max(nums[left:right + 1])
            # 找公差
            # 特殊情况,公差为零
            if minv == maxv:
                ans.append(True)
                continue
            #  公差为小数
            if (maxv - minv) % (right - left) != 0:
                ans.append(False)
                continue
            d = (maxv - minv) // (right - left)
            flag = True
            # 设置哈希表
            seen = set()
            for j in range(left, right + 1):
                # 与最小值之差不是公差的倍数
                if (nums[j] - minv) % d != 0:
                    flag = False
                    break
                t = (nums[j] - minv) // d
                # 如果有重复说明有两个数相同
                if t in seen:
                    flag = False
                    break
                seen.add(t)
            ans.append(flag)

        return ans
