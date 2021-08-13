#https://leetcode.com/problems/backspace-string-compare/
#844
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_lst = []
        t_lst = []
        for i in s:
            if i != '#':
                s_lst.append(i)
            else:
                if(len(s_lst)!=0):
                    s_lst.pop()
                
        for i in t:
            if i != '#':
                t_lst.append(i)
            else:
                if(len(t_lst)!=0):
                    t_lst.pop()
                
        return s_lst==t_lst
