#https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        count = 0
        
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        
        for i in d.values():
            n = len(i)
            count += (n*(n-1))//2
        
        return count
        
        """
        #Brute Force
        n = len(nums)
        count = 0
        for i in range(0,n-1):
            for j in range(i+1,n):
                if(nums[i] == nums[j]):
                    count += 1
        return count
        """
        
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(1, n):
            for j in range(0, i):
                if(nums[i]==nums[j]):
                    count += 1
        return count