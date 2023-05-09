# 使用者：姜海波
# 创建时间：2023/5/9  19:34
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                 "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                 "...-", ".--", "-..-", "-.--", "--.."]
        se=set()
        for i in words:
            a=[]
            for j in i:
                a.append(MORSE[ord(j)-ord('a')])
            se.add(''.join(a))
        return len(se)


