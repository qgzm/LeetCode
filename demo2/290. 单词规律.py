# 使用者：姜海波
# 创建时间：2023/5/23  16:01
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordtochar = dict()
        chartoword = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for char, word in zip(pattern, words):
            if (word in wordtochar and wordtochar[word] != char) or (char in chartoword and chartoword[char] != word):
                return False
            wordtochar[word] = char
            chartoword[char] = word
        return True
