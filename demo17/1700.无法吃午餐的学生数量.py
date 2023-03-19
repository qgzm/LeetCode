# 使用者：姜海波
# 创建时间：2022/10/19  13:36
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        flag=1
        indsan=0
        while flag==1:
            flag=0
            for i in range(len(students)):
                if students[i]==sandwiches[indsan]:
                    flag=1
                    students.pop(i)
                    indsan+=1
                    break
        return len(students)


print(Solution().countStudents([1, 1, 0, 0], [0, 1, 0, 1]))