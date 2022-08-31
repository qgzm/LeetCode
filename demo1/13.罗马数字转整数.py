# 使用者：姜海波
# 创建时间：2022/8/29  22:49
class Solution:
    def romanToInt(self, s: str) -> int:
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
        return ans


# 新思路,replace
'''
class Solution1 {
    public int romanToInt(String s) {
        s = s.replace("IV", "a");
        s = s.replace("IX", "b");
        s = s.replace("XL", "c");
        s = s.replace("XC", "d");
        s = s.replace("CD", "e");
        s = s.replace("CM", "f");

        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            res += getValue(s.charAt(i));
        }


        return res;
    }

    public int getValue(char c) {
        switch(c){
            case'I':return 1;
            case'V':return 5;
            case'X':return 10;
            case'L':return 50;
            case'C':return 100;
            case'D':return 500;
            case'M':return 1000;
            case'a':return 4;
            case'b':return 9;
            case'c':return 40;
            case'd':return 90;
            case'e':return 400;
            case'f':return 900;
        }
        return 0;
    }
}
'''