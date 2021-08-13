#https://leetcode.com/problems/first-bad-version/
#278
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = n
        l = 0
        r = n+1
        
        while(l<r):
            m = l+(r-l)//2
            if(isBadVersion(m)):
                if m<result:
                    result = m
                r = m
            else:
                l=m+1
                
        return result
