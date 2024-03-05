#https://leetcode.com/problems/rotate-list/description/
'''
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(head, k):
        if not head or k==0:
            return head

        length = 1
        moving = head

        while moving.next:
            length += 1
            moving = moving.next

        moving.next = head
        k = k%length

        start = None
        length = length - k - 1
        moving = head

        for i in range(length):
            moving = moving.next

        start = moving.next
        moving.next = None

        return start

'''
Explanation:
We try to find the length of the linked list first and do mod of k by len
while finding length when we traverse we point the last pointer to head so we form a cycle
now we move a moving pointer by lenght-k-1 and then point the start pointer to it's next 
and then change it's next to none and return start
'''
