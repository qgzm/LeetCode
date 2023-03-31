# 使用者：姜海波
# 创建时间：2023/3/31  14:51
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        for i in asteroids:
            if len(ans)==0:
                ans.append(i)
                continue
            while len(ans)>0:
                last=ans[-1]
                # 会发生碰撞
                if last>0 and i<0:
                    ans.pop()
                    # 左大右小,左进右弃
                    if abs(last)>abs(i):
                        ans.append(last)
                        break
                    # 左右相同,都弃
                    elif last==-i:
                        break
                    # 左小右大,左弃右继
                    else:
                        if len(ans)==0:
                            ans.append(i)
                            break
                        continue
                else:
                    ans.append(i)
                    break

        return ans


print(Solution().asteroidCollision([1, -2, -2, -2]))


