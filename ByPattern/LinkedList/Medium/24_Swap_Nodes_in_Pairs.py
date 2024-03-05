#https://leetcode.com/problems/swap-nodes-in-pairs/description/

'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(head):
        dummy = ListNode(0)
        result = dummy

        if head==None or head.next==None:
            return head

        while head and head.next:
            temp = head
            dummy.next = head.next
            head = head.next.next
            dummy.next.next = temp
            temp.next = head
            dummy = temp

        return result.next

    def swapPairs1(head):
        h = head


        while h and h.next:
              h.val, h.next.val = h.next.val, h.val

              h = h.next.next

        return head

'''
Explanation:
In the first slution we are trying to rotate the nodes by saving their next nodes in temporary variables
Where as in the second solution we are just swapping the values between 2 consecutive nodes and moving 2 places
'''
