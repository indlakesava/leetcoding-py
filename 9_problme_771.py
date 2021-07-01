#https://leetcode.com/problems/jewels-and-stones/submissions/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #using dictionary
        d = {}        
        for i in stones:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        count = 0
        for i in jewels:
            if i in d.keys():
                count += d[i]
                
        return count

        """
        #Brute Force
        count = 0
        for i in jewels:
            for j in stones:
                if(i == j):
                    count+=1
        return count
        """
        
                    