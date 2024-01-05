#https://leetcode.com/problems/search-a-2d-matrix/
'''
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

class Solution:
    def searchMatrix(matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m*n-1

        while left<=right:
            mid = (left+right)//2
            mid_row, mid_col = divmod(mid, n)

            if(matrix[mid_row][mid_col]==target):
                return True
            elif(matrix[mid_row][mid_col]<target):
                left = mid+1
            else:
                right = mid-1
        return False

'''
Explanation:
Treat this as a 1D array instead of 2D array and we are just doing Binary search
have 2 variables left and right and then at each step find the mid and check if it's traget
else move left or right
Learning: divmod function returns tuple of quotient and remainder
'''