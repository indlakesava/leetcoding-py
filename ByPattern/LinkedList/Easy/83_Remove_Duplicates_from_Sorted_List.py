#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(head):
        currentNode = head
        while currentNode and currentNode.next:
            nextNode = currentNode.next
            if currentNode.val==nextNode.val:
                currentNode.next = nextNode.next
            else:
                currentNode = nextNode
        return head

'''
Explanation:
we have current node and next node pointers 
if current node value and next node value is same then we move currentnode's next to nextnode's next
else we move the current node and next node. Finally return head once the loop ends.
'''
