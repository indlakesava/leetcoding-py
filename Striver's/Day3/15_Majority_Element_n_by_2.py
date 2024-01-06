#https://leetcode.com/problems/majority-element/

'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
'''

class Solution:
    def majorityElement(nums):
        nums.sort()
        return nums[len(nums)//2]

    def majorityElement1(nums):
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for a,b in d.items():
            if b>len(nums)//2:
                return a

print(Solution.majorityElement([2,2,1,1,1,2,2]))
print(Solution.majorityElement1([2,2,1,1,1,2,2]))

'''
Explanation:
Since the majority element will be present in more than half palces if we sort,
we can return the middle element which will be the majority element 

in the second solution, we are creating a dictionary with counter as value
now we iterate over each element in dictionary are return any element which has value more than half length of array
'''