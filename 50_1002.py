#https://leetcode.com/problems/array-partition-i/
#561
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sums = 0
        for i in range(len(nums)//2):
            sums += nums[i*2]
        return sums