#https://leetcode.com/problems/remove-linked-list-elements/description/

'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(head, val):
        if head == None:
            return head

        current = head
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head if head.val != val else head.next

'''
Explanation:
We cover the base case where the linked list is empty
we have a current pointer starting from head.next to check if cur val is not give one
if not we move current to next else we move current to current.next.next
finally we check head if it's value is given value and return head.next else return head
'''