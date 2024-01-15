#https://leetcode.com/problems/combination-sum/description/
'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []


Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
'''

class Solution:
    def combinationSum(candidates, target):
        ans = []
        ds = []

        def findCombinations(index, target):
            if index==len(candidates):
                if target==0:
                    ans.append(ds[:])
                return

            if candidates[index]<=target:
                ds.append(candidates[index])
                findCombinations(index, target - candidates[index])
                ds.pop()
            findCombinations(index+1, target)
        findCombinations(0, target)
        return ans

print(Solution.combinationSum([2,3,6,7], 7))
'''
Explanation:
Initially, the index will be 0, target as given and the data structure(vector or list) will be empty
Now there are 2 options viz to pick or not pick the current index element.
If you pick the element, again come back at the same index as multiple occurrences of the same element is possible so the target reduces to target – arr[index] (where target -arr[index]>=0)and also insert the current element into the data structure.
If you decide not to pick the current element, move on to the next index and the target value stays as it is. Also, the current element is not inserted into the data structure.
While backtracking makes sure to pop the last element as shown in the recursion tree below.
Keep on repeating this process while index < size of the array for a particular recursion call.
You can also stop the recursion when the target value is 0, but here a generalized version without adding too many conditions is considered.
Using this approach, we can get all the combinations.
'''