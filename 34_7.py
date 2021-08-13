#https://leetcode.com/problems/reverse-integer/
#7
class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        
        if(x<0):
            neg = -1
            x = -1*x
        
        rev = 0
        while(x>0):
            rev = rev*10 + x%10
            x = x//10
        
        if(rev>(pow(2, 31)-1)):
            return 0
        
        else:
            return neg*rev
