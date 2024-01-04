#https://leetcode.com/problems/find-the-duplicate-number/description/
'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
'''

class Solution:
    def findDuplicate(nums):
        for i in range(len(nums)):
            if nums[abs(nums[i])]>0:
                nums[abs(nums[i])] *= -1
            else:
                return abs(nums[i])

'''
Explanation:
At each index we try to go to the value index and multiply the number by -1
and before checking we just verify if it's already visited by checking if it's -ve
if yes then we return that index else we keep continuing till we find the duplicate
'''