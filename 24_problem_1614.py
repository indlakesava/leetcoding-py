#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        cur_depth = 0
        for i in s:
            if(i=='('):
                cur_depth += 1
                max_depth = max(max_depth, cur_depth)
            elif(i==')'):
                cur_depth -= 1
                
        return max_depth