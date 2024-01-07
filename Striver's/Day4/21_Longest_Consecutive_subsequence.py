#https://leetcode.com/problems/longest-consecutive-sequence/description/
'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

class Solution:
    def longestConsecutive(nums):
        numset = set(nums)
        max_length = 0
        for i in nums:
            if i-1 not in numset:
                temp_length=1
                while i+temp_length in numset:
                    temp_length+=1
                max_length = max(max_length, temp_length)
        return max_length

print(Solution.longestConsecutive([100,4,200,1,3,2]))

'''
Explanation:
We convert the given list to set so it's easy to check if a number is available
at each index, we try to check for consecutive sequence and see if it can be the longest one
'''