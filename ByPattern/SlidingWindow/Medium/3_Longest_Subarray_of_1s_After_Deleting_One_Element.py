#https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
'''
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

class Solution:
    def longestSubarray(nums) -> int:
        left = 0
        zeros = 0
        res = 0

        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1
            while zeros>1:
                if nums[left]==0:
                    zeros-=1
                left+=1

            res = max(res, right-left+1-zeros)
        if zeros==0:
            return res-1
        return res

'''
Explanation:
We start creating windows starting with left and right pointers
at each point if an numb is zero then we store it in zeros variable and at each point we calculate the 
window size as number of 1s and assign it to result if it's max than previous result
Along with that if we see more than 1 zero in this window we try to reduce the window size and complete 
iterating till end of array. Finally we return the result anf if there were no zeros then we return result-1
'''
