#https://leetcode.com/problems/3sum/
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''

class Solution:
    def threeSum(nums):
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum<0:
                    j+=1
                elif total_sum>0:
                    k-=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1

                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return ans

'''
Explanation:
We sort thr nums first to make sure we won't return duplicates and need not check the result everytime before appending
we also check if i is same as previous and go until the last of consecutive same number
we have 2 pointers j and k where j starts immediately next to i and k at the end of the array
we perform 2 sum between j and k and if we find any triplet with sum then we return their values
and keep moving j and k till we don't see a consecutive same number
this way we completely move i to the end of the array
'''