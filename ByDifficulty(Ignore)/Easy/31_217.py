#https://leetcode.com/problems/contains-duplicate/
#217
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False

Or
“””
class Solution:	
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
“””
