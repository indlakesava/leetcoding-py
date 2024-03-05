#https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
'''
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

Follow up: Can you flatten the tree in-place (with O(1) extra space)?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(root):
        """
        Do not return anything, modify root in-place instead.
        """
        dp = []

        # pretraversal
        def dfs(node):
            if not node:
                return
            dp.append(node)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        node = root

        for i in range(1, len(dp)):
            node.left = None
            node.right = dp[i]
            node = node.right

'''
Explanation:
We convert given binary tree into a list of nodes first in the order they should be in result
We iterate over the list to create the linked list but we assign node.left=Node so that 
even it's a tree it looks like a linked list and we return the root(head)
'''
