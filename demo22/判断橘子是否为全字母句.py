# 使用者：姜海波
# 创建时间：2022/12/13  23:37
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
