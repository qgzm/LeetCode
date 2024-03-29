# 使用者：姜海波
# 创建时间：2023/4/5  11:04
class MyCalendarTwo:

    def __init__(self):
        # booked存放日程
        self.booked = []
        # overlaps存放已经重复的日程
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        if any(s < end and start < e for s, e in self.overlaps):
            return False
        for s, e in self.booked:
            if s < end and start < e:
                self.overlaps.append(((max(s, start), min(e, end))))
            self.booked.append((start, end))
            return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
