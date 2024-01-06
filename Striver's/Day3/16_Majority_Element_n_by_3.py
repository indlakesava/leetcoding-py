#https://leetcode.com/problems/majority-element-ii/
'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]


Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109

Follow up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution:
    def majorityElement(nums):
        nums.sort()

        left, right = 0,0
        target_count = len(nums)//3
        result = []

        while right<len(nums):
            if nums[left]==nums[right]:
                if right-left+1>target_count:
                    if nums[left] not in result:
                        result.append(nums[left])
                right += 1
            else:
                left=right

        return result

print(Solution.majorityElement([3,2,3]))

'''
Explanation:
Similar to the Majority Element 1 problem, We sort the array first 
Then we traverse from left to right checking the values and see if the right - left is >n/3
'''