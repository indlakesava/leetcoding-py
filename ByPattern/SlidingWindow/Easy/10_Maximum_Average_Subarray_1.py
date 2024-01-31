#https://leetcode.com/problems/maximum-average-subarray-i/
'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:0+k])
        max_avg = s
        for i in range(k, len(nums)):
            s = s + nums[i] - nums[i-k]
            max_avg = max(max_avg, s)
        return max_avg/k

'''
Explanation:
We keep getting slices of size k using sliding window technique and the calculate 
sum by subtracting previous value and adding new index value and then taking average
At each iteration we try to see if it can be maximum average and store it and finally return it back
'''
