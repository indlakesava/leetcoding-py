#https://leetcode.com/problems/max-consecutive-ones/description/
'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2


Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

class Solution:
    def findMaxConsecutiveOnes(nums):
        max_val = 0
        temp = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                temp = temp+1
                max_val = max(max_val, temp)
            elif(nums[i] == 0):
                temp = 0
        return max_val

'''
Explanation:
We keep traversing from the beginning of the array and at each index we try to check
if the value is 1 or 0, if it's 1 we increment temp count by 1 and then compare this with global max
if it's 0 then we assign temp with 0 to free it to represent start of the next consecutive 1's
'''