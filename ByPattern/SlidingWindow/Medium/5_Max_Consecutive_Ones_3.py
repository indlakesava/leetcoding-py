#https://leetcode.com/problems/max-consecutive-ones-iii/description/

'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zeros = 0
        res = 0

        while right<len(nums):
            if nums[right]==0:
                zeros += 1

            if zeros<=k:
                res = max(res, right-left+1)
            else:
                while zeros>k:
                    if(nums[left]==0):
                        zeros -= 1
                    left += 1
            right += 1
        return res

'''
Explanation:
We slide using left, right pointers, Also have zeros variable to store the number of zeros at a given point
We keep traversing anf then if the value is zero then increment zeros variable
If zeros id less than k then we will proceed and find the res which is max of previous result and current window size
else, we try to move left pointer unti the zeros size is less than or equal to k
finally we return result once we reach en of array
'''
