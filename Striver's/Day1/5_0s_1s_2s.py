#https://leetcode.com/problems/sort-colors/

'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?
'''

class Solution:
    def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        twos = len(nums)-1
        moving = 0

        while moving<=twos:
            if nums[moving]==0:
                nums[moving], nums[zeros] = nums[zeros], nums[moving]
                zeros += 1
                moving += 1
            elif nums[moving]==1:
                moving += 1
            elif nums[moving]==2:
                nums[moving], nums[twos] = nums[twos], nums[moving]
                twos-=1

        print(nums)

Solution.sortColors([2,0,2,1,1,0])

'''
Explanation:
We have 3 pointers, one which is moving and one for zeros and one for twos
We keep moving and based on the current number we swap the values and move th pointers accordingly
'''