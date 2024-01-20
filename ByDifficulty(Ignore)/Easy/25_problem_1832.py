#https://leetcode.com/problems/check-if-the-sentence-is-pangram/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        
        for i in sentence:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            
        if len(d.keys())==26:
            return True
        else:
            return False