#https://leetcode.com/problems/set-matrix-zeroes/description/
'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

def setZeroes(matrix):
	"""
	Do not return anything, modify matrix in-place instead.
	"""
	temp = 1
	for i in range(0, len(matrix)):
		if(matrix[i][0]==0):
			temp = 0
		for j in range(1, len(matrix[0])):
			if(matrix[i][j]==0):
				matrix[i][0]=0
				matrix[0][j]=0

	for i in range(len(matrix)-1, -1, -1):
		for j in range(len(matrix[0])-1, -1, -1):
			if(matrix[i][0]==0 or matrix[0][j]==0):
				matrix[i][j]=0
		if(temp==0):
			matrix[i][0] = 0

	'''
	#Printing as matrix
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(matrix[i][j], end=" ")
		print('')
	'''

setZeroes([[1,1,1],[1,0,1],[1,1,1]])

'''
Explanation:
We need to check each cell and if it's value os 0 we need to store the status somewhere 
so we can update entire row and column later, because if we do at the moment we might miss others
We will use row 0 and col 0 to have the status of that particular row or column  
We need a temp variable to store the column status since we are updating both column and row 
Once we traverse completely and store the value, we update the corresponding rows and cols to 0
But we start from the ends because if we convert the row0 and col0 in the beginning the statuses will be missed 

In Bruteforce we can use additional space of 1 col and 1 row sized matrices and then store the corresponding statuses 
'''