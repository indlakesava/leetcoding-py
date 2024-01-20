#https://leetcode.com/problems/robot-return-to-origin/
#657
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        lst = [0, 0]
        for i in moves:
            if i=='R':
                lst[0] += 1
            elif i=='L':
                lst[0] -= 1
            elif i=='U':
                lst[1] += 1
            elif i=='D':
                lst[1] -= 1
                
        return lst==[0,0]
