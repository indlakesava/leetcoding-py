#https://leetcode.com/problems/pascals-triangle/
#118
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[1]]
        
        if(numRows == 1):
            return lst
        
        for i in range(1, numRows):
            lst.append([])
            for j in range(len(lst[i-1])+1):
                if(j==0 or j==len(lst[i-1])):
                    lst[i].append(1)
                else:
                    lst[i].append(lst[i-1][j-1] + lst[i-1][j])
                    
        return lst
