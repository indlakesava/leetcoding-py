#https://leetcode.com/problems/transpose-matrix/
#867
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []        
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            result.append(temp)
        
        return result
