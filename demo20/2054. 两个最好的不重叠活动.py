# 使用者：姜海波
# 创建时间：2023/4/5  19:58
from typing import List


class Event:
    def __init__(self, ts: int, op: int, val: int):
        self.ts = ts
        self.op = op
        self.val = val

    def __lt__(self, other: "Event"):
        return (self.ts, self.op) < (other.ts, other.op)


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        evs = list()
        for event in events:
            evs.append(Event(event[0], 0, event[2]))
            evs.append(Event(event[1], 1, event[2]))
        evs.sort()

        ans = bestFirst = 0
        for ev in evs:
            if ev.op == 0:
                ans = max(ans, ev.val + bestFirst)
            else:
                bestFirst = max(bestFirst, ev.val)

        return ans
