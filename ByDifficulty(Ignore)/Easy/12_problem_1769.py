#https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left = [0]*len(boxes)
        right = [0]*len(boxes)
        result = []
        
        left[0] = 0
        count = int(boxes[0])
        for i in range(1, len(boxes)):
            left[i] = left[i-1] + count
            count += int(boxes[i])
            
        right[-1] = 0
        count = int(boxes[-1])
        for j in range(len(boxes)-2, -1, -1):
            right[j] = right[j+1] + count
            count += int(boxes[j])
        
        result = [i+j for i,j in zip(left, right)]
        
        return result
            
        """
        #Brute Force solution T=O(n^2), S=O(n)
        lst = []
        for i in range(len(boxes)):
            count = 0
            for j in range(len(boxes)):
                if(boxes[j] == '1'):
                    count += abs(i-j)
            lst.append(count)
        
        return lst
        """