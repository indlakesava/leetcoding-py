#https://leetcode.com/problems/subsets-ii/
'''
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''
class Solution:
    def subsetsWithDup(nums):
        """
        level0    []
        level1    [1]          [2]
        level2    [1,2]        [2,2]
        level3    [1,2,2]
        """
        def backtracking(start,subset):
            res.append(list(subset))
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtracking(i+1,subset)
                subset.pop()
        nums.sort()
        res = []
        backtracking(0,[])
        return res


print(Solution.subsetsWithDup([1, 2, 3]))

'''
Sort the input array.Make a recursive function that takes the input array ,the current subset,the current index and  a list of list/ vector of vectors to contain the answer.
Try to make a subset of size n during the nth recursion call and consider elements from every index while generating the combinations. Only pick up elements that are appearing for the first time during a recursion call to avoid duplicates.
Once an element is picked up, move to the next index.The recursion will terminate when the end of array is reached.While returning backtrack by removing the last element that was inserted.
'''