#https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.total_sum = 0
        
        def getSum(root):
            if(root == None):
                return
            if(root.val>=low and root.val<=high):
                self.total_sum += root.val  
                getSum(root.left)
                getSum(root.right)
            elif(root.val<low):
                getSum(root.right)                
            elif(root.val>high):
                getSum(root.left)

        getSum(root)    
        return self.total_sum
            