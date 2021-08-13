#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#83
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(head==None or head.next==None):
            return head
        
        nextt = head.next
        cur = head
        
        while(nextt != None):
            if(cur.val == nextt.val):
                nextt = nextt.next
                cur.next = nextt
            else:
                cur = nextt
                nextt = cur.next
        
        return head
