#https://leetcode.com/problems/max-consecutive-ones/
#485
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = 0
        temp = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                temp = temp+1
                max_val = max(max_val, temp)
            elif(nums[i] == 0):
                temp = 0
        return max_val
