#https://leetcode.com/problems/permutations/description/
'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

class Solution:
    def permute(nums):
        result = []
        def helper(used, unused):
            if not unused:
                result.append(used)
                return
            for i in range(len(unused)):
                helper(used + [unused[i]], unused[:i] + unused[i+1:])

        helper([], nums)
        return result

print(Solution.permute([1,2,3]))

'''
Explanation:
we use a helper function to run recursively with 2 parameters used and unused
once we use all the numbers in the list in that call we add it to the result
'''



