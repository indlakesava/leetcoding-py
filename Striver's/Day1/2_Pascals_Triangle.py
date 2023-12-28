#https://leetcode.com/problems/pascals-triangle/
'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]


Constraints:
1 <= numRows <= 30
'''

class Solution:
    def generate(numRows):
        ans = [[1]]
        for i in range(numRows-1):
            temp = [0] + ans[-1] + [0]
            row = []
            for j in range(len(temp)-1):
                row.append(temp[j]+temp[j+1])
            ans.append(row)
        return ans

print(Solution.generate(5))

'''
Explanation:
We intiate the result with a 2D array with 1 row
We have a temp list to build the structure of the upcoming row  
then we iterate over it and add 2 consecutive values to form the current value
Once we form the row we then add it to the result 
'''