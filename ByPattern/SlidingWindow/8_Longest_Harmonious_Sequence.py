#https://leetcode.com/problems/longest-harmonious-subsequence/description/
'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0


Constraints:
1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
'''

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        res = 0
        for i in c:
            if i+1 in c:
                res = max(c[i]+c[i+1], res)
        return res

'''
Explanation:
We used counter of nums array to get the count frequency of each element
We run a for loop for each element in counter to check if it's immediate next element is present
if yes we count the current and next elements frequencies and the max of all is the result
'''