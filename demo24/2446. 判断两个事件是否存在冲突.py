# 使用者：姜海波
# 创建时间：2023/5/17  23:30
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return not (event1[1]<event2[0] or event1[0]>event2[1])