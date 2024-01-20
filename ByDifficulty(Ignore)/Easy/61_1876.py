#https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
#1876
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        if(len(s)<3):
            return count
        for i in range(len(s)-2):
            if(len(set(s[i:i+3]))==3):
                count += 1
        return count
    
        """
        if(len(s)<3):
            return 0
        
        d = {}
        count = 0
        
        for i in range(3):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        
        if (2 in d.values()) or (3 in d.values()):
            count = 0
        else:
            count = 1
        d[s[i-2]] -= 1

        for i in range(3, len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            if (2 not in d.values()) and (3 not in d.values()):
                count += 1
            d[s[i-2]] -= 1
            
        return count
        """
