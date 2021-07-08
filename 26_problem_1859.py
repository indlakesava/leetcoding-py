#https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split(' ');        
        lst = sorted(lst, key=lambda a: int(a[-1]))
        lst = [a[:-1] for a in lst]
        return ' '.join(lst)