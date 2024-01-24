#https://leetcode.com/problems/single-element-in-a-sorted-array/description/
'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10


Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 105
'''

class Solution:
    def singleNonDuplicate(nums):
        result = nums[0]
        for i in nums[1:]:
            result ^= i
        return result

    def singleNonDuplicate1(nums):
        left = 0
        right = len(nums)-1

        while left<right:
            mid = (right+left)//2
            if mid%2==1:
                mid -= 1

            if(nums[mid] != nums[mid+1]):
                right = mid
            else:
                left = mid+2
        return nums[left]

print(Solution.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(Solution.singleNonDuplicate1([1,1,2,3,3,4,4,8,8]))

'''
Explanation:
Xor of same number results in 0 and if all the elements are duplicate except 1 then
we can do xor of all numbers which will result in xor of single element and 0 = single element

Second way of dealing this question is using binary search
if we find the middle element, if the mid is odd then we go one step back 
and see if the mid and mid+1 is same, if yes, we move the left to mid+2, else we move right to mid
'''