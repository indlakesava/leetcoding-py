#https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
'''
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

Example 2:
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.

Constraints:
1 <= arr.length <= 105
1 <= arr[i] <= 104
1 <= k <= arr.length
0 <= threshold <= 104
'''

class Solution:
    def numOfSubarrays(arr, k, threshold):
        cur_sum = sum(arr[:k])
        res = 0 if cur_sum/k<threshold else 1

        for i in range(k, len(arr)):
            cur_sum += arr[i] - arr[i-k]
            if (cur_sum/k)>=threshold:
                res += 1

        return res

'''
Explanation:
First we find the sum of first k nums and then we find the average and inititlize res variable with
0 if avg is less than threshold else we assign 1. 
Now we use sliding window technique and keep removing left most element and add right most element from sum
and calculate average and repeat comparing with threshold and then increment result by 1 accordingly
return result one we reach end of array
'''
