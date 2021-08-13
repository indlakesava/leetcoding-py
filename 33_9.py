#https://leetcode.com/problems/palindrome-number/
#9
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        s = 0
        n = x
        while(n>0):
            temp = n%10
            s = s*10 + temp
            n = n//10
        
        return s==x

“””
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False        
        return str(x)==str(x)[::-1]
”””
