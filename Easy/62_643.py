#https://leetcode.com/problems/maximum-average-subarray-i/
#643
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:0+k])
        max_avg = s
        for i in range(k, len(nums)):
            s = s + nums[i] - nums[i-k]
            max_avg = max(max_avg, s)
        return max_avg/k
