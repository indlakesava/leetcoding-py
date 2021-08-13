#https://leetcode.com/problems/subarray-sum-equals-k/
#560
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        arr_sum = 0
        count = 0
        d = {}
        
        for i in range(len(nums)):
            arr_sum += nums[i]
            if(arr_sum==k):
                count += 1
            if (arr_sum-k) in d.keys():
                count+=d[arr_sum-k]
            if(arr_sum in d):
                d[arr_sum] += 1
            else:
                d[arr_sum] = 1

        return count
