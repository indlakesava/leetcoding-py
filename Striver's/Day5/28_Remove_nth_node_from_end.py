#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Follow up: Could you do this in one pass?
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        p = head
        while p.next:
            length += 1
            p = p.next

        indextoberemoved = length-n

        if length==1:
            return None

        if indextoberemoved==0:
            return head.next

        cur = head
        res = cur
        while indextoberemoved-1:
            cur = cur.next
            indextoberemoved-=1

        if cur.next.next:
            cur.next = cur.next.next
        else:
            cur.next = None

        return res

'''
Explanation:
We find the length of the linked list first and then we find the index of the element to be removed
We run few edge cases and then we travere a temp noed to the index before the one we need to remove
We check if the index to be removed has next, if yes then we update the temp node next as it's next.next
else we update it with None marking it as end of the linked list
'''