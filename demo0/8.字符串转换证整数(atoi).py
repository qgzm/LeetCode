# 使用者：姜海波
# 创建时间：2022/12/24  2:10
import re


class Solution:
    def myAtoi(self, s: str) -> int:
        # INT_MAX = 2 ** 31 - 1
        # INT_MIN = -2 ** 31
        # str = str.lstrip()
        # num_re = re.compile(r'^[\+\-]?\d+')
        # num = num_re.findall(str)
        # num = int(*num)
        # return max(min(num, INT_MAX), INT_MIN)
        s = s.lstrip()
        if not s:
            return 0
        s_list = list(s)
        res = ""
        if s_list[0] == "-":
            # 如果第一个是负号 那结果是负的
            res = "-"
        if (s_list[0] == "+") or (s_list[0] == "-"):
            # 如果第一个是正号 那结果是负的
            s_list.pop(0)
        for tmp in s_list:
            # isnumeric() 方法检测字符串是否只由数字组成
            if tmp.isnumeric():
                res += tmp
            else:
                break
        if (res == "") or (res == "-"):
            return 0
        if int(res) > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if int(res) < -2 ** 31:
            return -2 ** 31
        return int(res)


print(Solution().myAtoi("0042-2dl"))


