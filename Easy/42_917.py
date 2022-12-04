#https://leetcode.com/problems/reverse-only-letters/
#917
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lst_alpha = []
        
        for i in s:
            if i.isalpha():
                lst_alpha.append(i)
        
        lst_alpha = lst_alpha[::-1]
        st = "" 
        i = 0        
        for j in range(len(s)):
            if(s[j].isalpha()):
                st += lst_alpha[i]
                i+=1
            else:
                st += s[j]
                
        return st
            
