#https://leetcode.com/problems/valid-palindrome/
#125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=[]        
        for i in s:
            if i.isalnum():
                lst.append(i.lower())
        return lst==lst[::-1]
