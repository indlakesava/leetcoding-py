#https://leetcode.com/problems/longest-continuous-increasing-subsequence/
#674
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest_till_now = 1
        
        i=0
        j=1
        
        while(j<len(nums)):
            if(nums[j]>nums[j-1]):
                if(longest_till_now<(j-i+1)):
                    longest_till_now = j-i+1
                j+=1
            else:
                i = j
                j = i+1
        return longest_till_now
